from django.shortcuts import render, render_to_response
from django.db.models import Q
from django.http import HttpResponse
from dor.models import DorBookInf
import time
book_sum=DorBookInf.objects.all().count()
book_list = DorBookInf.objects.all



def new_book(request):
    pass

def show_books_info(request):
    pass

#书籍检索那里 实现数据库搜索打印

def share_books(request):

    userno = request.session.get('userno',None)

    username = request.session('username',None)

    if request.method=="POST":

        book_name=request.POST.get("book_name",None)
        book_author = request.POST.get("book_author", None)
        book_desc=request.POST.get("book_desc",None)


        print(book_author,book_desc,book_name)
        change = DorBookInf.objects.filter(Q(book_name=book_name) | Q(book_author=book_author)|Q(book_desc=book_desc)).update(
                                                                            book_share_man="1",
                                                                            book_share_time=time.strftime('%Y-%m-%d', time.localtime(time.time())),
                                                                            book_borrowman=username
                                                                             )

        book_borrow_list = DorBookInf.objects.filter(book_borrowman=username)
        book_share_list = DorBookInf.objects.filter(book_share_man="1", book_borrowman=username)
        return render(request, "student/book.html", {'book_list': book_list,
                                                     'book_borrow_list': book_borrow_list,
                                                     'book_share_list': book_share_list,
                                                     'book_sum':book_sum})


def borrow_books(request,get_id):#放在借阅表里面#
    userno = request.session.get('userno', None)

    username = request.session.get('username', None)
    if request.method=="POST":

        change = DorBookInf.objects.filter(book_id=get_id).update(book_borrow="1",
                                                                        book_borrow_state="1",
                                                                        book_operation=time.strftime('%Y-%m-%d', time.localtime(time.time())),
                                                                        book_borrowman=username,

                                                                       )


    book_borrow_list = DorBookInf.objects.filter(book_borrowman=username)
    book_share_list = DorBookInf.objects.filter(book_share_man="1", book_borrowman=username)
    return render(request, "student/book.html", {'book_list': book_list,
                                                    'book_borrow_list': book_borrow_list,
                                                     'book_share_list': book_share_list,
                                                 'book_sum': book_sum
                                                 })
pass

def find_books(request):

   if request.method=="POST":
    book_name=request.POST.get("book_name", None)#主键
    book_author=request.POST.get("book_author",None)
    book_word=request.POST.get("book_word",None)
    contributor=request.POST.get("contributor",None)
    userno = request.session.get('userno', None)

    username = request.session('username', None)
    book_list=DorBookInf.objects.filter(book_name=book_name)
    #get到那个检索值
    if book_list:
        print(book_list)
        error=" "
    else:
        book_list=DorBookInf.objects.all()
        error="检索出错，不存在"
    pass

    book_borrow=DorBookInf.objects.filter(book_borrowman=username)
    book_share_list = DorBookInf.objects.filter(book_share_man="1", book_borrowman=username)
    return render(request, "student/book.html", {"book_name": book_name,
                                                    "book_borrow_list":book_borrow,
                                                    "book_list": book_list,
                                                    "book_share_list":book_share_list,
                                                 'book_sum': book_sum,
                                                    "error":error})
    #
    # try:
    #     a=models.book_Inf.objects.get(book_name=book_name)
    # except Exception:
    #     a=None
    #
    # if (a!=None):
    #     print(a.book_name,a.book_author,a.book_word,a.contributor)
    #     return render(request, "student/book.html")
    # else:
    #     return HttpResponse("<p>数据搜索失败！</p>")

pass

def look_books(request):
    return render(request, "admin/bookManager.html", {'book_list': book_list})

def return_books(request,get_id):
    if request.method=="POST":
        userno = request.session.get('userno', None)
        username = request.session('username', None)
        book_name = request.POST.get("return", None)
        change=DorBookInf.objects.filter(book_name=book_name,book_id=get_id).update(book_borrow="0",
                                                                                         book_borrow_state="0",
                                                                                         book_operation="",
                                                                                         book_share_man="0",
                                                                                         book_share_time="",
                                                                                         book_borrowman = "")
    book_borrow_list = DorBookInf.objects.filter(book_borrowman=username)
    book_share_list = DorBookInf.objects.filter(book_share_man="1", book_borrowman=username)
    return render(request, "student/book.html", {'book_list': book_list,
                                                     'book_borrow_list': book_borrow_list,
                                                     'book_share_list': book_share_list,
                                                     'book_sum': book_sum
                                                 })

    pass