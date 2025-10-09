from django.db import models
import uuid
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
CHAI_TYPE_CHOICE=[
        ('ML','Masala'),
        ('GR','Ginger'),
        ('TL','Tulsi'),
        ('KL','KIWI'),
        ('PL','Plain'),
        ('EL','Elaichi'),
    ]

class Chaivariety(models.Model):
    
    id= models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='images/')
    choices=models.CharField(max_length=2,choices=CHAI_TYPE_CHOICE)
    date=models.DateTimeField(default=timezone.now)
    description=models.TextField(blank=True)
    price=models.DecimalField(max_digits=6,decimal_places=2,null=True)
    
    def __str__(self):
        return f"<Chaivariety(name={self.name}, choices={self.choices}, date={self.date}, price={self.price})>"

# One to Many
class ChaiReview(models.Model):
    chai=models.ForeignKey(Chaivariety,on_delete=models.CASCADE,related_name='reviews')
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    ratings=models.IntegerField(null=True)
    comment=models.TextField(null=True,blank=True)
    date_added=models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        chai_name = getattr(self.chai, "name", None) or "Unknown Chai"
        user_name = getattr(self.user, "username", None) or "Anonymous"
        return f"{user_name} — {chai_name} ({self.ratings}⭐)"
    
class Store(models.Model):
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    chai_variety=models.ManyToManyField(Chaivariety,related_name='stores')
    
    def __str__(self):
        return f'<Store(name={self.name}, location={self.location})>'
    
class ChaiCertificate(models.Model):
    chai=models.OneToOneField(Chaivariety,on_delete=models.CASCADE,related_name='certificate')
    certificate_number=models.CharField(max_length=100)
    issue_date=models.DateField(default=timezone.now)
    valid_until=models.DateField(null=True,blank=True)
    def __str__(self):
        return f'<ChaiCertificate(chai={self.chai.name}, certificate_number={self.certificate_number}, issue_date={self.issue_date}, valid_until={self.valid_until})>'
    