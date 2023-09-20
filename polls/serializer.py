from rest_framework.serializers import ModelSerializer
from .models import UniversityModel

class UniversitySer(ModelSerializer):
    class Meta:
        model = UniversityModel
        fields = ('__all__')

        