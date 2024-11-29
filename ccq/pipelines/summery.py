from mistralai import Mistral
class Summary:
    """
    This class helps summarize text using the Mistral API.
    """
    def __init__(self, apikey = "gt8Qq1j3x1enSd7rFN3JHgRLE3COytKm", model="open-mistral-nemo"):
        self.model = model
        self.apikey = apikey
    def get_summary(self, wo_trans):
        """
        Gets a summary of the provided text using the Mistral API.

        Args:
            wo_trans (str): The text to be summarized.

        Returns:
            str: The generated summary.
        """
        try:
            client = Mistral(api_key=self.apikey)

            response = client.chat.complete(
                model=self.model,
                messages=[{"role": "user", "content": f"hey i will provide you with a trascript and you give me a detailed summery of this with keypoints"}]
            )

            response = client.chat.complete(
                model=self.model,
                messages=[{"role": "user", "content": f"{wo_trans}"}]
            )

            ans = response.choices[0].message.content
            print(ans)
            return ans
        except:
            return "api limit reached you ass"

