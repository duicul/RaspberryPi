import requests
import json
data="outputpins"
r = requests.get('http://localhost:8765/outputpins')
status_json = r.json
y=json.loads(r.text)
print(y)
for i in range(30):
    try:
        print(str(i)+" "+y[str(i)])
    except KeyError:
        pass
print(r.text)
#for i in status_json:
#    print(i)
