import requests
import json

with open(".env.json", "r") as jfile:
    token = json.load(jfile).get("SPOTIFY_TOKEN", None)

if token is None:
    print("YOU NEED TO PROVIDE A TOKEN IN THE .ENV FILE")
    exit(1)

url = "https://api.spotify.com/v1/playlists/5s6auDOrQOmDZ1Uxdi27g6/tracks"

headers = {
    "Authorization": f"Bearer {token}"
}
res = requests.get(url, headers=headers)
items = res.json()['items']
while res.json()['next']:
    url = res.json()['next']
    res = requests.get(url, headers=headers)
    items += res.json()['items']
print(len(items))
def ten_percent(items):
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


    return top_10percent()

def duped_songs(items):
    songs = {}
    for item in items:
        song_name = f"{item['track']['name']} by {item['track']['artists'][0]['name']}"
        songs[song_name] = songs.get(song_name, 0) + 1

    for song, count in songs.items():
        if count > 1:
            print(f"{song} shows up {count} times")

duped_songs(items)
