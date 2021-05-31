import requests
import json
import webbrowser


apodurl = 'https://api.nasa.gov/planetary/apod?'
mykey = 'ymcaYSVggh5ZrAc8596LmdsKY74qcMfIRK3VZ44X'

params = {'api_key':mykey,
          'hd':'True',
          'date':'2021-05-24'}

response = requests.get(apodurl,params=params)
json_data = json.loads(response.text)
print(json_data)

image_url = json_data['hdurl']

webbrowser.open(image_url)



