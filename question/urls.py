from django.urls import path, include

from rest_framework.routers import DefaultRouter

from question.views import UserListCreateAPIView, QuestionAPIViewSet, ThemeAPIViewSet, \
    UserRetrieveDestroyAPIView, AdminTestAPILIST

router = DefaultRouter()
router.register('question', QuestionAPIViewSet)
router.register('theme', ThemeAPIViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('user/', UserListCreateAPIView.as_view(), name='user'),
    path('user/detail/<int:pk>', UserRetrieveDestroyAPIView.as_view(), name='user_detail'),
    path('admintest/', AdminTestAPILIST.as_view(), name='admintest'),


]
