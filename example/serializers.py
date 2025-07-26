from .models import ExampleModel
from rest_framework import serializers

class ExampleSerializer (serializers.ModelSerializer) : 

    class Meta:
        model = ExampleModel
        fields = "__all__"