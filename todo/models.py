from django.db import models

class Task(models.Model):
    name=models.CharField(max_length=255,null=False)
    phone_number=models.TextField()
    created=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
