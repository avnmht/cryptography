from django.shortcuts import render
from Myapp.models import activusers
from django.http import Http404
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
import json
import uuid
import hashlib
# Create your views here.
def index(request):
    response=json.dumps([{}])
    return HttpResponse(response,content_type="text/json")
def get_pass(request, final):
    if request.method == 'GET':
        try:
            first=final.split("&")
            activ=activusers.objects.filter(authtoken=first[0])
            if(len(activ)!=0):
                passs=first[1]
                new_pass = passs
                hashed_password = hash_password(new_pass)
                response=json.dumps([{'final':hashed_password}])
            else:
                response=json.dumps([{"Error" :"Authtoken is invalid"}])
        except:
            response=json.dumps([{"Error" :"With the form of request"}])
    return HttpResponse(response,content_type="text/json")

'''    
def home(request):
    return render(request,"home.html")
'''
def hash_password(password):
    salt = uuid.uuid4().hex
    p=uuid.uuid4().hex
    p=str(password)
    hashed=hashlib.sha1(salt.encode() + p.encode()).hexdigest() 
    for i in range(0,10):
        hashed=hashlib.sha1(hashed.encode()).hexdigest()
    return hashed + ":" + salt
'''
    
def check_password(hashed_password, user_password):
    password, salt = hashed_password.split(':')
    return password == hashlib.sha1(salt.encode() + user_password.encode()).hexdigest()
@api_view(["GET"])
def Hasher(request,final):
    try:
        print(final)
        final=(request.body).decode()
        first=final.split("&")
        authtoken = ((first[0]).split("="))[1]
        passs=((first[1]).split("="))[1]
        activ=activusers.objects.filter(authtoken=authtoken)
        if(len(activ)!=0):
            new_pass = passs
            hashed_password = hash_password(new_pass)
            #old_pass = input('Now please enter the password again to check: ')
            content={"h":hashed_password}

            return JsonResponse(hashed_password,safe=False)
        else:
            return JsonResponse("your authtoken is not active",safe=False) 
    except ValueError as e:
        return Response(e.args[0],status.HTTP_400_BAD_REQUEST)
'''