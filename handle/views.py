from django.shortcuts import render

# Create your views here.


def home(request):
    """
    登录之后返回用户主页面
    :param request: http 请求
    :return: home.html
    """
    return render(request, 'handle/home.html')


def search_book(request):
    """
    返回搜索图书结果页面
    :param request: http 请求
    :return: search_book.html
    """
    return render(request, 'handle/search_book.html')


def recharge(request):
    """
    返回充值金额页面
    :param request: http 请求
    :return: recharge.html
    """
    return render(request, 'handle/recharge.html')