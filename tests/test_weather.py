from lib.weather import Weather

def test_weather_instantiates():
    weather = Weather()

    assert isinstance(weather, Weather)

def test_weather_sunny_returns_sunglasses():
    weather = Weather()

    assert weather.lets_go_out() == 'Its sunny, take sunglasses!'

def test_weather_rainy_returns_raincoat():
    weather = Weather()

    assert weather.lets_go_out() == 'Its rainy, take a raincoat!'