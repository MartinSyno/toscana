from django.db import models
# Create your models here.


class SiteSettings(models.Model):
    # def save(self, *args, **kwargs):  # Чтобы запрещало создавать более 1 экземпляра этой модели.
    #     if self.pk and SiteSettings.objects.exists():
    #         raise FileExistsError('Не можна створювати два файли налаштувань. Видаліть попередній спочатку.')
    #     else:
    #         return super(SiteSettings, self).save(*args, **kwargs)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=30)
    email = models.EmailField()
    facebook_link = models.CharField(max_length=100)
    instagram_link = models.CharField(max_length=100)
    working_hours = models.CharField(max_length=30)
    # currency = models.CharField(max_length=10)
    latest_product_amount_in_column = models.IntegerField()


class Banner(models.Model):
    name = models.CharField(max_length=30, db_index=True)
    photo = models.ImageField(upload_to="img/banner")
    is_visible = models.BooleanField(default=True)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name