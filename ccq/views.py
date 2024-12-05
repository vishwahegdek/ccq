from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.core.files.storage import default_storage
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import os
# from . import chatbot
from .pipelines.CCQ import main_summarizer
from .pipelines.chatbot import ChatBot
# from .pipelines import temp



# # Initialize the chatbot instance
chatbot = ChatBot(api_key="gt8Qq1j3x1enSd7rFN3JHgRLE3COytKm")

@csrf_exempt
def chatbot_api(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            summary = data.get("summary", "")
            context = data.get("context", "")
            question = data.get("question", "")
            # Get response from chatbot
            response = chatbot.get_response(summary, context, question)
            return JsonResponse({"response": response}, status=200)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    else:
        return JsonResponse({"error": "Invalid HTTP method"}, status=400)


# @api_view(['POST'])
@api_view(['GET', 'POST'])
def submit_link(request):
    if request.method == 'GET':
        return Response({"msg":"Its working"},status=status.HTTP_200_OK)
    elif request.method == 'POST':
        video_link = request.data.get('video_link')
        destination, summ = main_summarizer(video_link)
        # link = temp.hello()
        # print(link)
        return Response({"summary":summ,"video-url":destination},status=status.HTTP_201_CREATED)
