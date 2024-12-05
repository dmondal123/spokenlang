from googleapiclient.discovery import build
import json

# Replace with your YouTube API key
API_KEY = ''

# Create the YouTube API client
service = build('youtube', 'v3', developerKey=API_KEY)

# Input and output files
input_file = 'assamese.txt'
output_file = 'assamese_videos.json'

# Read video IDs from the input file
with open(input_file, 'r') as file:
    video_ids = [line.strip() for line in file]

# Collect data for each video
video_data = []
for video_id in video_ids:
    try:
        # Make a request to get video details
        request = service.videos().list(part='snippet', id=video_id)
        response = request.execute()

        if 'items' in response and len(response['items']) > 0:
            item = response['items'][0]
            snippet = item['snippet']
            video_data.append({
                "video_id": video_id,
                "video_title": snippet["title"],
                "video_description": snippet["description"],
                "video_language": "assamese"
            })
        else:
            print(f"No data found for video ID: {video_id}")
    except Exception as e:
        print(f"Error fetching data for video ID {video_id}: {e}")

# Save the collected data to a JSON file
with open(output_file, 'w', encoding='utf-8') as file:
    json.dump(video_data, file, ensure_ascii=False, indent=4)

print(f"Video data saved to '{output_file}'.")

