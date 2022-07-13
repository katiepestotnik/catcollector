from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Cat
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# bring in feeding form from forms.py
from .forms import FeedingForm
#static data for example with class
# class Cat():
#     def __init__(self, name, breed, description, age):
#         self.name = name
#         self.breed = breed
#         self.description = description
#         self.age = age
    
# cats = [
#     Cat('Orion', 'Himalayan', 'Funny Cat', 20),
#     Cat('Sylvester', 'Farm Cat', 'Black and White', 40),
#     Cat('Yoda', 'Hairless', 'No hair', 1)
# ]


# Create your views here.
def home(request):
    return HttpResponse('<h1>Hello World</h1>')

# def about(request):
#     return HttpResponse('About Page')

def about(request):
    return render(request, 'about.html')

def cats_index(request):
    cats = Cat.objects.all()
    return render(request, 'cats/index.html', {
        'cats': cats
    })
    
def cats_detail(request, cat_id):
    cat = Cat.objects.get(id=cat_id)
    # bring (instanitate) in feeding form
    feeding_form = FeedingForm()
    return render(request, 'cats/detail.html', {
        'cat':cat,
        'feeding_form': feeding_form
    })       
def add_feeding(request, cat_id):
    feeding_form = FeedingForm(request.POST)
    if feeding_form.is_valid():
        new_feeding = feeding_form.save(commit=False)
        new_feeding.cat_id = cat_id
        new_feeding.save()
    return redirect('detail', cat_id = cat_id)

class CatCreate(CreateView):
    model = Cat
    fields = '__all__'
    success_url = '/cats/'

class CatUpdate(UpdateView):
    model = Cat
    # Let's disallow the renaming of a cat by excluding the name field!
    fields = ['breed', 'description', 'age']
class CatDelete(DeleteView):
    model = Cat
    success_url = '/cats/'