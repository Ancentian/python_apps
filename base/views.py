from django.shortcuts import render

from .models import Room

# Create your views here.
# rooms = [
#     {'id': 1, 'name': 'Ancent the Dev'},
#     {'id': 2, 'name': 'Ancent Marion'},
#     {'id': 3, 'name': 'Franscisca Wayua'},
# ]

def home(request):
    rooms = Room.objects.all()
    context = {
        'rooms': rooms
        }
    return render(request, 'base/home.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk)
    data = {'room' : room}
    return render(request, 'base/room.html', data)
