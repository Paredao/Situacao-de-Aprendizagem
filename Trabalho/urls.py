from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import TarefaViewSet
from django.shortcuts import redirect

router = DefaultRouter()
router.register(r'tasks', TarefaViewSet)

def redirect_to_home(request):
    return redirect('/admin')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', redirect_to_home),
]
