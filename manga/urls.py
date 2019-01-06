from django.urls import path,include
from . import views,person
from rest_framework import routers

router = routers.DefaultRouter()

router.register('person', views.PersonView)
router.register('person', views.PersonView)
router.register('person', views.PersonView)
router.register('person', views.PersonView)

urlpatterns = [
     path('', include(router.urls)),
]
