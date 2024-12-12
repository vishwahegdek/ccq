import whisper
import yt_dlp
import os

vedio_path = 'media/full.mp4.webm'
ydl_opts = {
    'format': 'bestvideo+bestaudio/best',
    'outtmpl': vedio_path
}

def download_video(video_url):
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

def transcribe_video(video_file):
    model = whisper.load_model("turbo")
    print("vidio transcribing")
    result = model.transcribe(video_file)
    print("transcribed")
    transcription = result["text"]
    return (transcription)


# Main function
def download_transcribe_and_summarize(link):

    print("downloding vedio")
    download_video(link)
    video_file = vedio_path
    print("vedio downloded")
    if os.path.exists(video_file):
        transcription = transcribe_video(video_file)

    else:
        print("Video was not downloded")

    return (transcription, vedio_path)


# Start the process
if __name__ == "__main__":
    download_transcribe_and_summarize()
