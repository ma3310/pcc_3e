from django.urls import path
from .views import homepage_view
from .views import HomepageView
from .views import AboutView

urlpatterns = [
    # Bind function to path and name it.
    path('', homepage_view, name='homepage-function'),

    # define http://domain/class, no leading / is required.
    path('homepage-class', HomepageView.as_view(), name='homepage-class'),
    path('about', AboutView.as_view(), name='about-class'),
]
