from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import googletrans




def home (request) : 
    languages = googletrans.LANGUAGES.values()
    return render( request, 'index.html' ,context={'langs':languages})



def translate (request ) :

    text = ''

    
    trans = googletrans.Translator()

    if 'keyword' in request.GET :
        keyword = request.GET['keyword']
        language = request.GET['language']

        text = trans.translate(keyword,dest=language).text 


    return HttpResponse(text)