from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

# Create your views here.

def home_page(request):
    return render(request, 'home.html')


class DemoView(APIView):
    def get(self,request):
        msg ={'info':'working'}

        return Response(msg,status=status.HTTP_200_OK)