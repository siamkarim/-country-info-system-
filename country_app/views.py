from rest_framework import viewsets, generics, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django.shortcuts import get_object_or_404
from .models import Country
from .serializers import CountrySerializer, CountryDetailSerializer, CountryCreateUpdateSerializer

class CountryViewSet(viewsets.ModelViewSet):
    """
    API endpoint for viewing and editing country data
    """
    queryset = Country.objects.all().order_by('name_common')
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return CountryCreateUpdateSerializer
        elif self.action == 'retrieve':
            return CountryDetailSerializer
        return CountrySerializer
    
    @action(detail=True, methods=['get'], url_path='same-region')
    def same_region(self, request, pk=None):
        """
        API endpoint to list countries in the same region as the specified country
        """
        country = self.get_object()
        if not country.region:
            return Response(
                {"detail": "This country does not have a specified region."},
                status=status.HTTP_404_NOT_FOUND
            )
        
        same_region_countries = Country.objects.filter(
            region=country.region
        ).exclude(cca2=country.cca2)
        
        page = self.paginate_queryset(same_region_countries)
        if page is not None:
            serializer = CountrySerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
            
        serializer = CountrySerializer(same_region_countries, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'], url_path='by-language/(?P<language>[^/.]+)')
    def by_language(self, request, language=None):
        """
        API endpoint to list countries that speak a specific language
        """
        # This is a bit complex since languages are stored in a JSONField
        # We need to filter countries where the provided language exists as a key in the languages dict
        countries_with_language = []
        
        for country in Country.objects.all():
            if country.languages and language in country.languages:
                countries_with_language.append(country)
        
        page = self.paginate_queryset(countries_with_language)
        if page is not None:
            serializer = CountrySerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
            
        serializer = CountrySerializer(countries_with_language, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'], url_path='search/(?P<search_term>[^/.]+)')
    def search(self, request, search_term=None):
        """
        API endpoint to search for countries by name (partial search supported)
        """
        if not search_term:
            return Response(
                {"detail": "Search term is required."},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        matching_countries = Country.objects.filter(name_common__icontains=search_term)
        
        page = self.paginate_queryset(matching_countries)
        if page is not None:
            serializer = CountrySerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
            
        serializer = CountrySerializer(matching_countries, many=True)
        return Response(serializer.data)