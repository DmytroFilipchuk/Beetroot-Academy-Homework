
"""
Task 2

Load data

Download all comments from a subreddit of your choice using URL: https://api.pushshift.io/reddit/comment/search/ .

As a result, store all comments in chronological order in JSON and dump it to a file.


"""

import json
import requests

params = {'subreddit':'worldnews',
          'size': '500',
          'sort': 'score:desc'}

comments = requests.get('https://api.pushshift.io/reddit/comment/search/',
                        params=params ).json()

data = {'comments': []}

for id, comment in enumerate(comments['data']):
    data['comments'].append({'id' : id,
                        'Comment: ': comment['body'],
                        'Author' : comment['author'],
                        })

with open('comments.json', 'w') as f:
    json.dump(data, f)


"""
Task 3

The Weather app

Write a console application which takes as an input a city name and returns current weather in the
format of your choice. For the current task, you can choose any weather API or website or use openweathermap.org

"""
import requests


class WeatherApp:

    api = 'https://api.openweathermap.org/data/2.5/weather/'

    units = {'Fahrenheit: key - F': 'imperial',
             'Celsius: key - C': 'metric',
             'Kelvin: key - K': ''}  # Kelvin is a default unit

    appid = 'b6c1b41761bfad97bd1a4740afdb44a0'

    def __init__(self):
        pass

    @staticmethod
    def enter_city():
        return input('Enter a city: ')

    def display_units(self):
        for unit in self.units.keys():
            print(unit)

    def choose_a_unit(self):

        self.display_units()
        choice = input("Enter a key for a desired unit: ")

        for unit in self.units.keys():

            if choice == unit[-1]:
                return self.units[unit]

        raise Exception(f'There is no "{choice}" key ')

    def setup_params(self):

        city = self.enter_city()
        unit = self.choose_a_unit()

        params = {'q': city,
                  'appid': f'{self.appid}',
                  'units': unit}

        return params

    def request(self):
        return requests.get(f'{self.api}',
                            params=self.setup_params()).json()

    def get_temp(self):
        return self.request()['main']['temp']

    def main(self):

        try:
            temp = self.get_temp()
        except KeyError:
            return 'There is no such city in the database'

        return temp


a = WeatherApp()
print(a.main())