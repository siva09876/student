from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=50)
    roll_no=models.IntegerField()

    def __str__(self) -> str:
        return f'{self.name} {self.roll_no}'