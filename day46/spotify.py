import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json

def do_spotify(SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET, song_names, date):
    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            scope="playlist-modify-private",
            redirect_uri="https://example.com",
            client_id=SPOTIFY_CLIENT_ID,
            client_secret=SPOTIFY_CLIENT_SECRET,
            show_dialog=True,
            cache_path=".cache"
        )
    )

    # get user ID
    user_id = sp.current_user()["id"]
    print(user_id)

    # generate list of song URIs using the song list you got from the billboard 100
    uri_list = []
    print('\nputting uri list together...\n\n')
    for song in song_names:
        search_results = sp.search(q=f"track:{song} year:{date[:4]}")
        track_results = search_results['tracks']['items'][:1]
        if len(track_results) >= 1:
            # print(f"{track_results[0]['name']} - {track_results[0]['uri']}")
            uri_list.append(track_results[0]['uri'])
        else:
            with open('misc.txt', mode='a') as f:
                f.write(f"No search results for {song}...")


        # USING A TXT FILE TO HELP SEE SEARCH RESULTS CLEARLY
        # with open('misc.txt', mode='a') as f:
            # f.write(json.dumps(search_results, indent=2))
            # for item in search_results['tracks']['items']:
            #     artist_list = [artist['name'] for artist in item['artists']]
            #     artist_output = ', '.join(artist_list)
            #     f.write(f"{item['name']} by {artist_output}\n")
            #     f.write(f"{item['name']} - {item['uri']}\n")


            # f.write(f"{test}")
            # uri_list.append(search_results['tracks']['items'][:1]['uri'])

    print('  ')
    print(uri_list)


    # create spotify playlist 
    playlist = sp.user_playlist_create(
        user=user_id,
        name=f"{date} Billboard 100",
        public=False,
        description=f"Playlist created programmatically for the Billboard Top 100 songs from {date}"
    )
    print("\n\nplaylist:\n\n")
    print(playlist)


    # add tracks to the playlist
    result = sp.playlist_add_items(
        playlist_id=playlist['id'],
        items=uri_list
    )
    print("\n\nresult:\n")
    print(result)


