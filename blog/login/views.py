from django.shortcuts import render, redirect
from .models import User
from .forms import UserForm


# главная страница
def index(request):
    # если в сессии сохранён пользователь - переходим на главную страницу
    if request.session.get('user_id'):
        # получим логин пользователя
        l = request.session.get('login')
        # переходим на главную страницу и передаем туда логин
        return render(request, 'index.html', {'login': l})
    # пользователь неавторизован - переходим на форму входа
    else:
        return redirect('/login/')


# авторизация
def login(request):
    # это get-запрос. нужно показать пустую форму
    if request.method == "GET":
        return render(request, 'login.html')
    # пришли данные. значит нужно проверить логин/пароль
    else:
        login = request.POST.get('login')
        password = request.POST.get('pas')

        # проверим что пользователь с таким логином вообще существует
        try:
            user = User.objects.get(login=login)
        except User.DoesNotExist:
            return redirect('/login/')

        # пользователь есть. проверим его пароль
        if password != user.password:
            return redirect('/login/')

        # сохраним данные пользователя в сессию
        request.session['user_id'] = user.id
        request.session['login'] = user.login
        return redirect('/')


# страница со списком пользователей
def users(request):
    # если пользователь не авторизован - отправляем на форму входа
    if not request.session.get('user_id'):
        return redirect('/login/')

    # получим всех пользователей из базы
    users = User.objects.all()
    return render(request, 'users.html', {'users': users})


# создать пользователя
def add_user(request):
    # получили данные. нужно сохранить юзера в базу
    if request.method == "POST":
        # получаем данные из формы
        user = UserForm(request.POST)
        if user.is_valid():
            user.save()
        return redirect('/login/')
    # это простой запрос, нужно показать форму
    else:
        form = UserForm()
        return render(request, "add_user.html", {'form': form})

def logout(request):
    # удалим данные пользователя из сессии
    request.session.flush()
    return redirect('/login/')
