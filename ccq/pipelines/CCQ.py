from .summery import *
from .timestamp import TimeStamp
from .vedio_croper import *
from .transcript_generator import *
from .downlode_n_transcript import *
from . import chatbot


def main_summarizer(link = "https://www.youtube.com/watch?v=Po4FCqAwIKU"):
    # to get the transcripts and location of the vedio
    print("transcribing vedio")
    trans, vedio_loc = download_transcribe_and_summarize(link)

    # to get the trans with time stamp
    print("time transcribing vedio")
    trans_w_time = transcribe_with_timestamps(vedio_loc)

    #to get the Summery of the transcript
    Summery = Summary()
    trans_summery = Summery.get_summary(trans)
    print(f"the SUmmery is  \n          {trans_summery}")


    # to get the time stamps from transcript
    TimeStamps = TimeStamp()
    print("generating time stamps")
    time_stamps = TimeStamps.get_ai_timestamps(trans_w_time)
    print(f"time stamps are like this is this ok ??\n {time_stamps}")
    print(f"and the ttpe is ?\n {type(time_stamps)}")


    #to crop the vedio
    destination = "./videos"
    print("On to Cropping")
    vedioCropper = vedio_croper(vedio_loc, destination)
    vedioCropper.get_vedio(timestamps=time_stamps)
    return (destination, trans_summery)

# destination, summ = main_summarizer()
#for the ChatBot
# ChatBot = chatbot.ChatBot()
# ChatBot.run_bot(summ)