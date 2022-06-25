from rest_framework.serializers import ModelSerializer

from question.models import Question, MyUser, Theme, AdminTest


class QuestionSerializer(ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class MyUserSerializer(ModelSerializer):
    class Meta:
        model = MyUser
        fields = '__all__'


class ThemeSerializer(ModelSerializer):
    class Meta:
        model = Theme
        fields = '__all__'


class AdminTestSerializer(ModelSerializer):
    class Meta:
        model = AdminTest
        fields = '__all__'
