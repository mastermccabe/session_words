from django.shortcuts import render, HttpResponse, redirect
import re
from django.contrib import messages
from time import gmtime, strftime
from django.utils.crypto import get_random_string
import random, string




# from models import *
# the index function is called when root is visited
def index(request):
    # if not 'count' in session:
    if request.method == 'GET':
        if 'deploy' not in request.session:
            request.session['words']=''
            request.session['color']=''
            request.session['size']=False
            request.session['deploy']=[]
    else:
        request.session['words'] = request.session['words']
        request.session['color']=request.session['color']
        request.session['color']=request.session['color']
        # else:
        # count += 1

        return render(request,'SessionWords/index.html')

    # print session['counter']

    return render(request,'SessionWords/index.html')


def clearsession(request):
    request.session.clear()
    return redirect('/session_words')
# def new(request):

def addword(request):
    if request.method =='POST':

        words =request.POST.get('text_field')
        color=request.POST.get('color')
        big = request.POST.get('big')
        if big == None:
            big = 6
        else:
            big = 2
        # words = request.form['text_field']


        request.session['words'] = words
        request.session['color'] = color
        request.session['big'] = big
        deploy = [{'words':words, 'color':color, 'big':big}]


        request.session['deploy'] += deploy
        print request.session['deploy']
        return redirect('/session_words')
        # return redirect('/session_words')
