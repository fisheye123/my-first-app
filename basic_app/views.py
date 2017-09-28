from django.shortcuts import render, render_to_response

def mainpage(request):
    return render(request, 'mainpage.html', {})