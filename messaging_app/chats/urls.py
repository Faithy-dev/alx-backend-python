from django.urls import path, include

urlpatterns = [
    # Include API routes from chats app
    path('api/', include('messaging_app.chats.urls')),

    # Include DRF's login/logout endpoints
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
