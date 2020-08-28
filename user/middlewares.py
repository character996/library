from django.http import JsonResponse
import re
from django.shortcuts import redirect, reverse

re_api = re.compile('/api/.*/')
re_handle = re.compile('/handle/.*/')
exclude_path = ['/api/login_check/', '/api/register_check/']


def check_login_middleware(get_resp):

    def wrapper(request, *args, **kwargs):
        if request.path not in exclude_path:
            if re_api.match(request.path) or re_handle.match(request.path):
                # 会话中包含user_id则视为已经登录
                if 'user_id' not in request.session:
                    print('未登录，重定向')
                    return redirect(reverse('user:login'))
        return get_resp(request, *args, **kwargs)
    return wrapper
