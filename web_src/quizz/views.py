from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import admin


from .forms import connectForm


def index(request):
    users = [
        {
            "username": "admin1",
            "password": "admin1"
        },
        {
            "username": "admin2",
            "password": "admin2"
        },
        {
            "username": "user1",
            "password": "user1"
        }
    ]

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        form = connectForm(request.POST)
        user = authenticate(request,
                            username=username,
                            password=password)
        if user is not None:
            if not user.get_user_permissions():
                return HttpResponse("Pas le droit")
            login(request, user)
            print(user.get_user_permissions())
            # return HttpResponse("<p>success</p>")
            # return render(request, "admin/")
            return redirect("../admin/")
        else:
            return HttpResponse("<p>fail</p>")

    #     if form.is_valid():
    #         # for user in users:
    #         #     if user["username"] == user_input and user["password"] == user_password:
    #         form
    #         return render(request, "quizz/connect_user.html", {'form': form, 'value_list': users})
    #         # return HttpResponse("<p>WRONG INPUT</p>")
    # else:
    form = connectForm()
    return render(request, "quizz/index.html", {'form': form, 'value_list': users})
