import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def get_data(artysta):
    spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())        # authorization for spotify api
    request = spotify.search(q=artysta, limit=1, offset=0, type='artist', market=None)      # request to find an artist
    id = 'spotify:artist:'+request['artists']['items'][0]['id']                             # fetch ID from request and add right header
    request = spotify.artist_albums(id, album_type='album')                                 # request to find artist albums
    albums = request['items']                                                               # save items from request to list albums

    while request['next']:                                                                  # add next pages from request to list
        request = spotify.next(request)
        albums.extend(request['items'])

    album_names = []
    for album in albums:                                                                    # save only names of albums in list
        album_names.append(album['name'])

    return album_names