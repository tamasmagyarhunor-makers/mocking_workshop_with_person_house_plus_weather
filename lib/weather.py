import random

class Weather():
    def __init__(self):
        pass

    def lets_go_out(self):
        current_weather = random.choice(['sunny', 'rainy'])
        
        if current_weather == 'sunny':
            return 'Its sunny, take sunglasses!'
        else:
            return 'Its rainy, take a raincoat!'