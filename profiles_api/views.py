from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView


class HelloApiView(APIView):
    """Test API View"""
    def get(self, request, format=None):
        """Return a list of APIView fetures"""
        an_apiview = [
            'Users HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to  traditional Django View',
            'Gives you the most control over you application logic',
            'Is mapped manaually to URLs',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})