import whisper
import yt_dlp
import os

vedio_path = '../video'
ydl_opts = {
    'format': 'best',
    'outtmpl': vedio_path
}

def download_video(video_url):
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

def transcribe_video(video_file):
    model = whisper.load_model("turbo")
    result = model.transcribe(video_file)

    transcription = result["text"]
    return (transcription)


# Main function
def download_transcribe_and_summarize(link):

    download_video(link)
    video_file = vedio_path

    if os.path.exists(video_file):
        transcription = transcribe_video(video_file)

    else:
        print("Video was not downloded")

    return (transcription, vedio_path)


# Start the process
if __name__ == "__main__":
    download_transcribe_and_summarize()
