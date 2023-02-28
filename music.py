import requests

apikey= "11ba2baedecba73d61d2d6563c2f1c3a"
limit = 5

def relevant_data(track, response):
    data = [dict() for i in range(limit)]
    for i in range(limit):
        responses = response[track]["track"][0]
        data[i]['name'] = responses['name']
        data[i]['artiste'] = responses['artist']['name']
        data[i]['url'] = responses['url']
    return data

def top5songs(emotion):
    api_url = "http://ws.audioscrobbler.com/2.0/?method=tag.gettoptracks&tag={}&limit={}&api_key={}&format=json".format(emotion, limit, apikey)
    response = requests.get(api_url)
    if response.status_code == 200:
        response.json()
        songs = relevant_data("tracks", response)
        return songs
        
                
def similar_songs(name,artist):
    api_url = "http://ws.audioscrobbler.com/2.0/?method=track.getsimilar&artist={}&track={}&limit={}&api_key={}&format=json".format(artist, name, limit, apikey)
    response = requests.get(api_url)
    if response.status_code == 200:
        response.json()
        songs = relevant_data("similartracks", response)
        return songs
