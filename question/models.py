from random import randint

from django.db import models


class Theme(models.Model):
    title_ru = models.CharField(max_length=100, verbose_name="Название теста на русском", unique=True)
    title_ky = models.CharField(max_length=100, verbose_name="Название теста на кыргызском", blank=True)
    pin_code = models.BigIntegerField(verbose_name='Пин код', blank=True, unique=True)
    count_question = models.PositiveIntegerField(verbose_name='Количество вопросов', default=0)
    is_start = models.BooleanField(verbose_name='Тест начался?', )
    test_participants = models.ManyToManyField('MyUser', verbose_name='Участники', null=True, blank=True)

    def __str__(self):
        return f'{self.title_ru} | {self.title_ky}'

    def save(self, *args, **kwargs):
        '''Переопределим метод save()'''
        while True:
            '''Даем пин код который нет ни в одном тесте! Адико Гений :)'''
            pin = randint(1000000, 9999999)

            if pin not in [i.pin_code for i in Theme.objects.all()]:
                '''Если сгенерированный пин нету в пин кодс'''
                self.pin_code = pin
                self.count_question = Question.objects.all().filter(theme=self).count()
                super().save(*args, **kwargs)
                break

    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'


class Question(models.Model):
    OPTION = ((1, 1), (2, 2), (3, 3), (4, 4))
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE, verbose_name='Тема')
    image = models.ImageField(verbose_name='Фото вопроса(необязательно)', blank=True)

    question_ru = models.TextField(verbose_name='Вопрос на русском')
    question_ky = models.TextField(verbose_name='Вопрос на кыргызском', blank=True)

    option_1_ru = models.CharField(max_length=250, verbose_name='1-Вариант на русском')
    option_1_ky = models.CharField(max_length=250, verbose_name='1-Вариант на кыргызском', blank=True)
    option_2_ru = models.CharField(max_length=250, verbose_name='2-Вариант на русском')
    option_2_ky = models.CharField(max_length=250, verbose_name='2-Вариант на кыргызском', blank=True)
    option_3_ru = models.CharField(max_length=250, verbose_name='3-Вариант на русском', blank=True)
    option_3_ky = models.CharField(max_length=250, verbose_name='3-Вариант на кыргызском', blank=True)
    option_4_ru = models.CharField(max_length=250, verbose_name='4-Вариант на русском', blank=True)
    option_4_ky = models.CharField(max_length=250, verbose_name='4-Вариант на кыргызском', blank=True)

    correct_answer = models.PositiveIntegerField(choices=OPTION, verbose_name='Правильный вариант')

    time_second = models.PositiveIntegerField(default=30, verbose_name='Время в секундах')

    point = models.PositiveIntegerField(default=1000, verbose_name='Очко')

    def __str__(self):
        return f'{self.question_ru[:20]}...'

    def save(self, *args, **kwargs):
        '''Переопределим метод save()'''
        theme = Theme.objects.get(pk=self.theme.pk)
        theme.count_question = Question.objects.all().filter(theme=theme).count()
        # когда сохраняю, Пин код теста меняется!!!
        theme.save()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class MyUser(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя', unique=True)
    pin_code = models.BigIntegerField(verbose_name='Пин код теста')
    point = models.PositiveIntegerField(default=0, verbose_name='Очко')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        '''Переопределим метод save()'''
        if self.pin_code in [i.pin_code for i in Theme.objects.all()]:
            '''Если введенный пин код есть то добавить в тест'''
            theme = Theme.objects.get(pin_code=self.pin_code)
            super().save(*args, **kwargs)
            theme.test_participants.add(self)

    class Meta:
        verbose_name = 'Игрок'
        verbose_name_plural = 'Игроки'


class AdminTest(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=25)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Админ'
        verbose_name_plural = 'Админы'