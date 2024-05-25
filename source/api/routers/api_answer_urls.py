from django.urls import path
from api.views.api_answer_views import api_answer_list_view, api_test_answers_view


urlpatterns = [

    path('answer_list/', api_answer_list_view, name='api_answer_list_view'),
    path('<int:test_set_id>/answer_list/', api_test_answers_view, name='api_test_answers_view'),

]
