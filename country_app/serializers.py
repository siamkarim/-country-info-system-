from rest_framework import serializers
from .models import Country

class CountrySerializer(serializers.ModelSerializer):
    """
    Serializer for the Country model
    """
    class Meta:
        model = Country
        fields = [
            'cca2', 'name_common', 'name_official', 'capital', 
            'region', 'subregion', 'population', 'languages', 
            'timezones', 'flags', 'latlng', 'borders', 
            'currencies', 'continents'
        ]

class CountryDetailSerializer(serializers.ModelSerializer):
    """
    Detailed serializer for the Country model including all fields
    """
    class Meta:
        model = Country
        exclude = ['raw_data'] 

class CountryCreateUpdateSerializer(serializers.ModelSerializer):
    """
    Serializer for creating and updating Country objects
    """
    class Meta:
        model = Country
        fields = [
            'cca2', 'name_common', 'name_official', 'capital', 
            'region', 'subregion', 'population', 'languages', 
            'timezones', 'flags', 'latlng', 'borders', 
            'currencies', 'continents'
        ]
