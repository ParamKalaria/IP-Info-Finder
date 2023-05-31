import requests
import json

api = "https://api.iplocation.net/?ip=8.8.8.8"

def get_data():
    news_in = requests.get(api)
    data_format(news_in.content)


def data_format(dt_data):
    json_object = json.loads(dt_data)
    json_formatted_str = json.dumps(json_object, indent=2)
    print(json_formatted_str)

get_data()