import time

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Book
import decimal


# Create your views here.
def find_all_books_view(request):
    all_books = Book.objects.filter(is_active=True)

    return render(request, 'bookstore/all_books.html', locals())


def update_book(request, book_id):
    try:
        book = Book.objects.get(id=int(book_id))
    except Exception as e:
        return HttpResponse('no book')
    if request.method == 'GET':
        return render(request, 'bookstore/update_books.html', locals())
    elif request.method == 'POST':
        new_price = request.POST.get('price')
        if not new_price:
            return HttpResponse('Please give me price!')
        to_update = False
        if decimal.Decimal(new_price) != book.price:
            to_update = True
        if to_update:
            book.price = new_price
            book.save()
        return HttpResponseRedirect('/bookstore/all_books')

def delete_book(request,book_id):
    # 伪删除
    books = Book.objects.filter(id=book_id,is_active=True)
    if not books:
        return HttpResponse('==no book==')
    book = books[0]
    book.is_active = False
    book.save()

    return HttpResponseRedirect(reverse('all_books'))



