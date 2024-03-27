from django.shortcuts import render, redirect
from .forms import LinkForm
from  .models import Links


# Create your views here.
def index(request):
    # news = News.objects.all()
    # categories = Category.objects.all()

    context = {
        # 'news': news,
        #'category': category,
        'titlepage': 'Список ссылок'
        # 'categories': categories
    }

    return render(request, 'links/index.html', context)


def add_link(request):
    if request.method == 'POST':
        form = LinkForm(request.POST)
        if form.is_valid():

            links = form.save()
            return redirect(links)
    else:
        current_user = request.user
        initial_dict = {'user': current_user.id }
        form = LinkForm(initial = initial_dict)


    return render(request, 'links/add_link.html', {'form': form})


def user_links(request, user):
    links = Links.objects.filter(user=user)
    domain = request.get_host()

    context = {
        'links': links,
        'domain': domain,
        'titlepage': 'Список пользовательских ссылок'
        # 'categories': categories
    }

    return render(request, 'links/user_links.html', context)


def redirect_link(request, abbrlink):
    gotolnk = Links.objects.get(shortlink=abbrlink)
    return redirect(gotolnk.link)