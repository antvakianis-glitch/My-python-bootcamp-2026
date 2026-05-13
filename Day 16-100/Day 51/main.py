import warnings
from data_scraping import InternetSpeedTwitterBot
warnings.filterwarnings("ignore")

connection = InternetSpeedTwitterBot()

connection.get_connection()

connection.get_speeds()

connection.check_speed_and_notify()



