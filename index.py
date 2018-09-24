import json
import random
from pprint import pprint
from flask import Flask, request, url_for, redirect
app = Flask(__name__)

@app.route("/")
def main():
    return "Hello World!"

@app.route("/recommend/<keyword>", methods=['GET', 'POST'])
def recommend(keyword):
    if request.method == 'GET':
        assert keyword == request.view_args['keyword']
        keyword_list = keyword.split(",")

        filename = "seoul_culture"
        result = {}
        data = get_json_file(filename, keyword_list)

        # print('keyword=>', keyword)
        # print('keyword_list=>', keyword_list)

        result['responseStatus'] = 200
        result['data'] = data
        result_data = json.dumps(result)

        return result_data


def get_json_file(fileName, keyword_list):
    with open(fileName+'.json') as f:
        file_data = json.load(f)
        data_list = file_data.get('DATA')
        random.shuffle(data_list)

        # print(len(data_list)) #838

        result = []
        count = 0
        for index in range(0, len(data_list)):

            if count == 5:
                return result
            else:
                for keyword in keyword_list:
                    if keyword in data_list[index].get('codename'):
                        pprint(data_list[index])
                        result.append(data_list[index])
                        count += 1
                        break

