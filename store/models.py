from django.db import models
import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save


# Create customer profile
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_modified = models.DateTimeField(User, auto_now_add=True)
    phone_number = models.CharField(max_length=20, blank=True)
    address_1 = models.CharField(max_length=180, blank=True)
    address_2 = models.CharField(max_length=180, blank=True)
    city = models.CharField(max_length=180, blank=True)
    region_or_state = models.CharField(max_length=180, blank=True)
    zipcode = models.CharField(max_length=180, blank=True)
    country = models.CharField(max_length=180, blank=True)
    old_cart = models.CharField(max_length=180, blank=True, null=True)

    def __str__(self):
        return self.user.username


# Create a user profile by default when user signs up
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()


# Automate the profile creation
post_save.connect(create_profile, sender=User)


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


# customer
class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# All of our product
class Product(models.Model):
    STATUS_CHOICES = [
        ('In Stock', 'In Stock'),
        ('Out of Stock', 'Out of Stock'),
        ('Pre-order', 'Pre-order')
    ]

    name = models.CharField(max_length=50)
    price = models.FloatField(default=0, max_length=13)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.TextField(default='', blank=True, null=True)
    product_details = models.TextField(default='', blank=True, null=True)
    image = models.ImageField(upload_to='uploads/product/')
    availability_status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='In Stock')
    expiration_date = models.DateField(blank=True, null=True)
    is_sale = models.BooleanField(default=False)
    sale_price = models.FloatField(default=0, max_length=13)

    def __str__(self):
        return self.name


# customer order
class Order(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('PROCESSING', 'Processing'),
        ('SHIPPED', 'Shipped'),
        ('DELIVERED', 'Delivered'),
        ('CANCELLED', 'Cancelled')
    ]
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    order_date = models.DateTimeField(datetime.datetime.today)
    phone = models.CharField(max_length=10, default='', blank=False)
    address = models.CharField(max_length=70, default='', blank=False)
    total_amount = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    payment_status = models.CharField(max_length=20, default='unpaid')

    def __str__(self):
        return f"Order {self.product} by {self.customer}"
