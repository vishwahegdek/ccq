import whisper
import os


def format_timestamp(seconds):
    """Format the timestamp from seconds to a string representation in seconds."""
    return str(int(seconds))

def transcribe_with_timestamps(video_path):
    '''

    :param video_path:
    :return: ill give you the transcript with time stamps in seconds
    '''
    model = whisper.load_model("turbo")
    result = model.transcribe(video_path)
    transcript_with_timestamps = []

    for segment in result['segments']:
        start_time = format_timestamp(segment['start'])
        end_time = format_timestamp(segment['end'])
        sentence = segment['text'].strip()

        transcript_with_timestamps.append(f"{start_time} - {end_time}: {sentence}")

    return transcript_with_timestamps

if __name__ == "__main__":
    video_path = "vedio/full.mp4.webm"  # Replace with your video path
    if not os.path.exists(video_path):
        print(f"Video file '{video_path}' does not exist.")
    else:
        # Get the transcript with timestamps
        transcript = transcribe_with_timestamps(video_path)

        for line in transcript:
            print(line)
