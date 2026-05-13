from zillow_scraper import ZillowFiller

filler = ZillowFiller()

links, prices, addresses = filler.get_listings()

for address, price, link in zip(addresses, prices, links):
    filler.fill_form(address, price, link)

filler.driver.quit()

