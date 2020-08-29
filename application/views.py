from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.http import HttpResponse
from django.http import JsonResponse
from datetime import datetime
import json
import random

# for prediction

import numpy as np
import pandas as pd

from keras.models import Sequential

from keras.layers import Dense,LSTM
import sqlite3
from sklearn.model_selection import train_test_split

from sklearn.preprocessing import LabelBinarizer




# main page function

def generate_code():
    random_str = ""
    for i in range(0, 20):
        this = random.randrange(0, 9)
        random_str += str(this)

    return random_str

def predict_now(request):
    output = {}

    if request.method == 'GET':
        color = request.GET['color']
        number = int(request.GET['number'])

        if countering.objects.get(which_user = request.user).isEntered:
            print("do main task")

            output['msg'] = 'Value has been added'
        else:
            print('number =>', number)
            print('color =>', color)

            output['msg'] = 'Value has been added'

    return JsonResponse(output)   

def entry(request):
    if request.method == 'GET':
        entry = int(request.GET['entry'])
        if entry == 1:
            focused = countering.objects.get(which_user = request.user)
            focused.isEntered = True
            focused.save()

    output = {
        'msg': 'done'
    }

    return JsonResponse(output)

def index(request):
    
    if not request.user.is_authenticated:
        return redirect("login")

    context = {
        'isEntered': countering.objects.get(which_user = request.user).isEntered
    }
        
    return render(request, 'main.html', context)

# function for signup

def signup(request):
    if request.method == "POST":
        name = request.POST['name']
        l_name = request.POST['l_name']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        context = {
            "name":name,
            "l_name":l_name,
            "email":email,
            "pass1":pass1,
            "pass2":pass2,
        }
        if pass1==pass2:
            if User.objects.filter(username=email).exists():
                print("Email already taken")
                messages.info(request, "Entered number already in use!")
                context['border'] = "email" 
                return render(request, "signup.html", context)

            user = User.objects.create_user(username=email, first_name=name, password=pass1, last_name=l_name)
            user.save()
            
            return redirect("login")
        else:
            messages.info(request, "Your pasword doesn't match!")
            context['border'] = "password"
            return render(request, "signup.html", context)


    
    return render(request, "signup.html")


# function for login

def login(request):

    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(username=email, password=password)
        if user is not None:
            auth.login(request, user)

            if countering.objects.filter(which_user = request.user).exists():
                countering.objects.filter(which_user = request.user).delete()
            
            myCode = generate_code()

            new_countering = countering(
                which_user = request.user,
                code = myCode
            )

            new_countering.save()

            return redirect("index")
        else:
            messages.info(request, "Incorrect login details!")
            return redirect("login")
    else:
        return render(request, "login.html")


# function for logout

def logout(request):
    auth.logout(request)
    return redirect("index")

