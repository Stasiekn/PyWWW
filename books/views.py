from books.models import Book
from books.forms import BookForm
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse


def add_book(request):
    form = BookForm()
    if request.method =="POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse("books:add"))
    return render(request=request, template_name="books/add.html", context={"form" : form})


def book_list(request):
    books = Book.objects.all()
    context = {'book_list' : books}
    return render(request, "books/list.html", context)


def book_details(request, book_id):
    book = Book.objects.get(pk=book_id)
    return render(
        request=request,
        template_name="books/details.html",
        context={"book" : book}
    )

