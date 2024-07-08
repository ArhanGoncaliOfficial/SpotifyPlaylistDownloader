import os
import logging
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import yt_dlp
from config import ConfigReader
from colorama import init as colorama_init
from colorama import Fore

class SpotifyPlaylistDownloader:
    """
    A class to download songs from a Spotify playlist using YouTube as the source.

    This class utilizes the Spotify Web API to fetch song details from a specified
    playlist and downloads the songs from YouTube using yt-dlp.

    Attributes:
    client_id (str): Spotify API client ID.
    client_secret (str): Spotify API client secret.
    sp (spotipy.Spotify): Spotify API client for accessing Spotify data.

    Methods:
    getSongNames(playlist_url: str) -> dict:
        Fetches song names and artist details from a Spotify playlist.

    downloadSongs(songDataDict: dict, file_type: str, output_path: str):
        Downloads songs from YouTube based on the song data dictionary.

    check_missing_songs(songDataDict: dict, output_path: str, file_type: str):
        Checks for missing songs in the specified output directory and logs them.

    `Made by Arhan Goncalı` | 07/06/2024
    """

    def __init__(self, client_id: str, client_secret: str) -> None:
        self.client_id = client_id
        self.client_secret = client_secret
        credentials = SpotifyClientCredentials(client_id=self.client_id, client_secret=self.client_secret)
        self.sp = spotipy.Spotify(client_credentials_manager=credentials)
        colorama_init()

    def getSongNames(self, playlist_url: str) -> dict:
        results = self.sp.playlist_tracks(playlist_url)
        songDataDict = {}

        for item in results['items']:
            try:
                track = item['track']
                artist = track['artists'][0]['name']
                track_name = track['name']
            except (KeyError, IndexError):
                logging.error(f"{Fore.RED}Error: Missing data for {item}. Skipping this item{Fore.RESET}")
                continue

            search_query = f"{artist} - {track_name}"

            songDataDict[search_query] = {
                "artist": artist,
                "track_name": track_name
            }

        return songDataDict

    def downloadSongs(self, songDataDict: dict, file_type: str, output_path: str):
        
        queueIndex = 1
        total_songs = len(songDataDict.keys())
        
        for search_query, song_data in songDataDict.items():
            track_name = song_data['track_name']
            ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': f'{file_type}',
                    'preferredquality': '192',
                }],
                'outtmpl': f'{output_path}/{track_name}.%(ext)s',
                'ffmpeg_location': 'C:/ffmpeg/bin',
                'http_headers': {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
                }
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                try:
                    print(f"{Fore.MAGENTA}{queueIndex}/{total_songs} | {track_name} | Trying to download the song.{Fore.RESET}")
                    result = ydl.download([f"ytsearch1:{search_query}"])
                    if result == 0:
                        print(f"{Fore.GREEN}{track_name} downloaded successfully!{Fore.RESET}\n")
                        logging.info(f"{track_name} downloaded successfully.")
                    else:
                        raise Exception("Download failed with non-zero exit code.")
                except Exception as e:
                    logging.error(f"{Fore.RED}Error downloading {track_name}: {e}{Fore.RESET}")
                finally:
                    queueIndex += 1
                    os.system('cls')

    def checkMissingSongs(self, songDataDict: dict, output_path: str, file_type: str):
        output_path = output_path.strip('\"')
        downloaded_files = set(os.listdir(output_path))
        missing_songs = []

        for search_query, song_data in songDataDict.items():
            track_name = song_data['track_name']
            if f"{track_name}.{file_type}" not in downloaded_files:
                missing_songs.append(search_query)

        if missing_songs:
            with open(f"{output_path}/missing_songs.txt", "w", encoding="utf-8") as f:
                for song in missing_songs:
                    f.write(f"{song}\n")
            logging.info(f"Missing songs logged in {output_path}/missing_songs.txt")
        else:
            print(f"{Fore.GREEN}You have downloaded all the songs successfully!{Fore.RESET}")

if __name__ == "__main__":
    os.system('cls')
    logging.basicConfig(filename='AppInfo.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', encoding="UTF-8")

    config = ConfigReader(config_path="config/application.cfg")

    spotify_credentials = config.getSpotifyCredentials()
    client_id = spotify_credentials["client_id"]
    client_secret = spotify_credentials["client_secret"]

    application_settings = config.getApplicationSettings()
    output_path = application_settings["output_path"].strip('\"')
    output_file_type = application_settings["output_file_type"]

    playlist_url = "SPOTIFY_PLAYLIST_URL" # Put your Spotify playlist URL that you want to download.

    downloader = SpotifyPlaylistDownloader(client_id, client_secret)
    songs = downloader.getSongNames(playlist_url)
    downloader.downloadSongs(songDataDict=songs, file_type=output_file_type, output_path=output_path)
    downloader.checkMissingSongs(songDataDict=songs, output_path=output_path, file_type=output_file_type)
