import json
import requests
r = requests.get('http://api.open-notify.org/astros.json')
print(json.loads(r.text))