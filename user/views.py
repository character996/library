from django.shortcuts import render
from django.shortcuts import redirect, reverse
import hashlib
from django.conf import settings
# Create your views here.


def detail_passwd(passwd, salt='add'):
    # 将密码加密
    dp = hashlib.sha256()
    passwd += salt
    # dp只接受字节类型
    dp.update(passwd.encode())
    return dp.hexdigest()


def login(request):

    return render(request, 'user/login.html')


def register(request):
    return render(request, 'user/register.html')


# def register(request):
#     if request.session.get('is_login', None):
#         return redirect('/')
#
#     message = "请填写信息注册账号"
#     if request.method == 'POST':
#         register_form = forms.RegisterForm(request.POST)
#         if register_form.is_valid():
#             username = register_form.cleaned_data.get('username')
#             password1 = register_form.cleaned_data.get('password1')
#             password2 = register_form.cleaned_data.get('password2')
#             email = register_form.cleaned_data.get('email')
#             sex = register_form.cleaned_data.get('sex')
#
#             if password1 != password2:
#                 message = '两次输入的密码不同！'
#                 return render(request, 'user/register.html', locals())
#             else:
#                 same_name_user = models.User.objects.filter(name=username)
#                 if same_name_user:
#                     message = '用户名已经存在'
#                     return render(request, 'user/register.html', locals())
#                 same_email_user = models.User.objects.filter(email=email)
#                 # if same_email_user:
#                 #     message = '该邮箱已经被注册了！'
#                 #     return render(request, 'user/register.html', locals())
#
#                 new_user = models.User.objects.create(name=username, password=detail_passwd(password1),
#                                                       email=email, sex=sex)
#                 code = make_confirm_email(new_user)
#                 send_email(email, code)
#                 message = '前往邮箱去确认'
#                 # return redirect(reverse('user:login'))
#                 return render(request, 'user/confirm.html', locals())
#         else:
#             return render(request, 'user/register.html', locals())
#     register_form = forms.RegisterForm()
#     return render(request, 'user/register.html', locals())


def logout(request):
    if not request.session.get('is_login', None):
        # 如果没有登录,跳转到登录页面
        return redirect(reverse('user:login'))
    request.session.flush()
    return redirect('/')


# def user_confirm(request):
#     code = request.GET.get('code', None)
#     message = ''
#     try:
#         confirm = models.ConfirmString.objects.get(code=code)
#     except:
#         message = '无效的确认请求!'
#         return render(request, 'user/confirm.html', locals())
#
#     c_time = confirm.c_time
#     now = datetime.datetime.now()
#     if now > c_time + datetime.timedelta(settings.CONFIRM_DAYS):
#         confirm.user.delete()
#         message = '您的邮件已经过期！请重新注册!'
#         return render(request, 'user/confirm.html', locals())
#     else:
#         confirm.user.has_confirmed = True
#         confirm.user.save()
#         confirm.delete()
#         request.session['has_confirm'] = True
#         message = '感谢确认，请使用账户登录！'
#         return render(request, 'user/confirm.html', locals())
