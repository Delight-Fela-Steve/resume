from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError

# Create your views here.


def index(request):
    form = ContactForm()
    return render(request, "resume/index.html",{"form":form})


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            full_name = form.cleaned_data['full_name']
            email = form.cleaned_data['email']
            message_body = form.cleaned_data['message']
            subject = f'{full_name}--copy'
            message = f'''
            Fullname: {full_name}\n\n
            Email: {email}\n\n
            Message: {message_body}

            '''
            try:
                send_mail(subject, message,'dfelastevetest@gmail.com',['dfelastevetest@gmail.com', email])
            except BadHeaderError:
                return HttpResponse('Invalid header found')
            return render(request, "resume/success.html", {'name':full_name})
    form = ContactForm()
    return render(request, "resume/index.html", {'form':form})


def success(request):
    return render(request, "resume/success.html")