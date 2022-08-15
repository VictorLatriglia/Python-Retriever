import json
from types import SimpleNamespace
  
# Opening JSON file
f = open('hurricanes.json')
jsonData = f.read()
# Closing file
f.close()

x = json.loads(jsonData, object_hook=lambda d: SimpleNamespace(**d))
print(x.May)
