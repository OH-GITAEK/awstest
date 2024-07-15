from django.shortcuts import render, redirect
from .models import LocalUser
from .forms import LocalUserForm

# Create your views here.
def userList(request):
  search_txt = request.GET.get('search_txt')
  users = LocalUser.objects.all()
  if search_txt:
    users = users.filter(name__contains=search_txt)
  ctx = {'users': users}
  return render(request, 'users/list.html', ctx)

def create(request):
  if request.method == 'GET':
    form = LocalUserForm()
    ctx = {'form': form}
    return render(request, 'users/create.html', ctx)
  form = LocalUserForm(request.POST)
  if form.is_valid():
    form.save()
  return redirect('users:list')

def delete(request, pk):
  if request.method == 'POST':
    LocalUser.objects.get(id=pk).delete()
  return redirect('users:list')

def update(request, pk):
  user = LocalUser.objects.get(id=pk)

  if request.method == 'GET':
    form = LocalUserForm(instance=user)
    ctx = {'form': form, 'pk': pk}
    return render(request, 'users/update.html', ctx)
  
  form = LocalUserForm(request.POST, instance=user)
  if form.is_valid():
    form.save()
  return redirect('users:list')