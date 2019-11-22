from django.shortcuts import render
from .models import DogBreedInfo,DogInfo,CatBreedInfo,CatInfo,RabbitInfo,RabbitBreedInfo, HamsterInfo, HamsterBreedInfo
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from .forms import UserForm


# Create your views here.
dic = dict()
dic['login'] = False


def index(request):
    return render(request, 'petApp/index1.html', dic)


def dogForm(request):
    breedinfo = DogBreedInfo.objects.all()
    dic['breed_info'] = breedinfo
    return render(request, 'petApp/dogform.html', dic)


def catForm(request):
    breedinfo = CatBreedInfo.objects.all()
    dic['breed_info'] = breedinfo
    return render(request, 'petApp/catform.html', dic)


def rabbitForm(request):
    breedinfo = RabbitBreedInfo.objects.all()
    dic['breed_info'] = breedinfo
    return render(request, 'petApp/rabitform.html', dic)


def hamsterForm(request):
    breedinfo = HamsterBreedInfo.objects.all()
    dic['breed_info'] = breedinfo
    return render(request, 'petApp/hamform.html', dic)


def dogDetail(request):
    dog = DogInfo()
    dog.pet_name = request.POST["name"]
    dog.gender = request.POST["sex"]
    dog.height = request.POST["height"]
    dog.weight = request.POST["weight"]
    dog.pet_breed = DogBreedInfo.objects.get(pk=request.POST["breed"])
    dog.username = request.user.username
    dog.save()
    return render(request, 'petApp/index1.html', {"login": True})


def catDetail(request):
    cat = CatInfo()
    cat.pet_name = request.POST["name"]
    cat.gender = request.POST["sex"]
    cat.height = request.POST["height"]
    cat.weight = request.POST["weight"]
    cat.pet_breed = CatBreedInfo.objects.get(pk=request.POST["breed"])
    cat.username = request.user.username
    cat.save()
    return render(request, 'petApp/index1.html', {"login": True})


def rabbitDetail(request):
    rabbit = RabbitInfo()
    rabbit.pet_name = request.POST["name"]
    rabbit.gender = request.POST["sex"]
    rabbit.height = request.POST["height"]
    rabbit.weight = request.POST["weight"]
    rabbit.pet_breed = RabbitBreedInfo.objects.get(pk=request.POST["breed"])
    rabbit.username = request.user.username
    rabbit.save()
    return render(request, 'petApp/index1.html', {"login": True})


def hamsterDetail(request):
    hamster = HamsterInfo()
    hamster.pet_name = request.POST["name"]
    hamster.gender = request.POST["sex"]
    hamster.height = request.POST["height"]
    hamster.weight = request.POST["weight"]
    hamster.pet_breed = HamsterBreedInfo.objects.get(pk=request.POST["breed"])
    hamster.username = request.user.username
    hamster.save()
    return render(request, 'petApp/index1.html', {"login": True})


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
        "login": False
    }
    return render(request, 'petApp/dogform.html', context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                dog = DogBreedInfo.objects.all()
                cat = CatBreedInfo.objects.all()
                rabbit = RabbitBreedInfo.objects.all()
                hamster = HamsterBreedInfo.objects.all()

                return render(request, 'petApp/dogform.html', {"login": True, "dog": dog, 'cat': cat, 'rabbit': rabbit, 'hamster': hamster})
            else:
                return render(request, 'petApp/dogform.html', {'error_message': 'Your account has been disabled', "login": False})
        else:
            return render(request, 'petApp/dogform.html', {'error_message': 'Invalid login', 'login': False})
    return render(request, 'petApp/dogform.html')



def indexLogin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                dic['login'] = True
                return render(request, 'petApp/index1.html', dic)
            else:
                dic['login'] = False
                dic['error_message'] = 'Your account has been disabled'
                return render(request, 'petApp/index1.html', dic)
        else:
            dic['login'] = False
            dic['error_message'] = 'Invalid login'
            return render(request, 'petApp/index1.html', dic)
    return render(request, 'petApp/index1.html')


def indexLogout(request):
    logout(request)
    form = UserForm(request.POST or None)
    dic["form"] = form
    dic["login"] = False
    return render(request, 'petApp/index1.html', dic)

def viewDog(request):
    username = request.user.username
    dog = DogInfo.objects.filter(username=username).order_by('price')
    dic["pets"] = dog
    dic["page"] = "dog"
    return render(request, 'petApp/view.html', dic)


def viewCat(request):
    username = request.user.username
    cat = CatInfo.objects.filter(username=username)
    dic["pets"] = cat
    dic["page"] = "cat"
    return render(request, 'petApp/view.html', dic)


def viewRabbit(request):
    username = request.user.username
    rabbit = RabbitInfo.objects.filter(username=username)
    dic["pets"] = rabbit
    dic["page"] = "rabbit"
    return render(request, 'petApp/view.html', dic)


def viewHamster(request):
    username = request.user.username
    hamster = HamsterInfo.objects.filter(username=username)
    dic["pets"] = hamster
    dic["page"] = "hamster"
    return render(request, 'petApp/view.html', dic)


def blog(request):
    dic["login"] = True
    return render(request, 'petApp/blog.html', dic)


