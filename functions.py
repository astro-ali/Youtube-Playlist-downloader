import googleapiclient.discovery
from urllib.parse import parse_qs, urlparse
import pafy

def fetch_playlist_urls(playlist_url):
	API_KEY = "AIzaSyBsvjNJOSlBxRg9HYwDcslAi49B-BrXaPQ"
	query = parse_qs(urlparse(playlist_url).query, keep_blank_values=True)
	playlist_id = query["list"][0]
	youtube = googleapiclient.discovery.build("youtube", "v3", developerKey = API_KEY)
	request = youtube.playlistItems().list(
	part = "snippet",
	playlistId = playlist_id,
	maxResults = 50)
	response = request.execute()
	playlist_items = []
	while request is not None:
		response = request.execute()
		playlist_items += response["items"]
		request = youtube.playlistItems().list_next(request, response)
	video_links = [
	f'https://www.youtube.com/watch?v={t["snippet"]["resourceId"]["videoId"]}'
	for t in playlist_items]
	titles = []
	for i in playlist_items:
		title = i["snippet"]["title"]
		titles.append(title)
	return [video_links, titles]


def fetchIDs(playlist_url):
	playlist = pafy.get_playlist(playlist_url)
	video_IDs = [playlist['items'][v]['pafy'].videoid 
	for v in range(len(playlist['items']))]
	titles = [playlist['items'][v]['pafy'].title 
	for v in range(len(playlist['items']))]
	video_links = [f"https://www.youtube.com/watch?v={video_id}" 
	for video_id in video_IDs]
	return [video_links, titles]