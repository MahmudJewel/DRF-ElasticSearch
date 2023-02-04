from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect

from django_elasticsearch_dsl_drf.constants import (
    LOOKUP_FILTER_TERMS,
    LOOKUP_FILTER_RANGE,
    LOOKUP_FILTER_PREFIX,
    LOOKUP_FILTER_WILDCARD,
    LOOKUP_QUERY_IN,
    LOOKUP_QUERY_GT,
    LOOKUP_QUERY_GTE,
    LOOKUP_QUERY_LT,
    LOOKUP_QUERY_LTE,
    LOOKUP_QUERY_EXCLUDE,
)
from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend,
    IdsFilterBackend,
    OrderingFilterBackend,
    DefaultOrderingFilterBackend,
    SearchFilterBackend,
)
from django_elasticsearch_dsl_drf.viewsets import BaseDocumentViewSet
from django_elasticsearch_dsl_drf.pagination import PageNumberPagination

from .documents import BookDocument #, PublisherDocument
from .serializers import BookDocumentSerializer
# Create your views here.

def home(request):
    return HttpResponse('Home page')


# elastic documents 
class BookDocumentView(BaseDocumentViewSet):
    """The BookDocument view."""

    document = BookDocument
    serializer_class = BookDocumentSerializer
    pagination_class = PageNumberPagination
    lookup_field = 'id'
    fielddata = True
    filter_backends = [
        FilteringFilterBackend,
        IdsFilterBackend,
        OrderingFilterBackend,
        DefaultOrderingFilterBackend,
        SearchFilterBackend,
    ]
    # Define search fields
    search_fields = (
        'title',
        'description',
        'summary',
    )
    # Define filter fields
    # filter_fields = {
        # 'id': {
        #     'field': 'id',
        #     # Note, that we limit the lookups of id field in this example,
        #     # to `range`, `in`, `gt`, `gte`, `lt` and `lte` filters.
        #     'lookups': [
        #         LOOKUP_FILTER_RANGE,
        #         LOOKUP_QUERY_IN,
        #         LOOKUP_QUERY_GT,
        #         LOOKUP_QUERY_GTE,
        #         LOOKUP_QUERY_LT,
        #         LOOKUP_QUERY_LTE,
        #     ],
        # },
        # 'title': 'title.raw',
        # 'publisher': 'publisher.raw',
        # 'publication_date': 'publication_date',
        # 'state': 'state.raw',
        # 'isbn': 'isbn.raw',
        # 'price': {
        #     'field': 'price.raw',
        #     'lookups': [
        #         LOOKUP_FILTER_RANGE,
        #         LOOKUP_QUERY_GT,
        #         LOOKUP_QUERY_GTE,
        #         LOOKUP_QUERY_LT,
        #         LOOKUP_QUERY_LTE,
        #     ],
        # },
        # 'pages': {
        #     'field': 'pages',
        #     'lookups': [
        #         LOOKUP_FILTER_RANGE,
        #         LOOKUP_QUERY_GT,
        #         LOOKUP_QUERY_GTE,
        #         LOOKUP_QUERY_LT,
        #         LOOKUP_QUERY_LTE,
        #     ],
        # },
        # 'stock_count': {
        #     'field': 'stock_count',
        #     'lookups': [
        #         LOOKUP_FILTER_RANGE,
        #         LOOKUP_QUERY_GT,
        #         LOOKUP_QUERY_GTE,
        #         LOOKUP_QUERY_LT,
        #         LOOKUP_QUERY_LTE,
        #     ],
        # },
        # 'tags': {
        #     'field': 'tags',
        #     'lookups': [
        #         LOOKUP_FILTER_TERMS,
        #         LOOKUP_FILTER_PREFIX,
        #         LOOKUP_FILTER_WILDCARD,
        #         LOOKUP_QUERY_IN,
        #         LOOKUP_QUERY_EXCLUDE,
        #     ],
        # },
        # 'tags.raw': {
        #     'field': 'tags.raw',
        #     'lookups': [
        #         LOOKUP_FILTER_TERMS,
        #         LOOKUP_FILTER_PREFIX,
        #         LOOKUP_FILTER_WILDCARD,
        #         LOOKUP_QUERY_IN,
        #         LOOKUP_QUERY_EXCLUDE,
        #     ],
        # },

    # }
    filter_fields = {
        'title': 'title',
        'content': 'content',
        'publisher':'publisher',
        'publication_date':'publication_date',
        'state':'state',
        'isbn':'isbn',
        'price':'price',
        'pages':'pages',
        'stock_count':'stock_count',
        'tags':'tags'
    }

    # Define ordering fields
    ordering_fields = {
        'id': 'id',
        'title': 'title.raw', 
        'price': 'price.raw',
        'state': 'state.raw',
        'publication_date': 'publication_date',
    }
    # Specify default ordering
    ordering = ('id', 'title', 'price',)


