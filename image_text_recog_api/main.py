import requests
import uuid
import time
import json

api_url = 'https://s41unh2wlg.apigw.ntruss.com/custom/v1/24115/0bbc6834b755a08b0e2d23c41f7215b83cff0a10bd964c3a12808e062a974c01/general'
secret_key = 'ZERaRXhISkRBa1hxQmVqQURPclNYZ21mYkpHZUdtS20='
image_file = 'test_img' + '.png'

request_json = {
    'images': [
        {
            'format': 'jpg',
            'name': 'demo'
        }
    ],
    'requestId': str(uuid.uuid4()),
    'version': 'V2',
    'timestamp': int(round(time.time() * 1000))
}

payload = {'message': json.dumps(request_json).encode('UTF-8')}
files = [
  ('file', open(image_file,'rb'))
]
headers = {
  'X-OCR-SECRET': secret_key
}

response = requests.request("POST", api_url, headers=headers, data = payload, files = files)

print(response.text)