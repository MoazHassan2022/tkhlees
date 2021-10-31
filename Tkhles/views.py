from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import *
from urllib.parse import urlparse, parse_qs
import re
import unittest
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.core.paginator import Paginator, EmptyPage, InvalidPage


def policies(request):
    return render(request, "policies.html")


def home(request):
    return render(request, "home.html")


def add(request):
    return render(request, "add.html")


def addCreditor(request):
    if request.method == "POST":
        ID = request.POST["ID"]
        name = request.POST["name"]
        phone = request.POST["phone"]
        address = request.POST["address"]
        gender = request.POST["gender"]
        additional = request.POST["additional"]
        caseNumber = request.POST["caseNumber"]
        casePlace = request.POST["casePlace"]

        cred = Creditor(NationalID=ID, name=name, address=address, phoneNumber=phone, gender=gender, additional=additional, caseNumber=caseNumber, casePlace=casePlace)
        cred.save()
        return HttpResponseRedirect(reverse("add"))


def addDebtor(request):
    if request.method == "POST":
        ID = request.POST["ID"]
        name = request.POST["name"]
        phone = request.POST["phone"]
        address = request.POST["address"]
        gender = request.POST["gender"]
        additional = request.POST["additional"]
        caseNumber = request.POST["caseNumber"]
        casePlace = request.POST["casePlace"]

        debt = Debtor(NationalID=ID, name=name, address=address, phoneNumber=phone, gender=gender, additional=additional, caseNumber=caseNumber, casePlace=casePlace)
        debt.save()
        return HttpResponseRedirect(reverse("add"))


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect("../home")
        else:
            return render(request, "login.html", {
                "message": "هذا الاسم أو كلمة السر غير صالحين."
            })
    else:
        return render(request, "login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect("../login")


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        phoneNumber = request.POST["phoneNumber"]
        email = request.POST["email"]
        pic = request.POST["pic"]
        NationalID = request.POST["NationalID"]
        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "register.html", {
                "message": "يجب أن تتوافق كلمة السر مع تأكيد كلمة السر."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password, phoneNumber=phoneNumber, pic=pic, NationalID=NationalID)
            user.save()
        except IntegrityError:
            return render(request, "register.html", {
                "message": "هذا الاسم موجود من قبل."
            })
        login(request, user)
        return HttpResponseRedirect("../home")
    else:
        return render(request, "register.html")