import requests
import json
import sys
ip = sys.argv[1]
api = f"https://api.iplocation.net/?ip={ip}"

def get_data():
    news_in = requests.get(api)
    data_format(news_in.content)


def data_format(dt_data):
    json_object = json.loads(dt_data)
    json_formatted_str = json.dumps(json_object, indent=2)
    print(json_formatted_str)

get_data()