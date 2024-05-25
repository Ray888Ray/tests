from django.urls import path, include


urlpatterns = [
    path('v1/', include('api.routers.api_test_urls')),
    path('auth/v1/', include('api.routers.api_authentication_urls')),
    path('v1/', include('api.routers.api_question_urls')),
    path('v1/', include('api.routers.api_answer_urls')),
]
