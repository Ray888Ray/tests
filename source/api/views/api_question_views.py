from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from webapp.models import Question, TestSet


def get_question_data(questions):
    return [{'id': question.id, 'text': question.text, 'photo': question.photo.url if question.photo else None,
              'audio': question.audio.url if question.audio else None, 'test_set': question.test_set_id} for
             question in questions]


# Список вопросов
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def api_question_list_view(request):
    questions = Question.objects.all()
    question_data = get_question_data(questions)
    return Response({'questions': question_data})


# Список вопросов для определенного теста
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def api_test_question_view(request, test_set_id):
    test_set = get_object_or_404(TestSet, pk=test_set_id)
    questions = Question.objects.filter(test_set=test_set)
    question_data = get_question_data(questions)
    return Response({'questions': question_data})