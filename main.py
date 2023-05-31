import requests
import json

api = "https://api.iplocation.net/?ip="

def get_data():
    news_in = requests.get(api)
    data_format(news_in.content)


def data_format(dt_data):
    json_object = json.loads(dt_data)
    json_formatted_str = json.dumps(json_object, indent=2)
    to_jsonfile_write(json_formatted_str)

def to_jsonfile_write(dt):
    with open('news.json', 'w') as w:
        w.write(dt)
        w.flush()
        w.close()