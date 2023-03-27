from django.shortcuts import render , HttpResponse , redirect
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import Book
from .forms import BookCreate
# Create your views here.


def mylibrarypage(request):
    shelf = Book.objects.all()
    return render (request ,'library.html',{'shelf':shelf})


def upload(request):
    upload = BookCreate()
    if request.method == 'POST':
        upload = BookCreate(request.POST,request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('home')
        else:
            return HttpResponse("""something went worng""")
    else:
        
        return render(request ,'upload_form.html',{'upload_form':upload})



def update_book(request, book_id):
    book_id = int(book_id)
    try:
        book_shelf = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        return redirect('home')
    book_form = BookCreate(request.POST or None, instance=book_shelf)
    if book_form.is_valid():
        book_form.save()
        return redirect('home')
    return render(request, 'upload_form.html', {'upload_form': book_form})

def delete_book(request, book_id):
    book_id = int(book_id)
    try:
        book_shelf = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        return redirect('home')
    book_shelf.delete()
    return redirect('home')
