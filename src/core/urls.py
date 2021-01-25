from django.urls import path
from core import views

app_name = 'user'

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
    path('login/', views.UserLoginApiView.as_view(), name='token'),
    path('me/', views.RetrieveUserView.as_view(), name='me'),
]
