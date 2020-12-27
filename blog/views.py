from django.shortcuts import render, HttpResponse
from .models import Blog, Contact
from django.core.paginator import Paginator

from django.contrib.messages import constants as messages

from django.contrib import messages

# Create your views here.


def home(request):
    return render(request, 'home.html')


def blog(request):
    blogs = Blog.objects.all().order_by('sno')
    # context = {'blogs': blogs} #this is for showing all data from database
    paginator = Paginator(blogs, 2, orphans=1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj}
    # print(page_obj)
    return render(request, 'blog.html', context)


def blogpost(request, slug):
    blog = Blog.objects.filter(slug=slug).first()
    context = {'blog': blog}
    # return HttpResponse(f"this is blog page and you are viewing {slug}")
    return render(request, 'blogpost.html', context)


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']

        con = Contact(name=name, email=email, phone=phone, desc=desc)

        con.save()
        messages.success(request, 'Your message is submitted!!')
    return render(request, 'contact.html')


def search(request):
    return render(request, 'search.html')
