from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'test', views.TestViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('list/', views.indexView, name="list"),
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
