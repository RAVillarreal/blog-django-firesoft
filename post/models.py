from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class PostModel(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    image = models.ImageField(
    )
    pub_date = models.DateTimeField()
    body = RichTextField()

    def __str__(self):
        return self.title
