from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.editor import concatenate_videoclips, vfx

class vedio_croper:
    '''
    Give me a source path of video and a destination path where I should store the video.
    '''
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

    def get_vedio(self, timestamps):
        """
        Gets a video as output based on the provided timestamps.

        Args:
            timestamps (list): list of tuples representing the start and the end of timestamps

        Returns:
            None
        """
        try:
            # Load the video
            video = VideoFileClip(self.source)
            cropped_clips = []

            # Iterate over the timestamps
            for i, (start_time, end_time) in enumerate(timestamps):
                cropped_video = video.subclip(start_time, end_time)
                cropped_clips.append(cropped_video)

            # Concatenate the cropped clips
            final_video = concatenate_videoclips(cropped_clips)

            # Write the final video to the destination
            final_video.write_videofile(self.destination, codec='libx264')
        except Exception as e:
            print(f"Error: {e}")
