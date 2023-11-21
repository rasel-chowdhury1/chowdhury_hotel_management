from django.db import models
from django.contrib.auth.models import User

class Hotel(models.Model):
    REVIEW = (
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5')
    )
    hotel_name = models.CharField(max_length=100,unique=True)
    slug = models.CharField(max_length=100,unique=True)
    description = models.TextField()
    address = models.CharField(max_length=200)
    rating = models.CharField(max_length=30, choices=REVIEW)
    price = models.IntegerField()
    image = models.ImageField(upload_to='photos/hotel')
    is_available = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    # Add other fields like price, amenities, images, etc.

class Review(models.Model):
    REVIEW = (
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5')
    )
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.CharField(max_length=30, choices=REVIEW)
    comment = models.TextField()
    
    def __str__(self) -> str:
        return self.hotel.slug
    
