from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.generics import GenericAPIView
from.searilizers import usersearilizers, loginserailizers, calculatesearizilers
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from  rest_framework import status
from django.contrib import auth
from rest_framework.decorators import permission_classes
class resgister(GenericAPIView):
    serializer_class = usersearilizers
    def post(self, request):
        searilizers=usersearilizers(data=request.data)
        if searilizers.is_valid(raise_exception=True):
            searilizers.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(searilizers.errors, status=status.HTTP_400_BAD_REQUEST)


class loginview(GenericAPIView):
    serializer_class = loginserailizers
    def post(self, request, instance=None):
        data=request.data
        email=data.get('email', '')
        password=data.get('password', '')
        user=auth.authenticate(email=email, password=password)

        if user:
            searilizers = loginserailizers(user)
            data = {
                "email": searilizers.data['email'],
            }
            return Response( data,status.HTTP_400_BAD_REQUEST)
        return Response({'details': 'Invaild creadails'}, status=status.HTTP_400_BAD_REQUEST)

class calculta(APIView, permissions.IsAuthenticated):
    serializer_class = calculatesearizilers
    def post(self, request, *args, **kwargs):
        n=int(request.data['n'])
        x=int(request.data['x'])
        sum=0
        for i in range(1, n+1):
            sum=sum + 1/(x) **i
        sum1=sum
        return HttpResponse(sum1)

