import endpoints as google_cloud_endpoints
from ferris3.discovery import discover_api_services, discover_webapp2_routes
from ferris3 import endpoints

# APIs

endpoints.add('app/default-endpoint.yaml', default=True)

API_CLASSES = discover_api_services()
API_APPLICATION = google_cloud_endpoints.api_server(API_CLASSES)


# WSGI handlers
import webapp2

WSGI_ROUTES = discover_webapp2_routes()
WSGI_APPLICATION = webapp2.WSGIApplication(WSGI_ROUTES)
