from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Country

@login_required
def country_list(request):
    """
    View to display the country list with pagination and search functionality
    """
    query = request.GET.get('query', '')
    countries = Country.objects.all().order_by('name_common')
    
    if query:
        countries = countries.filter(
            Q(name_common__icontains=query) | 
            Q(name_official__icontains=query) | 
            Q(cca2__icontains=query)
        )
    
    paginator = Paginator(countries, 20)  # Show 20 countries per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'query': query,
    }
    
    return render(request, 'country_app/country_list.html', context)

@login_required
def country_detail(request, country_id):
    """
    View to display detailed information about a specific country
    """
    country = get_object_or_404(Country, cca2=country_id)
    
    # Get same region countries
    same_region_countries = Country.objects.filter(
        region=country.region
    ).exclude(cca2=country.cca2)[:5]  # Limit to 5 countries
    
    # Get languages
    languages = country.languages or {}
    
    context = {
        'country': country,
        'same_region_countries': same_region_countries,
        'languages': languages,
    }
    
    return render(request, 'country_app/country_detail.html', context)