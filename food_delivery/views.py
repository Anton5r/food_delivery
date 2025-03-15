from django.shortcuts import render

def my_page(request):
    return render(request, 'my_page.html')
