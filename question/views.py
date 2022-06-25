from rest_framework import generics
from rest_framework.viewsets import ModelViewSet

from question.models import MyUser, Question, Theme, AdminTest
from question.serializers import MyUserSerializer, QuestionSerializer, ThemeSerializer, AdminTestSerializer


class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer


class UserRetrieveDestroyAPIView(generics.RetrieveDestroyAPIView):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer


class QuestionAPIViewSet(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class ThemeAPIViewSet(ModelViewSet):
    queryset = Theme.objects.all()
    serializer_class = ThemeSerializer


class AdminTestAPILIST(generics.ListAPIView):
    queryset = AdminTest.objects.all()
    serializer_class = AdminTestSerializer