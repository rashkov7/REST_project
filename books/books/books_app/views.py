from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status, permissions, response
from rest_framework.views import APIView
from rest_framework import generics

from books.books_app.models import BookModel
from books.books_app.serializers import BookSerializer


class ListBookView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        books = BookModel.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response({"all books": serializer.data})

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DetailsAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = BookSerializer
    lookup_field = "id"

    def get_queryset(self):
        query = BookModel.objects.filter(author=self.request.user)
        return query


class DetailsView(APIView):
    def get(self, request, pk):
        book = get_object_or_404(BookModel, id=pk)
        serializer = BookSerializer(book)
        return Response({"Book": serializer.data})

    def put(self, request, pk):
        book = get_object_or_404(BookModel, id=pk)
        serializer = BookSerializer(book, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        book = get_object_or_404(BookModel, id=pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AuthorDashboardAPIView(APIView):

    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = BookSerializer

    def get(self, request):
        user = request.user
        books = BookModel.objects.filter(author=user)
        serializer = BookSerializer(books, many=True)
        return response.Response({"all books": serializer.data})

    def post(self,request):
        request.data['user'] = request.user
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response({"book created":serializer.data},status.HTTP_201_CREATED)
        return response.Response({"errors":serializer.errors},status.HTTP_400_BAD_REQUEST)

