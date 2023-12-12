from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponseRedirect, HttpResponsePermanentRedirect, HttpResponseNotFound, \
    HttpResponseForbidden, HttpResponse, JsonResponse
from django.shortcuts import render

PostList = [
    {'id': 1, 'name': 'Открытие школы', 'text': 'В городе Елабуга была открыта новая общеобразовательная школа',
     'image': '/static/skoll.jpg', 'comment': 'Очень круто!', 'like': 8},
    {'id': 2, 'name': 'Новый завод Алабуги',
     'text': 'В городе Елабуга был построен новый завод по производству студентов "Роботов"',
     'image': '/static/zavod.jpg', 'comment': 'Очень интересно!', 'like': 10}
]


def PostIdView(request, id):
    post = {}
    for i in PostList:
        if i['id'] == int(id):
            post = i
            break
    return render(request, 'post.html', {'post': post})


def PostView(request):
    return render(request, 'posts.html', context={'form': PostList})

def AboutView(request):
    return HttpResponseRedirect('/app/posts')

def ContactsView(request):
    return HttpResponsePermanentRedirect('/app/posts')

def Test404(request):
    return HttpResponseNotFound('Загрузка страницы была завершена ошибкой')

def ProfileView(request):
    name_user = request.GET.get('name')
    password_user = request.GET.get('password')
    return render(request, 'profile.html', context={'name': name_user, 'password': password_user})

def AdminView(request):
    name_user = request.GET.get('name')
    password_user = request.GET.get('password')
    if name_user == 'admin' and password_user == 'admin':
        return render(request, 'admin.html', context={'name': name_user, 'password': password_user})
    else:
        return HttpResponseForbidden('Доступ запрещен, проверьте логин или пароль')

def SetView(request):
    username = request.GET.get("username", 'Неизвестен')
    response = HttpResponse(f'Hello {username}')
    response.set_cookie('username', username)
    return HttpResponse(response)

def GetView(request):
    username = request.COOKIES['username']
    return HttpResponse(f'Hello {username}')

def index(request):
    bob = Person(request.GET.get('username', 'Неизвестен'), request.GET.get('age', 'Неизвестен'))
    return JsonResponse(bob, safe=False, encoder=PersonEncoder)

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

class PersonEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, Person):
            return {'name': obj.name, 'age': obj.age}
        return super().default(obj)
