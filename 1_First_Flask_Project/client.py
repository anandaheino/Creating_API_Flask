import requests

#### USING GET FROM REQUESTS:
# adding the new get method with database connection
response = requests.get('http://127.0.0.1:5000/employees')

#print(response)
# This response is: <[200]> which tells us that the request worked

#print(response.text)
# Now we have the resposnse text, with the name, pay and position of the analists

#print(type(response.text))
# the output is <class 'str'>

# we have a str that is equal to json, so we can return a .json instead:

# print(type(response.json()))   # <class 'dict'>

if response.status_code == 200:
    print(response.json())
else:
    print("Sorry, something wen't wrong. Status code:",(response.status_code))