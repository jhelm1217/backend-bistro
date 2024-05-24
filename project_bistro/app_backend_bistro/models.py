from django.db import models

# Create your models here.

class MenuItem(models.Model):
    cuisine_choices = [
        ('Italian', 'Italian'),
        ('Mexican', 'Mexican'),
        ('Southern', 'Southern'),
        ('American', 'American'),
        ('Asian', 'Asian'),
        ('Mediterranean', 'Mediaterranean'),
        ('International', 'International')
    ] # need to put my cusines types

    category_choices = [
        ('Drink', 'Drink'),
        ('Breakfast', 'Breakfast'),
        ('Appetizer', 'Appetizer'),
        ('Lunch', 'Lunch'),
        ('Dinner', 'Dinner')
    ]# need to put my categories for my cuisines

    cuisine = models.CharField(choices=cuisine_choices, max_length=200, default='Italian')
    title = models.CharField(max_length=200)
    description = models.TextField() 
    category = models.CharField(choices=category_choices, max_length=200, default='Drink')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    # img

    def __str__(self):
        return self.title

class Customer(models.Model):
    name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=12)


    def __str__(self):
        return self.name



class Order(models.Model):
    status_choices = [
        ('Pending', 'Order Pending'),
        ('Completed', 'Order Completed'),
        ('Canceled', 'Order Canceled')
    ]

    customer_name = models.CharField(max_length=200)
    item = models.ManyToManyField(MenuItem, through='OrderItem') #grab info from OrderItem model
    status = models.CharField(choices=status_choices, max_length=20, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'Customer Order {self.id} - {self.customer_name}'

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    menu_item = models.ForeignKey('MenuItem', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.menu_item.title} (x{self.quantity})'



class Driver(models.Model):
    name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=12)
    vehicle_make = models.CharField(max_length=30)
    license_plate_number = models.CharField(max_length=10)


    def __str__(self):
        return self.name



class Review(models.Model):
    rating_choices = [
        (1, '1 Star'),
        (2, '2 Stars'),
        (3, '3 Stars'),
        (4, '4 Stars'),
        (5, '5 Stars')
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=rating_choices)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
       return f"Review from {self.customer.name} for {self.driver}"