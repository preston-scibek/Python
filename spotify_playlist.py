import requests
import json
import random
import datetime

def ten_percent(items : list):
    """Print out the top 10% of artists in a playlist

    Args:
        items (list) : list of songs from the playlist api
    """
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

def duped_songs(items : list):
    """Print out the list of duplicate songs in a playlist

    Args:
        items (list) : list of songs from the playlist api
    """
    songs = {}
    for item in items:
        song_name = f"{item['track']['name']} by {item['track']['artists'][0]['name']}"
        songs[song_name] = songs.get(song_name, 0) + 1

    for song, count in songs.items():
        if count > 1:
            print(f"{song} shows up {count} times")


def get_playlist_items(headers : dict, playlist_id : str) -> list:
    """Get the items in a playlist
    
    Args:
        headers: dictionary containing api request headers
    Returns:
        list : the items in the playlist
    """

    url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
    headers
    res = requests.get(url, headers=headers)
    if res.status_code != 200:
        print(res)
    items = res.json()['items']
    while res.json()['next']:
        url = res.json()['next']
        res = requests.get(url, headers=headers)
        items += res.json()['items']
    return items

def get_user_info(headers):
    """Get the authenticated users info
    
    Args:
        headers: dictionary containing api request headers
    """
    user_info_url = 'https://api.spotify.com/v1/me'
    return requests.get(user_info_url, headers=headers).json()
    
def auth() -> dict:
    """authenticate and receive a bear token
    
    Returns:
        Header dictionary pre-filled with authorization header
    """
    import base64
    import requests
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import parse_qs, urlparse

    with open(".env.json", "r") as jfile:
        _f = json.load(jfile)
        CLIENT_ID = _f['SPOTIFY']["CLIENT_ID"]
        CLIENT_SECRET = _f['SPOTIFY']["CLIENT_SECRET"]
    port = 8988
    REDIRECT_URI = f'http://localhost:{port}/callback'

    SCOPES = [
        'playlist-read-private',
        'playlist-read-collaborative',
        'playlist-modify-private',
        'playlist-modify-public',
        'user-library-read',
    ]
    SCOPE = ",".join(SCOPES)

    auth_url = f'https://accounts.spotify.com/authorize?' \
            f'client_id={CLIENT_ID}&response_type=code&redirect_uri={REDIRECT_URI}&scope={SCOPE}'

    # todo: can we forcibilly open browser tab?
    print(f'Please visit this URL to authorize your application: {auth_url}')
    auth_headers = ""
    # Start a simple HTTP server to handle the callback
    class CallbackHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            # set auth_headers to parent scope so that way we can return the value and use it in other functions
            nonlocal auth_headers
            query = parse_qs(urlparse(self.path).query)
            if 'code' in query:
                auth_code = query['code'][0]
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b'<html><body><p>Authorization successful! You can close this window.</p></body></html>')

                # conver auth code to token
                token_url = 'https://accounts.spotify.com/api/token'
                auth_header = base64.b64encode(f'{CLIENT_ID}:{CLIENT_SECRET}'.encode()).decode('utf-8')
                headers = {'Authorization': f'Basic {auth_header}'}
                data = {
                    'grant_type': 'authorization_code',
                    'code': auth_code,
                    'redirect_uri': REDIRECT_URI,
                }

                response = requests.post(token_url, headers=headers, data=data)
                token_info = response.json()

                # verify the access token exists and works
                if 'access_token' in token_info:
                    access_token = token_info['access_token']
                    user_info = get_user_info({'Authorization': f'Bearer {access_token}'})
                    assert "display_name" in user_info
                    display_name = user_info.get('display_name', 'Unknown')
                    print(f'Authenticated as {display_name}')
                    # set auth_headers to parent scope so that way we can return the value and use it in other functions
                    auth_headers = {'Authorization': f'Bearer {access_token}'}
                else:
                    print('Authentication failed.')
            else:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(b'<html><body><p>Authorization code not found in the callback URL.</p></body></html>')

    server = HTTPServer(('localhost', port), CallbackHandler)
    print('Waiting for authorization...')
    server.handle_request()
    return auth_headers


def randomize_and_create_new_playlist(items : list, headers : dict):
    """Randomize a playlist and create a new one
    
    Args:
        items (list) : the items in the playlist
        headers: dictionary containing api request headers
    Returns:
        list : the items in the playlist
    """
    randomized_list = items
    random.shuffle(randomized_list)
    user_info = get_user_info(headers)
    assert user_info["id"]
    res = requests.get(f"https://api.spotify.com/v1/users/me/playlists/", headers=headers)
    total_playlists = res.json()['total']
    # create new playlist
    post_headers = {"Content-Type": "application/json"}
    post_headers.update(headers)
    import json
    res = requests.post(f"https://api.spotify.com/v1/users/{user_info['id']}/playlists/", headers=post_headers, data=json.dumps({"name": f" Shuffle {total_playlists + 1}", "description": f"randomized shuffle :  {datetime.datetime.now().isoformat()}", "public": False}))
    new_playlist = res.json()
    if res.status_code != 201:
        print(new_playlist)
        exit(1)
    # add songs
    for index in range(0,len(randomized_list), 100):
        if index+100 >= len(randomized_list):
            splice = randomized_list[index::]
        else:
            splice = randomized_list[index:index+100]
        res = requests.post(f"https://api.spotify.com/v1/playlists/{new_playlist['id']}/tracks", headers=post_headers, data=json.dumps({"uris": [song['track']['uri'] for song in splice]}))


headers = auth()
items = get_playlist_items(headers, "5s6auDOrQOmDZ1Uxdi27g6")
print(len(items))
#ten_percent(items)
#duped_songs(items)
randomize_and_create_new_playlist(items, headers)
