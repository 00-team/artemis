from django.urls import path, include

from .views import account

urlpatterns = [

    # Accounts
    path(
        'account/',
        include([
            path('test/', account.test),
        ]),
    ),
]
