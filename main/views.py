from django.shortcuts import render, redirect

from .models import Information, MyHome, Services, Portfolio, AboutMe, Biography, Skills, Education, Resume, News, \
    Contact


def index_view(request):
    context = {
        "information": Information.objects.last(),
        "myhome": MyHome.objects.last(),
        "services": Services.objects.all().order_by('-id')[:3],
        "portfolio": Portfolio.objects.all().order_by('-id'),
        "about_me": AboutMe.objects.last(),
        "resume": Resume.objects.last(),
        "news": News.objects.all().order_by('-id')[:3],
    }
    return render(request, "home-dark.html", context)


def create_contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        contact = Contact(name=name, email=email, phone=phone, message=message)
        contact.save()
    return redirect('index')


def page_404(request, exception):
    return render(request, '404.html', {})