from django.urls import path
from .views import hotel_list,hotel_detail,book_room,booking_confirmation

urlpatterns = [
    path('', hotel_list, name='hotel_list'),
    path('<int:pk>/', hotel_detail, name='hotel_detail'),
    path('<int:hotel_id>/room/<int:room_id>/book/', book_room, name='book_room'),
    path('booking/<int:booking_id>/confirmation/', booking_confirmation, name='booking_confirmation'),
] 