from django.shortcuts import render, redirect, get_object_or_404
from .models import Hotel, Room, Booking
from .forms import BookingForm

def hotel_list(request):
    hotels = Hotel.objects.all ()
    return render(request, 'hotel_list.html', {'hotels': hotels})

def hotel_detail(request, pk):
    hotel = get_object_or_404(Hotel, pk=pk)
    rooms = hotel.rooms.all()
    print(rooms)
    return render(request, 'hotel_detail.html', {'hotel': hotel, 'rooms': rooms})

def book_room(request, hotel_id, room_id):
    hotel = get_object_or_404(Hotel, pk=hotel_id)
    room = get_object_or_404(Room, pk=room_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.hotel = hotel
            booking.room = room
            booking.total_amount = room.price * (booking.check_out - booking.check_in).days
            booking.save()
            return redirect('booking_confirmation', booking_id=booking.id)
    else:
        form = BookingForm()
    return render(request, 'book_room.html', {'form': form, 'hotel': hotel, 'room': room})

def booking_confirmation(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id)
    return render(request, 'booking_confirmation.html', {'booking':booking})