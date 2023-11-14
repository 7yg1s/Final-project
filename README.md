Air quality monitoring and analysis
Created by: Žygimantas Rėkus and Nerijus Čiuželis, 2023-11-16
imgpng

Air particulate matter monitoring and analysis.

This is the final project for Data analytics course at Vilnius Coding School. The goal is to get all the necessary data from a web, clean it and analyse. Check how air quality is changing according years, region and compare statistics to live data from different cities in Lithuania. For this project we used Python language with some of its libraries, CSV files for saving data and PowerBi for visualisations.

Libraries used in this project: Pandas, Folium, Timestamp, Selenium,

who_data_scraper.py: Libraries: Time, Pandas, Selenium.

Steps:
1. Using Selenium library we createad connection to WHO website.
    (https://whoairquality.shinyapps.io/AmbientAirQualityDatabase/)
2. With Selenium WebDriver we filtered the data on the website.
3. Usind Pandas Dataframe we saved the data into a CSV file.
live_data_scraper.py: Libraries: BeautifulSoup, Time, Requests, DateTime, Pandas.

Steps:
1. We scraped the data of major cities of Lithuania using BeautifulSoup.
    (https://aqicn.org/)
2. With Pandas we create a dataframe and stored the live data into a CSV file.
3. We created if function to check whether the file exists and has today's, if it doesn't have data then the new data will be appended.
live_air_quality_monitoring.py Libraries: Requests, Folium.

1. We connected to a website using Folium and API of https://aqicn.org/.
2. Created interactive map with live data and stored it as html file.
