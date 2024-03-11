from youtube_transcript_api import YouTubeTranscriptApi

def extract_transcript(youtube_video_url):
    try:

        # for playist
        # sample url : https://www.youtube.com/watch?v=OmS94lV-X6o&list=WL&index=44
        video_id = ""
        if "&" in youtube_video_url:
            video_id = youtube_video_url.split("v=")[1].split("&")[0]
        else:
            video_id = youtube_video_url.split("=")[1]

        transcript_text = YouTubeTranscriptApi.get_transcript(video_id)
        transcript = ""
        for i in transcript_text:
            transcript += " " + i["text"]

        return transcript

    except Exception as e:
        print(f"Error extracting transcript: {e}")
        return None
