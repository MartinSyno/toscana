from django.db import models

# Create your models here.
class Message(models.Model):
    user_name = models.CharField(max_length=40)
    user_email = models.EmailField()
    user_message = models.TextField(max_length=500)

    pub_date = models.DateField(auto_now_add=True)
    is_processed = models.BooleanField(default=False)

    class Meta:
        ordering = ("pub_date",)

    def __str__(self):
        return f"{self.user_name} : {self.user_email} : {self.user_message[:20]}"