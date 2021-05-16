from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):

    name = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(db_index=True)
    photo = models.ImageField(upload_to="img/category/%Y/%m/%d")
    category_ordered = models.IntegerField(unique=True)
    is_visible = models.BooleanField(default=True)

    class Meta:
        ordering = ("category_ordered",)
        index_together = (("id", "slug"),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("shop:category_info_page", args=[self.id, self.slug])

class Furniture(models.Model):

    name = models.CharField(max_length=30, db_index=True)
    slug = models.SlugField(db_index=True)
    # furniture_color =
    photo = models.ImageField(upload_to="img/furniture/%Y/%m/%d")
    furniture_ordered = models.IntegerField()
    is_visible = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    old_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    discount = models.IntegerField(blank=True, null=True)
    available = models.BooleanField(default=True)
    desc = models.TextField(max_length=500)
    size = models.CharField(max_length=30)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)#related_name='furnitures_of_category')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("furniture_ordered",)
        index_together = (("id", "slug"),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("shop:furniture_info_page", args=[self.category.id, self.category.slug, self.id, self.slug])

# class FurnitureColors(models.Model):
#     furniture_group_of_colors = models.CharField(max_length=30, unique=True)

class Photos(models.Model):
    furniture = models.ForeignKey(Furniture, default=None, related_name='photos', on_delete=models.DO_NOTHING)
    photo = models.ImageField(upload_to='img/furniture/%Y/%m/%d', blank=True)
