from django.db import models

# Create your models here.

class School_Deployment(models.Model):

  first_name = models.CharField (max_length=30)
  last_name = models.CharField (max_length=40)
  image = models.ImageField(upload_to='photo/')
  description = models.TextField()

  def __str__(self) -> str:
    return self.first_name + " " + self.last_name