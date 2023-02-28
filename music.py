import requests

apikey= "11ba2baedecba73d61d2d6563c2f1c3a"

song = [dict() for i in range(5)]

def music(emotion):
    api_url = "http://ws.audioscrobbler.com/2.0/?method=tag.gettoptracks&tag={}&limit=5&api_key={}&format=json".format(emotion,apikey)
    response = requests.get(api_url)
    if response.status_code == 200:
        response.json()
        for i in response
        
        
        
#obtain each track
#in each track obtain data for (name, artist and url)
#return this data in dictionary form