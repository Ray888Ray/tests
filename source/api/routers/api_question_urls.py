from django.urls import path
from api.views.api_question_views import api_question_list_view, api_test_question_view


urlpatterns = [

    path('question_list/', api_question_list_view, name='api_question_list_view'),
    path('<int:test_set_id>/question_list/', api_test_question_view, name='api_test_question_view'),

]
