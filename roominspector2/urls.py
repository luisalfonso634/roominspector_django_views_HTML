
from django.contrib import admin
from django.urls import path
from  roominspector2 import views as local_views
from users import views as users_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello-world/', local_views.hello_world),
    path('sorted/', local_views.sort_integers),
    path('hi/<str:name>/<int:age>/', local_views.say_hi),
    path('users/', users_views.list_users )
]

