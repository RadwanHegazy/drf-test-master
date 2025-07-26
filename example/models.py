from django.db import models


class ExampleModel (models.Model) : 
    name = models.CharField(max_length=225)
    number = models.IntegerField(
        null=True,
        blank=True,
        default=0
    )
    
    def __str__(self):
        return self.name
    