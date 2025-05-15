import requests
from django.core.management.base import BaseCommand
from country_app.models import Country
import json
import logging

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = 'Fetch countries data from REST Countries API and store in the database'

    def handle(self, *args, **options):
        self.stdout.write('Fetching countries data...')
        
        url = 'https://restcountries.com/v3.1/all'
        
        try:
            response = requests.get(url)
            response.raise_for_status() 
            
            countries_data = response.json()
            self.stdout.write(f'Successfully fetched data for {len(countries_data)} countries')
            
            # Counter for created and updated records
            created_count = 0
            updated_count = 0
            
            for country_data in countries_data:
                try:
                    # Extract required data
                    cca2 = country_data.get('cca2')
                    if not cca2:
                        self.stdout.write(self.style.WARNING(f'Skipping country without cca2 code'))
                        continue
                    
                    # Get or create the country object
                    country, created = Country.objects.get_or_create(cca2=cca2)
                    
                    # Update country data
                    country.name_common = country_data.get('name', {}).get('common', '')
                    country.name_official = country_data.get('name', {}).get('official', '')
                    country.capital = country_data.get('capital', [])
                    country.region = country_data.get('region', '')
                    country.subregion = country_data.get('subregion', '')
                    country.population = country_data.get('population', 0)
                    country.languages = country_data.get('languages', {})
                    country.timezones = country_data.get('timezones', [])
                    country.flags = country_data.get('flags', {})
                    country.latlng = country_data.get('latlng', [])
                    country.borders = country_data.get('borders', [])
                    country.currencies = country_data.get('currencies', {})
                    country.continents = country_data.get('continents', [])
                    
                    # Store the raw data for future use
                    country.raw_data = country_data
                    
                    # Save the country object
                    country.save()
                    
                    if created:
                        created_count += 1
                    else:
                        updated_count += 1
                
                except Exception as e:
                    self.stdout.write(
                        self.style.ERROR(f'Error processing country {country_data.get("name", {}).get("common", "Unknown")}: {str(e)}')
                    )
            
            self.stdout.write(
                self.style.SUCCESS(f'Successfully processed {created_count} new and {updated_count} existing countries')
            )
            
        except requests.exceptions.RequestException as e:
            self.stdout.write(self.style.ERROR(f'Error fetching data: {str(e)}'))
        except json.JSONDecodeError:
            self.stdout.write(self.style.ERROR('Error decoding JSON response'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Unexpected error: {str(e)}'))