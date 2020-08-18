import datetime
from django.shortcuts import render
from django.shortcuts import redirect, reverse
from django.http import JsonResponse

from . import models
# Create your views here.


def find_user(request):
    """
    从 session 得到 user_id 返回 user 对象
    :param request:
    :return: user 对象
    """
    user_id = request.session.get('user_id')
    login_user = models.User.objects.get(id=user_id)
    return login_user


def user(request):
    """
    根据 session 中的信息得到哪个用户在登录，由用户 id 返回用户信息
    :param request: session.user_id
    :return: 一个 json 数据 user，包括 id,name,balance
    """
    login_user = find_user(request)
    data = {
        'name': login_user.name,
        'balance': login_user.balance,
    }
    return JsonResponse(data)


def borrow_history(request):
    """
    根据 session 中的信息，返回 user 有关信息。
    :param request:
    :return: 一个 json 数据 data ，包括已登录用户已归还的书籍借阅历史，每条数据包括 id，book，borrowed_time,return_time,cost,balance
    """
    login_user = find_user(request)
    log_li = models.Log.objects.filter(user=login_user.id)
    data = []
    for log in log_li:
        each_data = {
            'id': log.id,
            'book': log.book.title,
            'borrowed_time': log.borrowed_time.strftime('%Y-%m-%d %H:%M'),
            'return_time': log.return_time.strftime('%Y-%m-%d %H:%M'),
            'cost': log.cost,
            'balance': log.balance
        }
        data.append(each_data)
    result = {'count': log_li.count(), 'data': data}
    return JsonResponse(result)


def borrow_info(request):
    """
    根据 session id ，返回用户 未归还书籍的信息。
    :param request:
    :return: 一个 json 数据 data，每条数据包括 id ,book, borrowed_time,return_ddl,is_timeout
    """
    login_user = find_user(request)
    info_li = login_user.borrowinfo_set.all()
    data = []
    for info in info_li:
        each_data = {
            'id': info.id,
            'book': info.book.title,
            'borrowed_time': info.borrowed_time.strftime('%Y-%m-%d %H:%M'),
            'return_ddl': info.return_ddl.strftime('%Y-%m-%d %H:%M'),
            'is_timeout': info.is_timeout(),
        }
        data.append(each_data)
    result = {'count': info_li.count(), 'data': data}
    return JsonResponse(result)


def balance_change(request):
    """
    session id 返回用户余额的变化情况
    :param request:
    :return: 一个 json 数据 data，每条数据包括 id, action, time, change_num, balance
    """
    login_user = find_user(request)
    changes = login_user.balancechange_set.all()
    data = []
    for change in changes:
        each_data = {
            'id': change.id,
            'time': change.time.strftime('%Y-%m-%d %H:%M'),
            'action': change.get_action_display(),
            'change_num': change.change_num,
            'balance': change.balance,
        }
        data.append(each_data)
    result = {'count': changes.count(), 'data': data}
    return JsonResponse(result)


def book_search(request):
    """
    根据搜索关键字，返回 book 搜索结果
    :param request: request.GET.get('title')
    :return: 一个 json 数据 books ，每条数据包括 id，title，is_borrow,author,pub_date,tag
    """
    pass


def borrow_book(request):
    """
    根据 book_id ，session id 判断用户借书是否成功，成功添加借阅历史
    :param request: book_id, session id
    :return: 一个 json 数据 data，包括 借书是否成功信息
    """
    pass


def return_book(request):
    """
    接收 borrow_info_id session_id 查看是否逾期,未逾期还书成功，加入借书历史，删除此条记录，逾期需要扣除费用后完成此操作，还需要扣费成功后，
    增加用户余额变化情况。同时还需要将书籍的借阅数量减 1 。
    :param request:
    :return:
    """
    login_user = find_user(request)
    borrowed_id = request.GET.get('borrow_info')
    borrowed_info = models.BorrowInfo.objects.get(id=borrowed_id)
    cost = 0
    balance = login_user.balance
    print(borrowed_info.is_timeout)
    if borrowed_info.is_timeout():
        days = (datetime.datetime.now() - borrowed_info.return_ddl).days
        print(days)
        cost = round(days * 0.1, 1)
        balance = round(login_user.balance - cost, 1)
        print(cost, balance)
        models.BalanceChange(user=login_user, action='cost', time=datetime.datetime.now(), change_num=cost,
                             balance=balance).save()
    print(borrowed_info.book.id)
    book = models.Book.objects.get(id=borrowed_info.book.id)
    book.borrowed_num -= 1
    book.save()
    models.Log(user=login_user, book=borrowed_info.book, borrowed_time=borrowed_info.borrowed_time,
               return_time=datetime.datetime.now(), cost=cost, balance=balance).save()
    borrowed_info.delete()
    result = {'message': '您已还书成功，此次消费{}元'.format(cost)}
    return JsonResponse(result)


def login_check(request):
    """
    根据登录信息，确认用户信息是否填写正确
    :param request:
    :return: 登录状态，成功返回成功状态，失败返回失败原因
    """
    print(request.path)
    username = request.POST.get('username')
    password = request.POST.get('password')
    print(username, password)
    status = False
    try:
        login_user = models.User.objects.get(name=username)
        if password == login_user.password:
            request.session['user_id'] = login_user.id
            request.session['user_name'] = login_user.name
            status = True
            message = '登录成功'
            print(True)
        else:
            message = '密码不正确'
    except Exception as e:
        print(e)
        message = '用户名不存在'
    data = {'status': status, 'message': message}
    return JsonResponse(data)












