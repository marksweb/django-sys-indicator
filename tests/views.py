from django.http import HttpResponse


def home(request):
    """Simple view for testing"""
    return HttpResponse("<html><head></head><body>Hello world!</body></html>")
