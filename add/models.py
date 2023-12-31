from django.contrib import admin
from django.db import models
from django.utils.html import format_html
from django.contrib.auth import get_user_model

user = get_user_model()

class Advert(models.Model):
    title = models.CharField("Заголовок", max_length=128)
    description = models.TextField("Описание")
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    auction = models.BooleanField("Торг", help_text="Отметьте, если торг уместен")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(user, verbose_name="Пользователь", on_delete=models.CASCADE)
    image = models.ImageField("Изображение", upload_to="adverts/", default="adverts/adv.png")

    @admin.display(description='Дата создания')
    def date_of_creation(self):
        from django.utils import timezone
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime("%H:%M:%S")
            return format_html(
                '<span style="color: green; font-weight: bold"> Сегодня в {}</span>', created_time
            )
        return self.created_at.time().strftime("%d.%m.%Y в %H:%M:%S")
    

    @admin.display(description='Дата обновления')
    def date_of_update(self):
        from django.utils import timezone
        if self.updated_at.date() == timezone.now().date():
            updated_time = self.updated_at.time().strftime("%H:%M:%S")
            return format_html(
                '<span style="color: green; font-weight: bold"> Сегодня в {}</span>', updated_time
            )
        return self.updated_at.time().strftime("%d.%m.%Y в %H:%M:%S")

    def __str__(self):     
        return f"Advertisement(id={self.pk}, title={self.title}, price={self.price})"
    
    class Meta:
       db_table = 'advertisements'
