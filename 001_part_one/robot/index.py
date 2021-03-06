import json
import requests

city = '杭州'  # 城市名称
province = '浙江'  # 省份名称
street = '文一西路'  # 道路
text = ''  # 想说的话

url = "http://openapi.tuling123.com/openapi/api/v2"
values = {
    "reqType": 0,
    "perception": {
        "inputText": {
            "text": text
        },
        "inputImage": {
            "url": "imageUrl"
        },
        "selfInfo": {
            "location": {
                "city": city,
                "province": province,
                "street": street
            }
        }
    },
    "userInfo": {
        "apiKey": "b017c92f5c084daab1dc79f6dba247a8",
        "userId": "youkedapy"
    }
}

response = requests.post(url, data=json.dumps(values))
response.encoding = 'utf-8'
result = response.json()
answer = result['results'][0]['values']['text']
print('我：' + text)
print('机器人：' + answer)
