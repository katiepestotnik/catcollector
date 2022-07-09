from django.shortcuts import render
from django.http import HttpResponse
from .models import Cat
from django.views.generic.edit import CreateView, UpdateView, DeleteView
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
    return render(request, 'cats/detail.html', {
        'cat':cat
    })
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