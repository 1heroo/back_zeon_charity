from django.contrib import admin
from .models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'photo')


admin.site.register(Category, CategoryAdmin)


class FundraisingImageInline(admin.TabularInline):
    model = FundraisingCardImage
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
        FundraisingImageInline,
    ]


admin.site.register(FundraisingCard, FundraisingCardAdmin)


class VolunteeringImageInline(admin.TabularInline):
    model = VolunteeringCardImage
    extra = 0
    max_num = 8


class VolunteeringDocumentInline(admin.TabularInline):
    model = VolunteeringCardDocument
    extra = 0
    max_num = 10


class VolunteeringLocationInline(admin.TabularInline):
    model = VolunteeringCardLocation
    extra = 0
    max_num = 10


class VolunteeringCardAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'description',
        'start_dt',
        'end_dt',
        'contacts',
        'is_active'

    )
    inlines = [
        VolunteeringImageInline,
        VolunteeringDocumentInline,
        VolunteeringLocationInline
    ]


admin.site.register(VolunteeringCard, VolunteeringCardAdmin)


class DonationsAdmin(admin.ModelAdmin):
    list_display = (
        'user_id',
        'card',
        'donation_amnt',
        'payment_dt',
    )


admin.site.register(CardApplyModel)
