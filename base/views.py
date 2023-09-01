from django.shortcuts import render

# Create your views here.
rooms = [
    {'id': 1, 'name': 'Ancent the Dev'},
    {'id': 2, 'name': 'Ancent Marion'},
    {'id': 3, 'name': 'Franscisca Wayua'},
]

def home(request):
    data = {'rooms': rooms}
    return render(request, 'base/home.html', data)

def room(request, pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    data = {'room' : room}
    return render(request, 'base/room.html', data)
