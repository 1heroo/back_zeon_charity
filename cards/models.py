from django.db import models
from datetime import timedelta
from django.utils.translation import gettext_lazy as _
from location_field.models.plain import PlainLocationField
from user.models import MyUser
from django.utils import timezone
from parler.models import TranslatableModel, TranslatedFields


class Category(models.Model):
    title = models.CharField(_('title'), db_column='title', max_length=100, blank=False)
    photo = models.ImageField(_('image'), null=True, blank=True, upload_to='images/')

    class Meta:
        db_table = 'category'
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.title


class FundraisingCard(models.Model):
    title = models.CharField(_('title'), db_column='title', max_length=100, blank=False)
    category = models.ForeignKey(
        verbose_name=_('category'),
        to=Category,
        related_name='category_list',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    description = models.TextField(_('description'), db_column='description', max_length=1000, blank=False)
    target_amnt = models.FloatField(_('target_amnt'), db_column='target_amnt',blank=False, default=0)
    deadline = models.DateTimeField(
        _('deadline'),
        db_column='deadline',
        blank=True,
        null=True
    )
    contacts = models.TextField(_('contacts'), db_column='contacts', max_length=500, blank=True, null=True)

    is_approved = models.BooleanField(default=False)

    @property
    def is_active(self):
        if timezone.now() < self.deadline:
            return True
        return False

    @property
    def is_urgent(self):
        if self.is_active == False:
            return False

        if timezone.now() > self.deadline-timedelta(days=3):
            return True
        return False

    @property
    def total(self):
        donations = self.donations.all()
        total = sum([item.amount if item.payment_success else 0 for item in donations])
        return total

    # TO FIX
    @property
    def helpers_amnt(self):
        donations = self.donations.all()
        helpers_amnt = sum([1 for item in donations])
        return helpers_amnt

    class Meta:
        db_table = 'fundraising_card'
        verbose_name = _('Fundraising Card')
        verbose_name_plural = _('Fundraising Cards')

    def __str__(self):
        return self.title


# class Donations(models.Model):
#     user = models.ForeignKey(
#         verbose_name=_('user'),
#         to=MyUser,
#         related_name='users',
#         on_delete=models.SET_NULL,
#         null=True, blank=True
#     )
#     card = models.ForeignKey(
#         verbose_name=_('card'),
#         to=FundraisingCard,
#         related_name='donations',
#         on_delete=models.SET_NULL,
#         null=True, blank=True
#     )
#     donation_amnt = models.FloatField(_('donation_amnt'), db_column='donation_amnt',blank=False, default=0)
#     payment_dt = models.DateTimeField(
#         verbose_name=_('payment_dt'),
#         default=timezone.now,
#         db_column='payment_dt',
#         blank=True,
#         null=True
#     )
#
#     class Meta:
#         db_table = 'donation'
#         verbose_name = _('Donation')
#         verbose_name_plural = _('Donations')


class VolunteeringCard(models.Model):
    title = models.CharField(_('title'), db_column='title', max_length=100, blank=False)
    description = models.TextField(_('description'), db_column='description', max_length=5000, blank=False)
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

    contacts = models.TextField(_('contacts'), db_column='contacts', max_length=500, blank=False, null=False)

    @property
    def is_active(self):
        if timezone.now() < self.end_dt:
            return True
        return False

    class Meta:
        db_table = 'volunteering_card'
        verbose_name = _('Volunteering Card')
        verbose_name_plural = _('Volunteering Cards')

    def __str__(self):
        return self.title


class FundraisingCardImage(models.Model):
    photo = models.ImageField(_('image'), null=True, blank=True, upload_to='images/fundraising')
    card = models.ForeignKey(
        verbose_name=_('card'),
        to=FundraisingCard,
        related_name='fund_card_images',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return str(self.photo)

    class Meta:
        db_table = 'fun_card_images'
        verbose_name = _('Fundraising Card Image')
        verbose_name_plural = _('Fundraising Card Images')


class VolunteeringCardImage(models.Model):
    photo = models.ImageField(_('image'), null=True, blank=True, upload_to='images/volunteering/')
    card = models.ForeignKey(
        verbose_name=_('card'),
        to=VolunteeringCard,
        related_name='vol_card_images',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return str(self.photo)

    class Meta:
        db_table = 'vol_card_images'
        verbose_name = _('Volunteering Card Image')
        verbose_name_plural = _('Volunteering Card Images')


class VolunteeringCardDocument(models.Model):
    document = models.FileField(upload_to='documents/')
    card = models.ForeignKey(
        verbose_name=_('card'),
        to=VolunteeringCard,
        related_name='card_documents',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return str(self.document)

    class Meta:
        db_table = 'card_docs'
        verbose_name = _('Volunteering Card Document')
        verbose_name_plural = _('Volunteering Card Documents')


class VolunteeringCardLocation(models.Model):
    location = PlainLocationField(verbose_name=_('location'), based_fields=['city'], zoom=7)
    card = models.ForeignKey(
        verbose_name=_('card'),
        to=VolunteeringCard,
        related_name='card_images',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return str(self.location)

    class Meta:
        db_table = 'card_locations'
        verbose_name = _('Volunteering Card Location')
        verbose_name_plural = _('Volunteering Card Locations')