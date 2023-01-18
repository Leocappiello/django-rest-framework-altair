from rest_framework import serializers
from .models import Costs

class CostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Costs
        fields = ('')
        read_only_fields = ('')