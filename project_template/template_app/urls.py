from django.urls import path, include
from template_app import views

# Template Tagging
app_name = 'template_app'

urlpatterns=[
    path('other/',views.other, name='other'),
    path('relative/',views.relative, name='relative'),
]
