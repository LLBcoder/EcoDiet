from django.shortcuts import render, redirect, get_object_or_404
import json
import random
import requests
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .forms import *
from .decorators import *
# Create your views here.


@authenticated_user
def createMealplan(request):

    # Creation of a url with the user's info (intolerances and ingredients)
    restriction = Restrictions.objects.get(user=request.user)
    intolerances = restriction.intolerance.all().values()
    ingredients = restriction.ingredient.all().values()

    intoleranceurl = '&intolerances='
    for i in intolerances :
        intoleranceurl += i['intolerance']+','
    
    ingredienturl = '&excludeIngredients='
    for i in ingredients :
        ingredienturl += i['ingredient']+','

    dietgoal = '&diet='+restriction.dietgoal
    level = restriction.level



    mealplanurl = "https://api.spoonacular.com/recipes/complexSearch?apiKey={}&type=maincourse&number=100"
    apiKey = '715492e736264d1a91e91152b3faac53'
    completeurl = mealplanurl.format(apiKey)+dietgoal+intoleranceurl+ingredienturl


    #Use the API or JSON file

    # data = requests.get(completeurl).json()

    with open('recipes.json') as f:
        data = json.load(f)

    recipeslist = data['results']


    #Generate random number for random list of recipes    
    recipesnum = []

    if level == 'Trying it out!':
        i = 3
    if level == 'Commited to change!':
        i = 5    
    if level == 'Full on transition!':
        i = 7


    while len(recipesnum) < i:
        randomnum = random.randint(0, len(recipeslist)-1)
        if randomnum not in recipesnum :
            recipesnum.append(randomnum)
    
    recipes = []
    for num in recipesnum:
        recipes.append(recipeslist[num]['id'])

    global val
    def val():
        return recipes


    return redirect('/')


@authenticated_user
def home(request):
    #Easily change restrictions
    form = RestrictionsForm(instance=get_object_or_404(Restrictions, user=request.user))

    if request.method =='POST' :
        form = RestrictionsForm(request.POST, instance=get_object_or_404(Restrictions, user=request.user))
        if form.is_valid():
            form.save()
            return redirect('/create')


    #Search for every recipes information
    recipes=val()
    print(recipes)
    
    recipesinfo = []

    for recipe in recipes :

        recipeurl = "https://api.spoonacular.com/recipes/{}/information?includeNutrition=false&apiKey={}"

        apiKey = '715492e736264d1a91e91152b3faac53'
        recipeinfodata = requests.get(recipeurl.format(recipe,apiKey)).json()

        
        recipeinfo = {
            'title': recipeinfodata['title'],
            'sourceurl':recipeinfodata['sourceUrl'],
            'summary':recipeinfodata['summary'],
            'image':recipeinfodata['image']
        }
        recipesinfo.append(recipeinfo)
    
    
    context = {'form':form, 'recipesinfo':recipesinfo}
    return render(request, 'mealplan/main.html', context)


@authenticated_user
def profilePage(request): 
    form = DietForm(instance=get_object_or_404(Restrictions, user=request.user))
    if request.method =='POST' :
        form = DietForm(request.POST, instance=get_object_or_404(Restrictions, user=request.user))
        if form.is_valid():
            form.save()
            return redirect('/create')
    

    context = {'form':form}
    return render( request, 'mealplan/profile.html', context)


@unauthenticated_user
def registerPage(request):

    form = CreateUserForm()
    if request.method=='POST' :
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()

            restrictionform = RestrictionsForm()
            restriction = restrictionform.save(commit=False)
            restriction.user = user
            restriction.save()

            return redirect('/login')

    context = {'form':form}

    return render(request, 'mealplan/register.html', context)


@unauthenticated_user
def loginPage(request):

    if request.method=='POST' :
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)

        if user is not None :
            login(request, user)
            return redirect('/create')


    context = {}
    return render(request, 'mealplan/login.html', context)


@login_required(login_url='login')
def logoutPage(request):
    logout(request)
    return redirect('/demo')

@unauthenticated_user
def demoPage(request):
    form = RestrictionsForm()
    context = {'form':form}
    return render(request, 'mealplan/demo.html', context)