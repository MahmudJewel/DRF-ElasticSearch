from django.urls import path #, include
from .views import home, BookDocumentView

from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
books = router.register(r'books',
                        BookDocumentView,
                        basename='bookdocument')

urlpatterns = [
    path('',home, name='home'),
    # elastic search url 
    url(r'^', include(router.urls)),
]

