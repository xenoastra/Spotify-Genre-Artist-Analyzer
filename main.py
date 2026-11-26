import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
import os
from dotenv import load_dotenv

load_dotenv()

auth_manager = SpotifyClientCredentials(
    client_id=os.getenv("SPOTIFY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIFY_CLIENT_SECRET")
)
# playlist_link = "https://open.spotify.com/playlist/4OFACY9bSggVZBmLrmqhNc?si=355d5e4ad6b94249" 
playlist_link = input("Enter the link of a public spotify playlist: ")
playlist_URI = playlist_link.split("/")[-1].split("?")[0]
playlist_data = sp.playlist(playlist_URI)

# print(f"\nReading Playlist data for Playlist: {playlist_data['name']} (" + playlist_link+")")
artistlist = []
genrelist = []
artistcount = {}
genrecount = {}
count = 0

for item in playlist_data['tracks']['items']:
    song = item['track']['name']
    artistname = item['track']['artists'][0]['name']
    artistid = item['track']['artists'][0]['id']
    artistlist.append(artistname)
    #get genres
    artistdata = sp.artist(artistid)
    genres = artistdata['genres']
    genrelist.append(genres)
    # print(song, genres)
    # print (artistlist)
    artist_count = {}
    for artist in artistlist:
        if artist in artist_count:
            artist_count[artist] += 1
        else:
            artist_count[artist] = 1



total = len(artistlist)   
tot = len(genrelist)
orderedartist = dict(sorted(artist_count.items()))
orderedgenre = dict(sorted(genrecount.items()))

print ("\n",playlist_data['name'] , "'s playlist breakdown (not including features): ")
print(f"Total Number of songs: {playlist_data['tracks']['total']}\n")

#print artist break down
orderedartistbd = {}
for artist, count in artist_count.items():
    artistbd = (count / total) * 100
    orderedartistbd[artist] = artistbd 


#print genre break down


sortedartistbd = sorted(orderedartistbd.items(), key=lambda x: x[1], reverse=True)
for artist, artistbd in sortedartistbd:
    print(f"{artist}: {artistbd:.2f}% ")


