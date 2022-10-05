import pprint
import requests

SPOTIFY_ACCESS_TOKEN = 'BQCy-8cL4Z3PWBN0Q_z5BGBVEvokk-0_5nh8jIEzF93W4MwVxzEwvpGw0W65NDAJggBxe3SRDBMYv1nw6gcmWHTKVlblQCK0nMLZlGnqAvNstMqySRVvkCIgjyUV6Ss6EiRYtCFmNw7JZ9zPaWnB7PeNaQTVPlW_sotrRWidACunNdAt9UsbXo9VspNoHTVbWm689Q25'
SPOTIFY_GET_CURRENT_TRACK_URL = 'https://api.spotify.com/v1/me/player/currently-playing'


def get_current_track(access_token):
    response = requests.get(
        SPOTIFY_GET_CURRENT_TRACK_URL,
        headers ={
            "Authorization": f"Bearer {access_token}"
        }
    )
    resp_json = response.json()

    track_id = resp_json['item']['id']
    track_name = resp_json['item']['name']
    artists = resp_json['item']['artists']
    artists_names = ', '.join([artist['name'] for artist in artists])
    link = resp_json['item']['external_urls']['spotify']

    current_track_info = {
        "id": track_id,
        "name": track_name,
        "artists": artists_names,
        "link": link
    }

    return current_track_info


def main():
    current_track_info = get_current_track(
        SPOTIFY_ACCESS_TOKEN
    )

    pprint(current_track_info, indent = 4)


if __name__ == '__main__':
    main()