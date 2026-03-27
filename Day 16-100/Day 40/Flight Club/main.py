#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from datetime import datetime, timedelta
import time
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

# Get customer emails
print("📧 Loading subscriber list...")
customers = data_manager.get_customer_emails()
print(f"Found {len(customers)} subscribers\n")

# Get destinations
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

deals_found = []

# Search for deals
for row in sheet_data:
    destination_id = row["iataCode"]

    if not destination_id or destination_id == "N/A":
        continue

    print(f"\nChecking {row['city']}...")

    flight_result = flight_search.check_flights(
        origin_city_code="City:belgrade_rs",
        destination_city_code=destination_id,
        from_time=departure,
        to_time=return_date
    )

    try:
        itineraries = flight_result.get("itineraries", [])

        if not itineraries:
            continue

        first_item = itineraries[0]
        price = first_item.get("price", {}).get("amount")

        if not price:
            continue

        float_price = float(price)

        # Get flight details
        outbound = first_item.get("outbound", {})
        sector_segments = outbound.get("sectorSegments", [])

        airline = "Unknown"
        if sector_segments:
            carrier = sector_segments[0].get("segment", {}).get("carrier", {})
            airline = carrier.get("name", "Unknown")

        # Get booking URL
        booking_url = None
        edges = first_item.get("bookingOptions", {}).get("edges", [])
        if edges:
            relative_url = edges[0].get("node", {}).get("bookingUrl")
            if relative_url:
                booking_url = f"https://www.kiwi.com{relative_url}"

        print(f"  💰 {float_price}€ with {airline}")

        # Check if deal
        if float_price < row["lowestPrice"]:
            print(f"  🚨 DEAL! Below {row['lowestPrice']}€ threshold")

            deals_found.append({
                "city": row["city"],
                "price": price,
                "airline": airline,
                "booking_url": booking_url
            })

    except Exception as e:
        print(f"  ❌ Error: {e}")

    time.sleep(2)

# Send emails to all subscribers
if deals_found:
    print(f"\n{'=' * 60}")
    print(f"📧 Sending {len(deals_found)} deal(s) to {len(customers)} subscriber(s)")
    print('=' * 60)

    for deal in deals_found:
        print(f"\n🎉 Sending alert for {deal['city']} ({deal['price']}€)...")

        sent_count = 0
        failed_count = 0

        for customer in customers:
            success = notification_manager.send_email(
                to_email=customer["email"],
                to_name=customer.get("firstName", "Traveler"),
                price_amount=deal["price"],
                city_dest=deal["city"],
                airline=deal["airline"],
                booking_url=deal.get("booking_url")
            )

            if success:
                sent_count += 1
            else:
                failed_count += 1

            time.sleep(0.5)  # Small delay between emails

        print(f"  ✅ Sent: {sent_count}")
        if failed_count > 0:
            print(f"  ❌ Failed: {failed_count}")

else:
    print("\n❌ No deals found today")

print(f"\n{'=' * 60}")
print("🎉 Search completed!")
print('=' * 60)



