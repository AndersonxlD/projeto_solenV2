from django.urls import path
from .views import index, produtos, contato


urlpatterns = [
    path('', index, name='index'),
    path('produtos/',produtos, name='produtos'),
    path('contato/', contato, name='contato'),
]