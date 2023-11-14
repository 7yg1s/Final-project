from live


#Map data update:
def live_map_data():
    while True:
        live_air_quality_monitoring_scraper()
        time.sleep(10800)
live_map_data()

#Update live_data_scraper.py
def live_data_scraper_update():
    while True:
        live_data_scraping()
        time.sleep(86400)
live_data_scraper_update()
