from django.urls import path
from .views import signup,login_view,logout_view,profile,edit_profile, delete_profile

urlpatterns = [
    path('signup/', signup, name="signup"),
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),
    path('<int:user_id>/profile/', profile, name='profile'),
    path('<int:user_id>/profile/edit/', edit_profile, name='edit_profile'),
    path('<int:user_id>/profile/delete/', delete_profile, name='delete_profile'),

]