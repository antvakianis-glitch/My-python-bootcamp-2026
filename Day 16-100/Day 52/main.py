from google_data_scrab import GoogleDataScraper

bot = GoogleDataScraper()

bot.open_maps()
bot.search("cafes Novi Sad")
bot.scroll_results()
bot.extract_data()
bot.save_to_excel()
bot.close()