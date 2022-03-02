import requests
import json

url = 'http://0.0.0.0:5000/prediction'

data = [[2,180,74,24,21,23.9091702,1.488172308,22]]
j_data = json.dumps(data)
r = requests.post(url, data=j_data)
print(r, r.text)