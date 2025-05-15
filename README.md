## Country Information System
    This Django application allows users to browse, search, and manage country information fetched from the REST Countries API.

### Features
    Fetch and store country data from REST Countries API
    RESTful API endpoints for country data manipulation
    Web interface for displaying and searching countries
    Authentication system to secure the application
    Interactive API documentation with Swagger and ReDoc
    
### Setup Instructions
### Prerequisites
    Python 3.8+
    pip (Python package manager)
    Git

### Installation Steps
Clone the repository:
```
git clone https://github.com/siamkarim/-country-info-system-.git
cd -country-info-system-
```
### Create and activate a virtual environment:
```
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```
### Install dependencies:
```
pip install -r requirements.txt

```
### Set up the database:

```
python manage.py makemigrations
python manage.py migrate

```

### Create a superuser for admin access:

```
python manage.py createsuperuser
```
### Fetch country data from the API:
```
python manage.py fetch_countries
```
### Run the development server:
```
python manage.py runserver

```
Access the application 
```
http://127.0.0.1:8000/
```
### Project Structure
country_info_system/
├── manage.py
├── country_project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── country_app/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   ├── views.py
│   ├── management/
│   │   └── commands/
│   │       └── fetch_countries.py
│   └── templates/
│       └── country_app/
│           ├── base.html
│           ├── country_list.html
│           ├── country_detail.html
│           └── login.html
└── requirements.txt

### API Endpoints

Endpoint	Method	Description
```
/api/countries/	GET	List all countries
/api/countries/	POST	Create a new country
/api/countries/<str:pk>/	GET	Get details of a specific country
/api/countries/<str:pk>/	PUT	Update a country's details
/api/countries/<str:pk>/	DELETE	Delete a country
/api/countries/<str:pk>/same-region/	GET	List countries in the same region
/api/countries/by-language/<str:language>/	GET	List countries that speak a specific language
/api/countries/search/<str:search_term>/	GET	Search for countries by name

````
API Documentation
The project includes interactive API documentation:

Swagger UI: Available at /swagger/
(http://127.0.0.1:8000/swagger/ when running locally)

ReDoc: Available at /redoc/ 
(http://127.0.0.1:8000/redoc/ when running locally)


