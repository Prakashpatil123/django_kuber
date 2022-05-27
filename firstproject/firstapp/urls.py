from django.urls import path
from .views import home_page, DemoView

urlpatterns = [
    path('home/',home_page),
    path('rest/',DemoView.as_view())
]
