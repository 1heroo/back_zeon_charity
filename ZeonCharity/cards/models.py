from django.db import models
from datetime import datetime
from location_field.models.plain import PlainLocationField
from user.models import MyUser


class Category(models.Model):
    title = models.CharField(db_column='title', max_length=100, blank=False)
    photo = models.ImageField(null=True, blank=True, upload_to='images/')

    class Meta:
        db_table = 'category'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class Fund(models.Model):
    title = models.CharField(db_column='title', max_length=100, blank=False)
    description = models.TextField(db_column='description', max_length=1000, blank=False)
    photo = models.ImageField(null=True, blank=True, upload_to='images/')

    @property
    def total_raised(self):
        dontations_for_funds = self.funds.all()
        total_raised = sum([item.total for item in dontations_for_funds])
        return total_raised

    @property
    def total_helpers(self):
        dontations_for_funds = self.funds.all()
        total_helpers = sum([item.helpers_amnt for item in dontations_for_funds])
        return total_helpers
    
    class Meta:
        db_table = 'fund'
        verbose_name = 'Fund'
        verbose_name_plural = 'Funds'

    def __str__(self):
        return self.title


class Card(models.Model):
    title = models.CharField(db_column='title', max_length=100, blank=False)
    category = models.ForeignKey(
        Category,
        related_name='category_list',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    description = models.TextField(db_column='description', max_length=1000, blank=False)
    fund = models.ForeignKey(
        Fund,
        related_name='funds',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    target_amnt = models.FloatField(db_column='target_amnt',blank=False, default=0)
    total_amnt = models.FloatField(db_column='total_amnt',blank=False, default=0)
    photo = models.ImageField(null=True, blank=True, upload_to='images/')
    deadline = models.DateTimeField(
        db_column='deadline',
        blank=True,
        null=True
    )
    is_urgent = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)

    @property
    def total(self):
        donations = self.donations.all()
        total = sum([item.donation_amnt for item in donations])
        return total

    @property
    def helpers_amnt(self):
        donations = self.donations.all()
        helpers_amnt = sum([1 for item in donations])
        return helpers_amnt

    class Meta:
        db_table = 'card'
        verbose_name = 'Card'
        verbose_name_plural = 'Cards'

    def __str__(self):
        return self.title


class CardImage(models.Model):
    photo = models.ImageField(null=True, blank=True, upload_to='images/')
    card = models.ForeignKey(
        Card,
        related_name='card_images',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return str(self.photo)

    class Meta:
        db_table = 'card_images'
        verbose_name = 'Card Image'
        verbose_name_plural = 'Card Images'


class Donations(models.Model):
    user = models.ForeignKey(
        MyUser,
        related_name='users',
        on_delete=models.SET_NULL,
        null=True, blank=True
    )
    card = models.ForeignKey(
        Card,
        related_name='donations',
        on_delete=models.SET_NULL,
        null=True, blank=True
    )
    donation_amnt = models.FloatField(db_column='donation_amnt',blank=False, default=0)
    payment_dt = models.DateTimeField(
        default=datetime.now(),
        db_column='payment_dt',
        blank=True,
        null=True
    )
    region = models.CharField(db_column='region', max_length=100, blank=True)

    class Meta:
        db_table = 'donation'
        verbose_name = 'Donation'
        verbose_name_plural = 'Donations'


class Volunteer(models.Model):
    title = models.CharField(db_column='title', max_length=100, blank=False)
    description = models.TextField(db_column='description', max_length=1000, blank=False)
    photo = models.ImageField(null=True, blank=True, upload_to='images/')
    city = models.CharField(max_length=255)
    location = PlainLocationField(based_fields=['city'], zoom=7)
    start_dt = models.DateTimeField(
        db_column='start_dt',
        blank=True,
        null=True
    )
    end_dt = models.DateTimeField(
        db_column='end_dt',
        blank=True,
        null=True
    )
    responsibility = models.TextField(db_column='responsibility', max_length=1000, blank=False)
    requirements = models.TextField(db_column='requirements', max_length=1000, blank=False)

    class Meta:
        db_table = 'volunteer'
        verbose_name = 'Volunteer'
        verbose_name_plural = 'Volunteers'

    def __str__(self):
        return self.title