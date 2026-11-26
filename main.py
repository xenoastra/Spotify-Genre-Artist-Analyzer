import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
import time
import matplotlib.pyplot as plt
import os
from dotenv import load_dotenv


load_dotenv()

client_id = os.getenv("SPOTIFY_CLIENT_ID")
client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")

print("Client Secret Loaded:", client_secret is not None)
auth_manager = SpotifyClientCredentials(
    client_id=client_id,
    client_secret=client_secret
)

sp = spotipy.Spotify(auth_manager=auth_manager)
print("Spotify connection successful!")


# Example playlist_link = "https://open.spotify.com/playlist/4OFACY9bSggVZBmLrmqhNc?si=355d5e4ad6b94249" 
playlist_link = input("Enter the link of a public spotify playlist: ")
start_time = time.time()
try:
    playlist_URI = playlist_link.split("/")[-1].split("?")[0]
    playlist_data = sp.playlist(playlist_URI)
except:
    print("Invalid URL, The link provided may be invalid or private")
    exit()

# print(f"\nReading Playlist data for Playlist: {playlist_data['name']} (" + playlist_link+")")
artistlist = []
genrelist = []
artistcount = {}
genrecount = {}
count = 0
artist_cache = {}

#get the items from playlist_data list of dict - artist name, song name e.t.c
for item in playlist_data['tracks']['items']:
    song = item['track']['name']
    artistname = item['track']['artists'][0]['name']
    artistid = item['track']['artists'][0]['id']
    artistlist.append(artistname)

    #save the artist name to the cache, this prevents issues with bigger playlists
    if artistid not in artist_cache:
        artist_cache[artistid] = sp.artist(artistid)
    genres = artist_cache[artistid]['genres']

    genrelist.append(genres)
    # print(song, genres)
    # print (artistlist)
    artists = item['track']['artists']

    #For songs with multiple artists, split the weight of each artist's %
    if artists:
        weight1 = 1 / len(artists)
        for artist in artists:
            artist_name = artist['name']
            if artist_name not in artistcount: #don't duplicate the artist weight so it doesn't exceed 100
                artistcount[artist_name] = 0
            artistcount[artist_name] += weight1

    #For songs with multiple artists, split the weight of each artist's %
    if genres:
        weight = 1 / len(genres)
    for genre in genres:
        if genre not in genrecount:
            genrecount[genre] = 0
        genrecount[genre] += weight  

    # for genre in genres:
    #     if genre in genrecount:
    #         genrecount[genre] += 1
    #     else:
    #         genrecount[genre] = 1

#total songs
total = len(artistlist)   
tot = len(genrelist)

#order artists and genres dict
orderedartist = dict(sorted(artist_cache.items()))
orderedgenre = dict(sorted(genrecount.items()))

#print titles
print (playlist_data['name'], "'s playlist breakdown: ")
print(f"Total Number of songs: {playlist_data['tracks']['total']}\n")

#print artist break down
orderedartistbd = {}
for artist, count in artistcount.items():
    artistbd = (count / total) * 100
    orderedartistbd[artist] = artistbd 


# print genre break down
orderedgenrebd = {}  
for artist, count in genrecount.items():
    genrebd = (count / total) * 100 
    orderedgenrebd[artist] = genrebd 

#sort the list of dictionaries for artist and genre
sortedartistbd = sorted(orderedartistbd.items(), key=lambda x: x[1], reverse=True)
sortedgenrebd = sorted(orderedgenrebd.items(), key=lambda x: x[1], reverse=True)


labels = []
values = []
for genre, genrebd in sortedgenrebd:
    labels.append(genre)
    values.append(genrebd)
    
#pie chart plotting stuff
plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)# 
plt.title(f"Genre breakdown for {playlist_data['name']}")
#plt.legend(genrebd,genre)

#displaying artist breakdown
print("Artist breakdown: ")
for artist, artistbd in sortedartistbd:
    print(f"{artist}: {artistbd:.2f}% ")

#displaying genre breakdown
print("-----------------------------------------------------------------------")
print("Genre breakdown: ")
for genre, genrebd in sortedgenrebd:
    print(f"{genre}: {genrebd:.2f}% ")
end_time = time.time()
print(f"\nScript finished in {end_time - start_time:.2f} seconds")
print("\nNote: Song's with multiple artists' and genres have thier percents split")
plt.show()
#print(json.dumps(playlist_data, indent=4))


#playlist break down, artist break down in a chart, get count of artists
#for now take a count of artist name and make a % for the break down
# Eventually add error handlign for private ones
# Add a mood like for example "your taste is emo"
# In the pie chart make the genres genralized if they are too specific e.g rock, metal, pop, rap etc...
