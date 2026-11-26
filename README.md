# Spotify-Genre-Artist-Analyzer
Analyzes Spotify playlist data using Python and the Spotify API to identify music preference patterns and artist/genre trends.

## Demo
The Playlist I will use for this Demo : [https://open.spotify.com/playlist/4OFACY9bSggVZBmLrmqhNc?si=355d5e4ad6b94249](https://open.spotify.com/playlist/4np0XQMgPabO0bObdxsyWG?si=21b7a686af904ca2)

<img width="1088" height="97" alt="image" src="https://github.com/user-attachments/assets/0238bedd-875d-41f5-9e1d-6d0e19a858b9" />

Here you will Enter a link to a playlist, The playlist MUST be a Public Spotify Playlist

The Playlist As it is on Spotify:
<img width="1014" height="585" alt="image" src="https://github.com/user-attachments/assets/1d83e1a0-878d-4066-8294-938da571b79a" />

Output:

<img width="752" height="434" alt="image" src="https://github.com/user-attachments/assets/c1e8bcba-0dde-47f9-93b5-3146de052fef" />

This Playlist Contains 2 songs with multiple genres. One song has one artist and the other song has three artists. The weight of the three artists are split evenly.
There is also a Pie Chart with The Artist Breakdown attached

<img width="570" height="437" alt="image" src="https://github.com/user-attachments/assets/e227c26f-e889-438f-9e9b-84103a1bc28e" />

# Features
Spotify API integration
Artist distribution analysis
Genre distribution analysis
Weighted artist percentages for collaborations
Weighted genre percentages for multi-genre artists
Automatic playlist breakdown reporting
Pie chart visualizations using Matplotlib

## Tech Stack
Python and spotipy API

## Setup

Request a Spotify Client secret:
```
https://developer.spotify.com/documentation/web-api/concepts/apps
```
Create a `.env` file in the project root, replace the client ID and client secret with your own:

```env
SPOTIFY_CLIENT_ID=your_client_id
SPOTIFY_CLIENT_SECRET=your_client_secret
```

Install dependencies:

```bash
pip install python-dotenv
```

## Future Improvements and Features
- Playlist Analysis: Add a breakdown of listening habits by playlist, including the number of artists featured in each playlist.
- Artist Distribution: Calculate the number of unique artists listened to and visualize artist representation as percentages.
- Improved Error Handling: Add error handling for private or inaccessible Spotify data.
- Music Taste Personality: Generate a descriptive summary of listening preferences based on genre distribution (e.g., "Your music taste is emo").
= Genre Categorization: Group specific genres into broader categories (e.g., Rock, Metal, Pop, Rap) to make genre distribution charts easier to interpret.

