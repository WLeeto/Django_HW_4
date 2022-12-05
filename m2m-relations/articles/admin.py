from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, Scope


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        for form in self.forms:
            # В form.cleaned_data будет словарь с данными
            # каждой отдельной формы, которые вы можете проверить
            if not form.cleaned_data['is_main']:
                # вызовом исключения ValidationError можно указать админке о наличие ошибки
                # таким образом объект не будет сохранен,
                # а пользователю выведется соответствующее сообщение об ошибке
                raise ValidationError('Хотябы один таг должен быть главным')
        return super().clean()  # вызываем базовый код переопределяемого метода


class ScopeInLine(admin.TabularInline):
    model = Scope
    extra = 0
    formset = ScopeInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    # list_display =['title', 'text', 'published_at', 'image']
    inlines = [ScopeInLine, ]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
