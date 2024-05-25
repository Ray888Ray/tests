from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from webapp.models import Answer


def get_answer_data(answers):
    return [
        {'id': answer.id, 'text': answer.text, 'is_correct': answer.is_correct, 'question': answer.question_id}
        for answer in answers
    ]


# Список ответов
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def api_answer_list_view(request):
    answers = Answer.objects.all()
    answer_data = get_answer_data(answers)
    return Response({'answers': answer_data})


# Список ответов для определенного теста
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def api_test_answers_view(request, test_set_id):
    answers = Answer.objects.filter(question__test_set_id=test_set_id)
    answer_data = get_answer_data(answers)
    return Response({'answers': answer_data})
