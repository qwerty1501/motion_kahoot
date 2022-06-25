from django.contrib import admin

from question.models import Question, Theme, MyUser, AdminTest

admin.site.register(Question)
admin.site.register(MyUser)
admin.site.register(AdminTest)


class QuestionInline(admin.TabularInline):
    model = Question
    extra = 0


@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    list_display = ['title_ru', 'pin_code']
    readonly_fields = ['pin_code', 'count_question']
    filter_horizontal = ['test_participants']
    inlines = [
        QuestionInline,
    ]

