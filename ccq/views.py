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
# from .pipelines import temp


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
