<h1>Spotify Playlist Downloader</h1>
<p>This project allows you to download songs from a Spotify playlist using YouTube as the source. It uses the Spotify Web API to fetch song details and yt-dlp to download the songs.</p>

<h2>Features</h2>
<ul>
<li>Fetch song names and artist details from a Spotify playlist.</li>
<li>Download songs from YouTube using yt-dlp.</li>
<li>Check for missing songs in the specified output directory and log them.</li>
</ul>

<h2>Prerequisites</h2>
<ul>
<li>Python 3.6 or higher</li>
<li><code>spotipy</code> library</li>
<li><code>yt-dlp</code> library</li>
<li><code>colorama</code> library</li>
<li><code>configparser</code> library</li>
<li><code>ffmpeg</code> installed and added to PATH</li>
</ul>

<h2>Installation</h2>
<ol>
<li>Clone the repository:
<pre><code>git clone https://github.com/ArhanGoncaliOfficial/SpotifyPlaylistDownloader.git
cd SpotifyPlaylistDownloader
</code></pre>
</li>
<li>Install the required libraries:
<pre><code>pip install spotipy yt-dlp colorama configparser
</code></pre>
</li>
<li>Install <code>ffmpeg</code>:
<ul>
<li>Download from <a href="https://ffmpeg.org/download.html">ffmpeg.org</a>.</li>
<li>Add the <code>ffmpeg</code> binary to your system's PATH.</li>
</ul>
</li>
</ol>

<h2>Configuration</h2>
<ol>
<li>Create a configuration file <code>application.cfg</code> in the <code>config</code> directory with the following structure:
<pre><code>[SpotifyAPICredentials]
client_id = your_spotify_client_id
client_secret = your_spotify_client_secret

[ApplicationSettings]
output_path = path_to_output_directory
output_file_type = mp3
</code></pre>
</li>
<li>Replace <code>your_spotify_client_id</code> and <code>your_spotify_client_secret</code> with your Spotify API credentials.</li>
<li>Replace <code>path_to_output_directory</code> with the path where you want to save the downloaded songs.</li>
</ol>

<h2>Usage</h2>
<ol>
<li>Update the <code>playlist_url</code> variable in <code>SpotifyPlaylistDownloader</code> with your Spotify playlist URL.</li>
<li>Run the script:
<pre><code>python spotify_playlist_downloader.py
</code></pre>
</li>
<li>The script will fetch the song names and artist details from the specified Spotify playlist, download the songs from YouTube, and check for any missing songs.</li>
</ol>

<h2>Logging</h2>
<p>The application logs its activity in the <code>AppInfo.log</code> file in the project root directory.</p>

<h2>Author</h2>
<p>Made by <b>Arhan Goncalı</b></p>
