import requests

# USING GET FROM REQUESTS:
response = requests.get("http://127.0.0.1:5000/employees/position/analist")

#print(response)
# This response is: <[200]> which tells us that the request worked

#print(response.text)
# Now we have the resposnse text, with the name, pay and position of the analists

#print(type(response.text))
# the output is <class 'str'>

# we have a str that is equal to json, so we can return a .json instead:
print(response.json())
print(type(response.json()))   # <class 'dict'>
