from mistralai import Mistral
import ast

class TimeStamp:
    def __init__(self, apikey="gt8Qq1j3x1enSd7rFN3JHgRLE3COytKm", model="mistral-large-latest"):
        self.model = model
        self.apikey = apikey

    def get_ai_timestamps(self, w_trans):
        """
        Gets a video as output of the provided text with timestamp the Mistral API.

        Args:
            w_trans (str): The text with time stamp

        Returns:
            return a list of tuples with start and end times
        """
        client = Mistral(api_key=self.apikey)

        response = client.chat.complete(
            model=self.model,
            messages=[{"role": "user", "content": f"{w_trans}     Given the following transcript of a video with timestamps, give remove the time where there is not important aspects of the concept is present in seconds The exact format should be: [(start time 1 ins seconds, end time 1seconds), (start time 2 , end time 2), ...] only give me this list ng else as output"}]
        )

        # response = client.chat.complete(
        #     model=self.model,
        #     messages=[{"role": "user",
        #                "content": f"{w_trans}     Given the following transcript of a video with timestamps, give me only the timestamps where the important parts of the video and present: [(start time 1 ins seconds, end time 1seconds), (start time 2 , end time 2), ...] only give me this list ng else as output"}]
        # )
        return ast.literal_eval(response.choices[0].message.content)


