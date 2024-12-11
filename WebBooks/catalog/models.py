from django.db import models

# Create your models here.
class myModelName(models.Model):

    my_field_name = models.CharField(max_length = 20, help_text = "Не более 20 символов")

    class Meta:
        ordering = ["-my_field_name"]

    def get_absolute_url(self):
        return reverse("model-detail-view", args=[str(self.id)])

    def __str__(self):
        return self.field_name
    
a_record = myModelName(my_field_name = "Книга о вкусной еде")

a_record.save()