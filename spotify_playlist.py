import requests

url = "https://api.spotify.com/v1/playlists/5s6auDOrQOmDZ1Uxdi27g6/tracks"
headers = {
    "Authorization": "Bearer "
}
res = requests.get(url, headers=headers)
items = res.json()['items']
while res.json()['next']:
    url = res.json()['next']
    res = requests.get(url, headers=headers)
    items += res.json()['items']
print(len(items))
artists = {}
for item in items:
    for artist in item['track'].get('artists', []):
        name = artist['name']
        artists[name] = artists.get(name, 0 ) + 1


artists = [(k,v) for k,v in sorted(artists.items(), key=lambda x: x[1])]

total_artists = len(artists)
ten_percent = total_artists * .10
top_10percent = artists[::-1][0:int(ten_percent) + 1]

for artist, count in top_10percent:
    print(f"{artist}: {count}")


