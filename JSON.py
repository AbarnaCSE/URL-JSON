import requests
response = requests.get('https://restcountries.com/v3.1/all')
data = response.json()
print(data)
