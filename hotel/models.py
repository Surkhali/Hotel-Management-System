from django.db import models
class Guest(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()


class Room(models.Model):
    ROOM_TYPES = [
        ('SGL', 'Single'),
        ('DBL', 'Double'),
        ('STE', 'Suite'),
    ]
    STATUS_CHOICES = [
        ('AVL', 'Available'),
        ('BOK', 'Booked'),
        ('MNT', 'Maintenance'),
    ]
    


class Reservation(models.Model):
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Reservation {self.id} by {self.guest}"


class Payment(models.Model):
    PAYMENT_METHODS = [
        ('CRD', 'Credit Card'),
        ('CSH', 'Cash'),
        ('ONL', 'Online'),
    ]
    


class Staff(models.Model):
    ROLES = [
        ('MGR', 'Manager'),
        ('RCP', 'Receptionist'),
        ('HKP', 'Housekeeping'),
    ]
    
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    role = models.CharField(max_length=3, choices=ROLES)
    phone = models.CharField(max_length=15)
    email = models.EmailField()


class Service(models.Model):
    service_name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)


class ServiceRequest(models.Model):
    STATUS_CHOICES = [
        ('PND', 'Pending'),
        ('CMP', 'Completed'),
    ]
    
