from django.shortcuts import render, redirect

# Create your views here.

data_storage = {}

def welcome(request):
    return render(request, 'welcome.html')

def create(request):
    if request.method == 'POST':
        key = request.POST.get('key')
        value = request.POST.get('value')
        data_storage[key] = value
        return redirect('read')
    return render(request, 'create.html')

def read(request):
    return render(request, 'read.html', {'data_storage': data_storage})

def update(request):
    if request.method == 'POST':
        key = request.POST.get('key')
        value = request.POST.get('value')
        if key in data_storage:
            data_storage[key] = value
        return redirect('read')
    return render(request, 'update.html')

def delete(request):
    if request.method == 'POST':
        key = request.POST.get('key')
        if key in data_storage:
            del data_storage[key]
        return redirect('read')
    return render(request, 'delete.html')