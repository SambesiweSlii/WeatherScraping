# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 19:04:14 2025

@author: SambesiweSli
"""

# this program's purpose is to help us
# scrape weather content from a website.
from requests_html import HTMLSession

# this is the html session we will be using
session = HTMLSession()

# here we enter the location we want. in time it will ask for the user's input.
location = input('You want the weather data of which city? -- ')
print('\n')

# this is where we store the url of the website we need
# the location within the link was replaced by the location variable.
url = f'https://www.google.com/search?q=weather+{location}'

# here we are requesting for a session to start with the scraping process
request = session.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Avast/131.0.0.0'})

'''the if statements code is meant to assist with overcoming the 
AttributeError: "NoneType" object has no attribute "text"'''

# this line of code helps us retrieve the temperature from the website
temperature = request.html.find('span#wob_tm', first=True)

if temperature is not None:
    temp = temperature.text
else:
    temp = None
    
unit = request.html.find('div.vk_bk.wob-unit span.wob_t', first=True)

if unit is not None:
    celcius = unit.text
else:
    celcius = None
    
forecast = request.html.find('div.wob_dcp span#wob_dc', first=True)

if forecast is not None:
    description = forecast.text
else:
    description = None

# retrieving our element title with this line of code
print(request.html.find('title'))

# retrieving the title of the web site with this line of code
print(request.html.find('title', first=True).text)
print('=====================================================')
print('\n')

# and here we are retrieving the temperature using the tags
# within the websites html file. These tags are the span and the id of the span tag
# the temperature uses
print(f'The weather forecast for {location} is {temp}{celcius} {description}.')