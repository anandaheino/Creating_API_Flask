import requests

# USING THE METHOD POST FROM REQUESTS:
data = {'username':'Math', 'secret':'@admin2', 'info': 'pay', 'value': 4000}
response = requests.post("http://127.0.0.1:5000/informations", data=data)

# Analysing the status code:
if response.status_code == 200:
    print(response.json())
else:
    print("Sorry, something wen't wrong. Status code:",(response.status_code))