from django.shortcuts import render, HttpResponse, redirect
from app01.models import *


def addbook(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        price = request.POST.get('price')
        pub_date = request.POST.get('pub_date')
        authors_id = request.POST.getlist('authors_id')  # 取出的是主键值的列表
        publish_id = request.POST.get('publish_id')
        book = Book.objects.create(title=title, price=price, publishDate=pub_date, publish_id=publish_id)
        book.authors.add(*authors_id)  # 加'*'表示列表作为数据传进去
        return HttpResponse('添加成功')
    else:
        publishs = Publish.objects.all()
        authors = Author.objects.all()
        return render(request, 'addbook.html', locals())


def checkbooks(request):
    books = Book.objects.all()
    return render(request, 'checkbooks.html', locals())


def edit(request, id):
    if request.method == 'GET':
        book = Book.objects.all().filter(nid=id).first()
        publishs = Publish.objects.all()
        authors = Author.objects.all()
        return render(request, 'edit.html', locals())
    else:
        """取修改后的数据"""
        title = request.POST.get('title')
        price = request.POST.get('price')
        pub_date = request.POST.get('pub_date')
        authors_id = request.POST.getlist('authors_id')  # 取出的是主键值的列表
        publish_id = request.POST.get('publish_id')
        book = Book.objects.filter(nid=id).update(title=title, price=price, publishDate=pub_date, publish_id=publish_id)
        book_obj = Book.objects.filter(nid=id).first()
        # 方法1
        # book_obj.authors.clear()    # 先清除之前的书、作者关系
        # book_obj.authors.add(*authors_id)  # 加'*'表示列表作为数据传进去
        # 方法2
        book_obj.authors.set(authors_id)
        return redirect('/checkbooks/')    # checkbooks是某个视图函数


def delete(request, id):
    Book.objects.filter(nid=id).delete()
    return redirect('/checkbooks/')
