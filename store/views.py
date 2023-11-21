from django.shortcuts import render,redirect,get_object_or_404
from .models import Hotel,Review
from .forms import ReviewForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q

# Create your views here.
def home(request):
    hotels = Hotel.objects.all()
    return render(request, 'hotel/hotel.html', {'hotels':hotels})

def hotel_details(request,hotel_id):
    single_hotel = Hotel.objects.get(id = hotel_id)
    hotel_review = Review.objects.filter(hotel__id = hotel_id)
    return render(request, 'hotel/hotel_details.html', {'hotel':single_hotel, 'reviews':hotel_review})


def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            hotels = Hotel.objects.order_by('-created_date').filter(Q(address__icontains=keyword) | Q(hotel_name__icontains=keyword))
            hotel_count = hotels.count()
    context = {
        'hotels' : hotels,
        'h_count': hotel_count
    }
    
    return render(request, 'hotel/hotel.html', context)


def submit_review(request, hotel_id):
    hotel = get_object_or_404(Hotel, id=hotel_id)
    
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.hotel = hotel
            review.save()
            return redirect('home')
    else:
        form = ReviewForm()

    return render(request, 'hotel/review.html', {'form': form})


def edit_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            # Redirect to the review detail page or a thank-you page
            return redirect('home')
    else:
        form = ReviewForm(instance=review)

    return render(request, 'hotel/review.html', {'form': form, 'review': review})

def delete_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    if request.method == 'POST':
        review.delete()
        # Redirect to the review list or a thank-you page
        return redirect('home')

    return render(request, 'hotel/delete.html', {'review': review})