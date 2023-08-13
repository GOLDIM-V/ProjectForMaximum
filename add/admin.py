from django.contrib import admin
from .models import Advert

# Register your models here.

class AdvertAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "description", "price", "auction", "date_of_creation", "date_of_update"]
    list_filter = ["auction", "created_at"]
    actions = ["make_auctions_as_true", "make_auctions_as_false"]
    fieldsets = (
        ("общее", {
              'fields': ("title", "description")
        }),

        ("финансы", {
            'fields': ("price", "auction"),
            "classes": ['collapse']
        })
    )
    

    @admin.action(description="Добавить возможность торга")
    def make_auctions_as_true(self, request, queuryset):
        queuryset.update(auction=True)

    @admin.action(description="Убрать возможность торга")
    def make_auctions_as_false(self, request, queuryset):
        queuryset.update(auction=False)

admin.site.register(Advert, AdvertAdmin)