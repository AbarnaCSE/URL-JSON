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
    
    def getnewyorkbreweries(self):
        result = []
        for item in self.fetch_data():
            result.append(item['brewery_type'])
        return result
    
    def getmainebreweries(self):
        result = []
        for item in self.fetch_data():
            result.append(item['brewery_type'])
        return result

url = 'https://api.openbrewerydb.org/v1/breweries?by_state=new_york&per_page=3'
obj = LatLong(url)
print(obj.getnewyorkbreweries())
breweries1 = len(obj.getnewyorkbreweries())
print(breweries1)

url = 'https://api.openbrewerydb.org/v1/breweries/search?query=dog&per_page=3'
obj = LatLong(url)
print(obj.getmainebreweries())
breweries2 = len(obj.getmainebreweries())
print(breweries2)

Totalbreweriescount = breweries1+breweries2
print("Total breweries count:",Totalbreweriescount)