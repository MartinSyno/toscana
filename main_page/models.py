from django.db import models
# Create your models here.


# class SiteSettings(models.Model):
#     def save(self, *args, **kwargs):  # Чтобы запрещало создавать более 1 экземпляра этой модели.
#         if not self.pk and SiteSettings.objects.exists():
#             raise FileExistsError('Не можна створювати два файли налаштувань. Видаліть попередній спочатку.')
#         else:
#             return super(SiteSettings, self).save(*args, **kwargs)
#
#     phone = models.CharField(max_length=20)
#     address = models.CharField(max_length=30)
#     email = models.EmailField()
#     facebook_link = models.CharField(max_length=100)
#     instagram_link = models.CharField(max_length=100)
#     working_hours = models.CharField(max_length=30)
    # currency = models.CharField(max_length=10)
    # latest_product_amount_in_column = models.IntegerField()


class Banner(models.Model):
    name = models.CharField(max_length=30, db_index=True)
    photo = models.ImageField(upload_to="img/banner/%Y/%m/%d")
    is_visible = models.BooleanField(default=True)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name

# class Info(models.Model):
#     def get_file_name(self, filename):
#         ext = filename.strip().split(".")[-1]  # Узнать разширение файла (my_photo.jpg -> [ "my_photo", "jpg" ])
#         filename = f"{uuid4()}.{ext}"
#         return path.join("images/info", filename)
#
#     cafe_info = models.CharField(max_length=500, unique=True)
#     photo = models.ImageField(upload_to=get_file_name)
#     is_visible = models.BooleanField(default=True)
#
# class Team(models.Model):
#     def get_file_name(self, filename):
#         ext = filename.strip().split(".")[-1]  # Узнать разширение файла (my_photo.jpg -> [ "my_photo", "jpg" ])
#         filename = f"{uuid4()}.{ext}"
#         return path.join("images/team", filename)
#
#     team_info = models.CharField(max_length=500, unique=True)
#     photo = models.ImageField(upload_to=get_file_name)
#     is_visible = models.BooleanField(default=True)
#
# class Phone(models.Model):
#     phone = models.CharField(max_length=13, unique=True)
#     is_visible = models.BooleanField(default=True)
#
#     def __str__(self):
#         return f"{self.phone}"
#
# class Adress(models.Model):
#     city = models.CharField(max_length=20)
#     street = models.CharField(max_length=20)
#     home = models.CharField(max_length=5)
#     is_visible = models.BooleanField(default=True)
#
#     def __str__(self):
#         return f"{self.city}; {self.street}; {self.home}"
#
# class OpeningHours(models.Model):
#     day = models.CharField(max_length=10)
#     hours_start = models.CharField(max_length=5)
#     hours_end = models.CharField(max_length=5)
#
#     def __str__(self):
#         return f"{self.day} - {self.hours_start}-{self.hours_end}"
#
# class CafeInfo(models.Model):
#     adress_id = models.ForeignKey(Adress, on_delete=models.CASCADE)
#     phone_id = models.ForeignKey(Phone, on_delete=models.CASCADE)
#     openinghours_id = models.ForeignKey(OpeningHours, on_delete=models.CASCADE)
#
#
# class Message(models.Model):
#     user_name = models.CharField(max_length=40)
#     user_email = models.EmailField()
#     user_message = models.CharField(max_length=400)
#
#     pub_date = models.DateField(auto_now_add=True)
#     is_processed = models.BooleanField(default=False)
#
#     def __str__(self):
#         return f"{self.user_name} : {self.user_email} : {self.user_message[:20]}"