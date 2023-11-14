import aqi



myaqi = aqi.to_aqi([
    (aqi.POLLUTANT_PM25, '12'),
    (aqi.POLLUTANT_PM10, '24'),
    (aqi.POLLUTANT_O3_8H, '0.087')
])


print(myaqi)