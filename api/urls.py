from django.conf.urls import url
from api import views

urlpatterns = [
    url(r'^add/', views.add),
    url(r'^query/', views.query),
    url(r'update/', views.update),
    url(r'delete/', views.delete),
    url(r'^(\d+)/', views.rest),
    url(r'^show/', views.show),
    url(r"view/", views.CustomView.as_view()),
    url(r'login/', views.login),
]
