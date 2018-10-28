import logging
from yahooweather import YahooWeather, UNIT_C

def predictWeather(woeid):
	logging.basicConfig(level=logging.WARNING)

	yweather = YahooWeather(woeid, UNIT_C)
	if yweather.updateWeather():
		print("RawData: %s" % str(yweather.RawData))
		print("Units: %s" % str(yweather.Units))
		print("Now: %s" % str(yweather.Now))
		print("Forecast: %s" % str(yweather.Forecast))
		print("Wind: %s" % str(yweather.Wind))
		print("Atmosphere: %s" % str(yweather.Atmosphere))
		print("Astronomy: %s" % str(yweather.Astronomy))
		return yweather.Now,yweather.Forecast,yweather.Wind,yweather.Atmosphere,yweather.Astronomy
	else:
		print("Can't read data from yahoo!")

