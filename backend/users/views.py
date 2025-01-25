from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User

@csrf_exempt
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():
            return JsonResponse({'error': '用户名已存在'}, status=400)
        User.objects.create(username=username, password=password)
        return JsonResponse({'message': '注册成功'})
    return JsonResponse({'error': '无效请求'}, status=400)

@csrf_exempt  # 确保这里有 login 函数
def login(request):  # <--- 重点检查函数名是否拼写正确
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username, password=password)
            return JsonResponse({'message': '登录成功'})
        except User.DoesNotExist:
            return JsonResponse({'error': '用户名或密码错误'}, status=400)
    return JsonResponse({'error': '无效请求'}, status=400)