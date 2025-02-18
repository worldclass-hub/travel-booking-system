from django.shortcuts import render, redirect
from .models import Booking
from .forms import BookingForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def create_booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user  # Assign the logged-in user
            booking.save()
            messages.success(request, "Your booking was successful!")
            return redirect('my_bookings')  # Redirect to user's bookings page
    else:
        form = BookingForm()

    return render(request, 'bookings/create_booking.html', {'form': form})



@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user)  # Get bookings for the logged-in user
    return render(request, 'bookings/my_bookings.html', {'bookings': bookings})
