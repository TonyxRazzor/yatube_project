from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse('Главная страница')


def group_posts(group_posts, slug):
    return HttpResponse('Посты отфильтрованные по группам')
