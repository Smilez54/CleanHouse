from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete,name='delete'),
    path('pricing/', views.pricing, name='pricing'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
]