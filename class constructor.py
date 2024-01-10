import requests

class LatLong:

    def __init__(self, url):
        self.url = url
        self.response = requests.get(url)
    
    def server_status(self):
        return self.response.status_code

    def fetch_data(self):
        try:
            if self.server_status() == 200:
                return self.response.json()
            else:
                print(self.server_status())
        except:
            print("Error")
    
    def getName(self):
        result = []
        for item in self.fetch_data():
            result.append(item['name'])
        return result

    def getLat(self):
        result = []
        for item in self.fetch_data():
            result.append(item['address']['geo']['lat'])
        return result

    def getLong(self):
        result = []
        for item in self.fetch_data():
            result.append(item['address']['geo']['lng'])
        return result


url = 'https://restcountries.com/v3.1/all'
obj = LatLong(url)
print(obj.getName())