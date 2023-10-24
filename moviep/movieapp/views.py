from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm
# Create your views here.

def index(request):
    movie = Movie.objects.all()
    context = {'list': movie}
    return render(request, 'index.html', context)

#
# def id(request, movie_id):
#     mov = Movie.objects.get(id=movie_id)
#     return render(request, 'detail.html', {'m': mov})
#
#
# def add(request):
#     if request.method == 'POST':
#         name = request.POST.get('name', )
#         desc = request.POST.get('desc', )
#         year = request.POST.get('yr', )
#         img = request.FILES['img']
#         mvi = Movie(name=name, desc=desc, year=year, img=img)
#         mvi.save()
#         return redirect('/')
#     return render(request, 'add.html')
#
#
# def update(request, id):
#     movie = Movie.objects.get(id=id)
#     form = MovieForm(request.POST or None, request.FILES, instance=movie)
#     if form.is_valid():
#         form.save()
#         return redirect('/')
#     return render(request, 'edit.html', {'movie':movie,'form':form})
#
# def delete(request,id):
#     if request.method=='POST':
#        movie=Movie.objects.get(id=id)
#        movie.delete()
#        return redirect('/')
#     return render(request,'delete.html')
