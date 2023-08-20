from django.contrib import admin
from .models import Advert
from django.utils.html import format_html


# Register your models here.

class AdvertAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "description", "price", "auction", "date_of_creation", "date_of_update", 'get_image', "image"]
    list_filter = ["auction", "created_at"]
    actions = ["make_auctions_as_true", "make_auctions_as_false"]
    fieldsets = (
        ("общее", {
              'fields': ("title", "description", "user", "image")
        }),

        ("финансы", {
            'fields': ("price", "auction"),
            "classes": ['collapse']
        })
    )

    @admin.display(description='картинка')
    def get_image(self, obj):
        return format_html('<img src="{}", width=150, hight=100>', obj.image.url)


    @admin.action(description="Добавить возможность торга")
    def make_auctions_as_true(self, request, queuryset):
        queuryset.update(auction=True)

    @admin.action(description="Убрать возможность торга")
    def make_auctions_as_false(self, request, queuryset):
        queuryset.update(auction=False)

admin.site.register(Advert, AdvertAdmin)