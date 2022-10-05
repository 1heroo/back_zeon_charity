from django.contrib import admin
from .models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'photo')

admin.site.register(Category, CategoryAdmin)


class CardInline(admin.TabularInline):
    model = CardImage
    extra = 0
    max_num = 8
 

class FundraisingCardAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'category',
        'description',
        'target_amnt',
        'total',
        'deadline',
        'is_urgent', 
        'is_approved',
        'is_active'
    )
    inlines = [
        CardInline,
    ]

admin.site.register(FundraisingCard, FundraisingCardAdmin)

class VolunteeringCardAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'description',
        'location',
        'start_dt',
        'end_dt',
        'responsibility', 
        'requirements',
        'contacts',
        'is_active'
    )

admin.site.register(VolunteeringCard, VolunteeringCardAdmin)


class DonationsAdmin(admin.ModelAdmin):
    list_display = (
        'user_id',
        'card',
        'donation_amnt',
        'payment_dt',
    )

admin.site.register(Donations, DonationsAdmin)
