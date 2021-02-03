from django.urls import path
# . means current directry
from . import views

urlpatterns = [
    path('',views.youtubers, name="youtubers"),
    # id is unique value given in admin section to each field
    path('<int:id>',views.youtubers_detail, name="youtubers_detail"),
    path('search',views.search, name="search"),

]
