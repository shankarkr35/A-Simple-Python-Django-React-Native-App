from rest_framework import serializers
from apps.sectors.models import Sector

class SectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sector
        fields = ['id', 'title', 'slug', 'status', 'create_date']