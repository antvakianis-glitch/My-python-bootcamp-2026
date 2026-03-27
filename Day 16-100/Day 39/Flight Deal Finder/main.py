#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from datetime import datetime, timedelta
import time
import json
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

notified_cities = []

# Get destination data
sheet_data = data_manager.get_destination_data()

# Define dates
TRIP_DURATION = 7
DAYS_AHEAD = 1

departure_date = datetime.now() + timedelta(days=DAYS_AHEAD)
return_date_obj = departure_date + timedelta(days=TRIP_DURATION)

departure = departure_date.strftime("%Y-%m-%dT00:00:00")
return_date = return_date_obj.strftime("%Y-%m-%dT00:00:00")

print(f"Searching {TRIP_DURATION}-day trips")
print(f"Departure: {departure_date.strftime('%d %B %Y')}")
print(f"Return: {return_date_obj.strftime('%d %B %Y')}\n")

for row in sheet_data:
    destination_id = row["iataCode"]

    if not destination_id or destination_id == "N/A":
        print(f"Skipping {row['city']} - No valid City ID found.")
        continue

    print(f"\n{'=' * 60}")
    print(f"Checking flights for {row['city']} ({destination_id})")
    print('=' * 60)

    flight_result = flight_search.check_flights(
        origin_city_code="City:belgrade_rs",
        destination_city_code=destination_id,
        from_time=departure,
        to_time=return_date
    )

    try:
        itineraries = flight_result.get("itineraries", [])

        if not itineraries:
            print(f"❌ No flights found")
            continue

        first_item = itineraries[0]
        price = first_item.get("price", {}).get("amount")

        if not price:
            print(f"❌ No price found")
            continue

        # Get flight details
        outbound = first_item.get("outbound", {})
        sector_segments = outbound.get("sectorSegments", [])

        # Get airline
        airline = "Unknown Airline"
        if sector_segments:
            first_segment = sector_segments[0].get("segment", {})
            carrier = first_segment.get("carrier", {})
            airline = carrier.get("name", "Unknown Airline")

        # Calculate stops
        num_stops = len(sector_segments) - 1

        # Flight type
        if num_stops == 0:
            flight_type = "✈️ Direct flight"
        elif num_stops == 1:
            flight_type = "✈️ 1 stop"
        else:
            flight_type = f"✈️ {num_stops} stops"

        float_price = float(price)

        # ═══════════════════════════════════════
        # Get booking URL
        # ═══════════════════════════════════════
        booking_url = None
        booking_options = first_item.get("bookingOptions", {})
        edges = booking_options.get("edges", [])

        if edges:
            first_option = edges[0].get("node", {})
            relative_url = first_option.get("bookingUrl")

            if relative_url:
                # Convert relative to absolute URL
                booking_url = f"https://www.kiwi.com{relative_url}"

        # Display flight info
        print(f"\n💰 Price: {float_price}€")
        print(f"✈️  Airline: {airline}")
        print(f"🛫 Flight Type: {flight_type}")

        if booking_url:
            print(f"🔗 Booking: {booking_url}")

        # Build layover messages
        layover_messages = []

        if num_stops > 0:
            print(f"\n📍 Layover Details:")

            for i, segment_obj in enumerate(sector_segments[:-1]):
                segment = segment_obj.get("segment", {})
                layover = segment_obj.get("layover")

                destination_station = segment.get("destination", {}).get("station", {})
                stopover_code = destination_station.get("code") or "???"
                stopover_city = destination_station.get("city", {}).get("name") or "Unknown"

                duration_str = None
                if layover:
                    duration_seconds = layover.get("duration", 0)
                    if duration_seconds > 0:
                        duration_hours = duration_seconds / 3600
                        duration_minutes = (duration_seconds % 3600) / 60

                        if duration_hours >= 1:
                            duration_str = f"{int(duration_hours)}h {int(duration_minutes)}m"
                        else:
                            duration_str = f"{int(duration_minutes)}m"

                if duration_str:
                    msg = f"Stop {i + 1}: {stopover_city} ({stopover_code}) - {duration_str} layover"
                else:
                    msg = f"Stop {i + 1}: {stopover_city} ({stopover_code})"

                print(f"  {msg}")
                layover_messages.append(msg)

        layover_info = "\n".join(layover_messages) if layover_messages else None

        print()

        # Check if it's a deal
        if float_price < row["lowestPrice"] and row["city"] not in notified_cities:
            print(f"🚨 DEAL ALERT! Price below {row['lowestPrice']}€ threshold!")

            notification_manager.send_email(
                price_amount=price,
                city_dest=row["city"],
                airline=airline,
                flight_type=flight_type,
                layover_info=layover_info,
                booking_url=booking_url  # ← Πρόσθεσε το booking URL
            )
            notified_cities.append(row["city"])
        elif float_price >= row["lowestPrice"]:
            print(f"ℹ️  Price is above threshold ({row['lowestPrice']}€)")

    except Exception as e:
        print(f"\n❌ Error processing {row['city']}: {e}")
        import traceback

        traceback.print_exc()

    time.sleep(2)

print("\n" + "=" * 60)
print("🎉 Search completed!")
print(f"📧 Sent {len(notified_cities)} notification(s)")
if notified_cities:
    print(f"   Cities: {', '.join(notified_cities)}")
print("=" * 60)



