from django.contrib import admin
from .models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'photo')

admin.site.register(Category, CategoryAdmin)


class CardInline(admin.TabularInline):
    model = CardImage
    extra = 0
    max_num = 8
 

class CardAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'category',
        'description',
        'target_amnt',
        'total_amnt',
        'photo',
        'deadline',
        'is_urgent', 
        'is_approved',
        'total'
    )
    inlines = [
        CardInline,
    ]

admin.site.register(Card, CardAdmin)


class DonationsAdmin(admin.ModelAdmin):
    list_display = (
        'user_id',
        'card',
        'donation_amnt',
        'payment_dt'
    )

admin.site.register(Donations, DonationsAdmin)


class FundAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'photo',
        'total_helpers',
        'total_raised'
    )

admin.site.register(Fund, FundAdmin)
