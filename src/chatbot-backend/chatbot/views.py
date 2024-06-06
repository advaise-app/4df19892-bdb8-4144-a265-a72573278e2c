from rest_framework.decorators import api_view
from rest_framework.response import Response
from .llamaindex_utils import generate_answer


@api_view(['POST'])
def answer_query(request):
    query = request.data.get('query')
    if query:
        answer_dict = generate_answer(query)
        return Response(answer_dict)
    else:
        return Response({'error': 'No query provided'}, status=400)
