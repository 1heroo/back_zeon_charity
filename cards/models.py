from django.db import models
from datetime import datetime
from django.utils.translation import gettext_lazy as _
from location_field.models.plain import PlainLocationField
from user.models import MyUser


class Category(models.Model):
    title = models.CharField(_('title'), db_column='title', max_length=100, blank=False)
    photo = models.ImageField(_('image'), null=True, blank=True, upload_to='images/')

    class Meta:
        db_table = 'category'
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.title


class Fund(models.Model):
    title = models.CharField(_('title'), db_column='title', max_length=100, blank=False)
    description = models.TextField(_('description'), db_column='description', max_length=1000, blank=False)
    photo = models.ImageField(_('photo'), null=True, blank=True, upload_to='images/')

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
        verbose_name = _('Fund')
        verbose_name_plural = _('Funds')

    def __str__(self):
        return self.title


class Card(models.Model):
    title = models.CharField(_('title'), db_column='title', max_length=100, blank=False)
    category = models.ForeignKey(
        _('category'),
        to=Category,
        related_name='category_list',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    description = models.TextField(_('description'), db_column='description', max_length=1000, blank=False)
    fund = models.ForeignKey(
        _('fund'),
        to=Fund,
        related_name='funds',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    target_amnt = models.FloatField(_('target_amnt'), db_column='target_amnt',blank=False, default=0)
    total_amnt = models.FloatField(_('total_amnt'), db_column='total_amnt',blank=False, default=0)
    photo = models.ImageField(_('image'), null=True, blank=True, upload_to='images/')
    deadline = models.DateTimeField(
        _('deadline'), 
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
        verbose_name = _('Card')
        verbose_name_plural = _('Cards')

    def __str__(self):
        return self.title


class CardImage(models.Model):
    photo = models.ImageField(_('image'), null=True, blank=True, upload_to='images/')
    card = models.ForeignKey(
        _('card'),
        to=Card,
        related_name='card_images',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return str(self.photo)

    class Meta:
        db_table = 'card_images'
        verbose_name = _('Card Image')
        verbose_name_plural = _('Card Images')


class Donations(models.Model):
    user = models.ForeignKey(
        _('user'),
        to=MyUser,
        related_name='users',
        on_delete=models.SET_NULL,
        null=True, blank=True
    )
    card = models.ForeignKey(
        _('card'),
        to=Card,
        related_name='donations',
        on_delete=models.SET_NULL,
        null=True, blank=True
    )
    donation_amnt = models.FloatField(_('donation_amnt'), db_column='donation_amnt',blank=False, default=0)
    payment_dt = models.DateTimeField(
        _('payment_dt'),
        default=datetime.now(),
        db_column='payment_dt',
        blank=True,
        null=True
    )
    region = models.CharField(_('region'), db_column='region', max_length=100, blank=True)

    class Meta:
        db_table = 'donation'
        verbose_name = _('Donation')
        verbose_name_plural = _('Donations')

class Volunteer(models.Model):
    title = models.CharField(_('title'), db_column='title', max_length=100, blank=False)
    description = models.TextField(_('description'), db_column='description', max_length=1000, blank=False)
    photo = models.ImageField(_('photo'), null=True, blank=True, upload_to='images/')
    city = models.CharField(_('city'), max_length=255)
    location = PlainLocationField(verbose_name=_('location'), based_fields=['city'], zoom=7)
    start_dt = models.DateTimeField(
        _('start_dt'), 
        db_column='start_dt',
        blank=True,
        null=True
    )
    end_dt = models.DateTimeField(
        _('end_dt'), 
        db_column='end_dt',
        blank=True,
        null=True
    )
    responsibility = models.TextField(_('responsibility'), db_column='responsibility', max_length=1000, blank=False)
    requirements = models.TextField(_('requirements'), db_column='requirements', max_length=1000, blank=False)

    email = models.

    class Meta:
        db_table = 'volunteer'
        verbose_name = _('Volunteer')
        verbose_name_plural = _('Volunteers')

    def __str__(self):
        return self.title