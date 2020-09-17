from django.shortcuts import render
from django.http import HttpResponse

posts=[
    {
        'author':'Vijay',
        'title':'Blog 1',
        'content':'Blog 1 content',
        'date':'September 17, 2020'
    },
    {
        'author': 'Sainath',
        'title': 'Blog 2',
        'content': 'Blog 2 content',
        'date': 'September 18, 2020'
    }
]
# Create your views here.
def home(request):
    context={
        'posts': posts
    }
    return render(request, 'myapp/home.html',context)

def about(request):
    return render(request, 'myapp/about.html',{'title':'about'})