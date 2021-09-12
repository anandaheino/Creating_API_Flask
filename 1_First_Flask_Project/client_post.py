import requests

# USING THE METHOD POST FROM REQUESTS TO RECEIVE INFORMATIONS:
#data = {'username':'Ananda', 'secret':'@admin1', 'info': 'pay', 'value': 4000}
#response = requests.post("http://127.0.0.1:5000/informations", data=data)

# REGISTER NEW EMPLOYEES:
data = {'username':'Ananda', 'secret':'@admin1', 'name': 'Ananda', 'position': 'DataScientist', 'pay': 5000}
response = requests.post("http://127.0.0.1:5000/register", data=data)

# Analysing the status code:
if response.status_code == 200:
    print(response.json())
else:
    print("Sorry, something wen't wrong. Status code:",(response.status_code))