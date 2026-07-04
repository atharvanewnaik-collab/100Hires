from youtube_transcript_api import YouTubeTranscriptApi

# Example YouTube Video ID
video_id = "nP7OJg7vQOg"

try:
    transcript = YouTubeTranscriptApi.get_transcript(video_id)

    print("Transcript fetched successfully!\n")

    for line in transcript[:10]:
        print(line["text"])

except Exception as e:
    print("Error:", e)