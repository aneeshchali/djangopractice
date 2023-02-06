from django.shortcuts import render
from django.http.response import HttpResponse

articles = {'sports': 'Sports Page!',
            'finance': 'Finance Page!',
            'politics': 'Politics Page!',
            }


def news_view(request, topic):
    return HttpResponse(articles[topic])


def add_view(request, num1, num2):
    # domain.com/first_app/3/5 -->7
    result = num1 + num2
    return HttpResponse(result)

# def finance_view(request):
#     return HttpResponse(articles['finance'])
