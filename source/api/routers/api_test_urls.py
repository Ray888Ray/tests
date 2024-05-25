from django.urls import path
from api.views.api_test_views import api_test_list_view, api_test_detail_view, api_test_pass_view
from api.views.api_answer_views import api_answer_list_view
from api.views.api_question_views import api_question_list_view


urlpatterns = [
    path('answer_list/', api_answer_list_view, name='api_answer_list_view'),
    path('question_list/', api_question_list_view, name='api_question_list_view'),
    path('test_list/', api_test_list_view, name='test_list_view'),
    path('test/<int:test_set_id>/', api_test_detail_view, name='test_detail_view'),
    path('test/<int:test_set_id>/pass/', api_test_pass_view, name='test_pass_view'),
]
