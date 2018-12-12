import requests
import json
data="outputpins"
for i in range(20):
    r = requests.post('http://localhost:8765/outputpins',str(i))
    print(r.text)
    status_json = r.json
    y=json.loads(r.text)
    print(y)
    for i in range(30):
        try:
            print(str(i)+" "+y[str(i)])
        except KeyError:
            pass
#for i in status_json:
#    print(i)
