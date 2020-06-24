from django.urls import path
from webapp.views import *

urlpatterns = [

    path("home/", home, name='home'),
    path("spacing/", spacing, name='spacing'),

]
