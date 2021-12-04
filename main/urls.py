from django.urls import path
from .views import index, other_page, BBLoginView, profile, BBLogoutView, ChangeUserInfoView, BBPasswordChangeView, RegisterDoneView, RegisterUserView, user_activate, DeleteUserView, by_rubric

app_name = 'main'
urlpatterns = [
    path('', index, name='index'),
    path('accounts/profile/delete/', DeleteUserView.as_view (), name='profile_delete'),
    path('accounts/register/асtivate/<str:sign>/', user_activate, name='register_activate'),
    path('acoounts/register/done/', RegisterDoneView.as_view(), name='register_done'), 
    path('acoounts/register/', RegisterUserView.as_view(), name='register'),
    path('accounts/password/change/', BBPasswordChangeView.as_view(), name='password_change'),
    path('accounts/profile/change/', ChangeUserInfoView.as_view(), name='profile_change'),
    path('accounts/login/', BBLoginView.as_view(), name='login'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/logout/', BBLogoutView.as_view(), name='logout'),
    path('<int:pk>/', by_rubric, name='by_rubric'),
    path('<str:page>/', other_page, name='other'),
]