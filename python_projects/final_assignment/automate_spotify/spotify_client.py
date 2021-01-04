import requests
import urllib.parse


class SpotifyClient(object):
    def __init__(self):
        self.api_token ='BQD4zF3KaLDkhWKqggljKOEk1t-kC3wwRp9_abyMZSRYG3cDxQpUyR3B4HGEiwopi6FkfykopccYRlVv37vwu8zdGAMqeWNq87Bt1tD_VEAWeY4a0ZldWlRQ0-z_7917whdXCwfZA_e37wl60QXgSFybz36m2tSf6qnSfsImiozupxM9u81fz_E501LevRo'


    def search_song(self, artist, track):
        query = urllib.parse.quote(f'{artist} {track}')
        url = f"https://api.spotify.com/v1/search?q={query}&type=track"
        response = requests.get(
            url,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.api_token}"
            }
        )
        response_json = response.json()

        results = response_json['tracks']['items']
        if results:
            # let's assume the first track in the list is the song we want
            return results[0]['id']
        else:
            raise Exception(f"No song found for {artist} = {track}")

    def add_song_to_spotify(self, song_id):
        url = "https://api.spotify.com/v1/me/tracks"
        response = requests.put(
            url,
            json={
                "ids": [song_id]
            },
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.api_token}"
            }
        )

        return response.ok