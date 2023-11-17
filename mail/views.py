from django.shortcuts import render
from .utlls import send_email_to_client
# Create your views here.
def main(request):
    if request.method == "POST":
        send_email_to_client(request.POST["email"])

    return render(request,"mail/main.html")


def contactUs(request):
    data = {}
    return render(request,"mail/contact.html",data)


def About(request):
    data = {}
    return render(request,"mail/about.html",data)