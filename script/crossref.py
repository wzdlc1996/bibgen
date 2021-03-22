import requests
import json

testdoi = "10.1109/5.771073"
crossrefapi = "https://api.crossref.org/v1/works/{}"

metadata = requests.get(crossrefapi.format(testdoi))
metad = json.loads(metadata.content)
print(metad.keys())
print(metad)
with open("./res.json", "w") as f:
    json.dump(metad, f)
