from django.shortcuts import render
import json
import requests
from bs4 import BeautifulSoup
import re
import urllib.request as u
import pandas as pd

# Create your views here.
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib.auth.models import User #####

def index(request):
    return HttpResponse("Hello, world. You're at the article index.")

def summary_extractor(html):

    r = requests.get(html)
    soup = BeautifulSoup(r.text,'lxml')
    schema = soup.prettify()
    class_values,data = [],[]
    class_unique = {}

    title = soup.title.text
    p_val = soup.findAll('p')
    div_val = soup.findAll('div')

    for i in p_val:
        if i.attrs != {}:
            if 'class' in i.attrs.keys() and 'css' in i.attrs.get('class')[0]:
                class_values.append(('p',i.attrs.get('class')[0]))
    for i in div_val:
        if i.attrs != {}:
            if 'class' in i.attrs.keys() and 'body' in i.attrs.get('class')[0].lower():
                class_values.append(('div',i.attrs.get('class')[0]))
        if 'class' in i.attrs.keys() and 'headlines' in i.attrs.get('class')[0].lower():
            class_values.append(('div',i.attrs.get('class')[0]))
        if 'class' in i.attrs.keys() and 'text' in i.attrs.get('class')[0].lower():
            class_values.append(('div',i.attrs.get('class')[0]))
    if class_values == []:
        for i in soup.findAll('p'):
            if i.attrs == {}:
                data.append(i.text)

    for i in class_values:
        if i in class_unique.keys():
            class_unique[i] = class_unique[i] + 1
        else:
            class_unique[i] = 1

    if data == []:
        max_val = list(sorted(class_unique.items(), key=lambda x:x[1], reverse = True))
        if max_val != [] :
            max_class= max_val[0][0]

        for line in soup.findAll(max_class[0], class_ = max_class[1]):
            data.append(line.text)

    article_summary = " ".join(data).replace("\n","")

    return(title,article_summary,schema)
    
def extract_test(request):
    article = request.GET.get('article', None)

    print('article:', article)

    title = summary_extractor(article)[0]

    data = {
        'summary': title,
        'raw': 'Successful',
    }

    print('json-data to be sent: ', data)

    return JsonResponse(data)