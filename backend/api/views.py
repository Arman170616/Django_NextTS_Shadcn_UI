from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ToDo
from .serializers import ToDoSerializer

class ToDoListCreateView(APIView):
    # List all To-Dos or create a new one
    def get(self, request):
        todos = ToDo.objects.all()
        serializer = ToDoSerializer(todos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ToDoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ToDoDetailView(APIView):
    # Get, update, or delete a specific To-Do
    def get_object(self, pk):
        try:
            return ToDo.objects.get(pk=pk)
        except ToDo.DoesNotExist:
            return None

    def get(self, request, pk):
        todo = self.get_object(pk)
        if not todo:
            return Response({"error": "To-Do not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = ToDoSerializer(todo)
        return Response(serializer.data)

    def put(self, request, pk):
        todo = self.get_object(pk)
        if not todo:
            return Response({"error": "To-Do not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = ToDoSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        todo = self.get_object(pk)
        if not todo:
            return Response({"error": "To-Do not found"}, status=status.HTTP_404_NOT_FOUND)
        todo.delete()
        return Response({"message": "To-Do deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
