# Posts Views
from django.shortcuts import render
from datetime import datetime
from django.contrib.auth.decorators import login_required

posts = [
    {
        'title': 'Mont Blanc Hotel',
        'user': {
            'name': 'Yésica Cortés (Concierge)',
            'picture': 'https://picsum.photos/60/60/?image=1027'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://i.picsum.photos/id/180/2400/1600.jpg?hmac=Ig-CXcpNdmh51k3kXpNqNqcDYTwXCIaonYiBOnLXBb8',
    },
    {
        'title': 'Via Láctea Hotel',
        'user': {
            'name': 'Christian Van der Henst (CEO)',
            'picture': 'https://picsum.photos/60/60/?image=1005'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://i.picsum.photos/id/225/1500/979.jpg?hmac=jvGoek9ng_Y0GaBbzxN0KJhHaiPtk1VfRcukK8R8FxQ',
    },
    {
        'title': 'New Hotel',
        'user': {
            'name': 'Uriel (Manager)',
            'picture': 'https://picsum.photos/60/60/?image=883'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/500/700/?image=1076',
    }
]

@login_required
def list_posts(request):
    """List existing posts."""
    return render(request, 'post/feed.html', {'posts': posts})


