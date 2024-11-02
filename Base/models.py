from django.db import models

# Create your models here.

class Catagory (models.Model):

  name = models.CharField (max_length=70)
  discriptionsTwo = models.TextField (null=True, blank=True)

  def __str__(self) -> str:
    return self.name

class School_Deployment(models.Model):

  first_name = models.CharField (max_length=30)
  last_name = models.CharField (max_length=40)
  description = models.TextField()

  def __str__(self) -> str:
    return self.first_name + " " + self.last_name