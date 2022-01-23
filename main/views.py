from django.http import HttpResponse
from django.shortcuts import render
from main.forms import ContactForm, UserProfileForm
from . import services
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404


def user_profile(request, user_id):
    user = get_object_or_404(get_user_model(), id=user_id)
    if request.method =="POST":
        try:
            profile =user.userprofile
            form = UserProfileForm(request.POST, istance=profile)
        except AttributeError: pass
        if form.is_valid(): form.save()
    else:
        try:
            profile = user.userprofile
            form = UserProfileForm(instance=profile)
        except AttributeError:
            form = UserProfileForm(initial={"user": user, "bio":""})
        if request.user != user:
            for field in form.fields:
                form.fields[field].disabled = True
            form.helper.inputs = []
    return render(request, 'main/userprofile.html', {'form' : form})



def contact(request):
    if request.method == "POST":
        form = ContactForm(data=request.POST)
        if form.is_valid():
            services.send_message(form.cleaned_data)
            return HttpResponseRedirect(reverse("main:contact"))
    else:
        form = ContactForm()
    return render(
        request,
        "main/contact.html",
        {"form" : form}
    )


def hello_word(request):
    return render(request, "main/hello_word.html", {})


def about(request):
    return render(request, "main/about.html", {})


def some_test(request):
    age = 33
    first_name = 'łukasz'
    gry = ['gran turismo', 'wiedzmin', 'the last of us']
    programing = {
        'python' : 'easy',
        'C++' : 'aesy',
        'labview' : 'aha'
    }
    books = set(['Czysty kod', 'Posqsql'])
    return render(request, "main/some_test.html", context={
        'age' : age,
        'first_name' : first_name,
        'gry' : gry,
        'programing' : programing,
        'books' : books
    })
# Create your views here.
