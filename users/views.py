from django.http import HttpResponse


def list_users(request):
    users = [1,2,3,4,5,6]
    return HttpResponse(str(users))

# Create your views here.
