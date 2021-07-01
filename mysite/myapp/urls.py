from django.urls import path
from . import views
from .views import check, Choice, Category

app_name = 'myapp'
urlpatterns = [
    path('test/<int:category>/', views.test, name='test'),
    path('', views.index, name='index'),
    path('check/', check, name='check')

]
