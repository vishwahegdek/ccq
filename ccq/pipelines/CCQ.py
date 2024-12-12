from .summery import *
from .timestamp import TimeStamp
from .vedio_croper import *
from .transcript_generator import *
from .downlode_n_transcript import *
from .chatbot import ChatBot
# import chatbot_llama
import time

def summerize(link = "https://www.youtube.com/watch?v=Po4FCqAwIKU"):
    vedio_path = 'media/full.mp4.webm'

    # to get the transcripts and location of the vedio
    # print("starting transcribing vedio")
    # trans, vedio_loc = download_transcribe_and_summarize(link)
    # print("vedio transcribed")
    # print(f"the transcibed vedio is {trans}")
    # to get the trans with time stamp
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': vedio_path
    }
    print("started with the vedio downloding !!")
    start= time.time()
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])
    end = time.time()
    print("vedio downloded !!")
    print(f"the time taken is {end - start}")


    print("started time transcribing vedio")
    start = time.time()
    trans_w_time = transcribe_with_timestamps(vedio_path)
    print("the transcribe with time stamp is done \n \n ")
    print(f"so the trans with time is {trans_w_time}")
    end = time.time()
    print(f"the time taken for the complete time trans is {end - start}")
    trans = " ".join(item.split(":", 1)[-1].strip() for item in trans_w_time)
    # print("the trans is ", trans )


    #to get the Summery of the transcript
    start = time.time()
    Summery = Summary()

    trans_summery = Summery.get_summary(trans)
    end = time.time()
    print (f"the time taken for generating the summery is {end - start}")
    # print(f"the SUmmery is  \n          {trans_summery}")
    return (trans_summery, trans_w_time)

def vedio(time_summary):
    # to get the time stamps from transcript
    TimeStamps = TimeStamp()
    vedio_path = "./media/full.mp4.webm"

    print("generating time stamps")
    time_stamps = TimeStamps.get_ai_timestamps(time_summary)
    # print(f"time stamps are like this is this ok ??\n {time_stamps}")


    #to crop the vedio
    destination = "./media/cropped.mp4"
    print("staring to Cropping")
    start = time.time()
    vedioCropper = vedio_croper(vedio_path, destination)
    vedioCropper.get_vedio(timestamps=time_stamps)
    end = time.time()
    print(f'the time taken for cropping the complete vedio is {end - start}')
    return destination


# summary, time_summary  = summerize()
# location = vedio(time_summary)
# #for the ChatBot
# vedio_path = "./media/full.mp4.webm"
# start= time.time()
# ChatBot = ChatBot()
# ChatBot.run_bot(summary)
# end = time.time()
# print(f'the time taken for chatbot to run is {end - start}')

# chat_ll = chatbot_llama.ChatBot_LLama()
# chat_ll.run_bot(summary)