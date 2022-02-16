from django.urls import path, include

from .views import account

urlpatterns = [

    # Accounts
    path(
        'account/',
        include([
            # telegram
            path('telegram_callback/', account.telegram_callback),

            # twitter
            path('twitter_auth/', account.twitter_auth),
            path('twitter_callback/', account.twitter_callback),

            # main
            path('logout/', account.logout),
        ]),
    ),
]
