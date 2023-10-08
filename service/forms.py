import calendar

from django import forms

from client.forms import StyleFormMixin
from service.models import NewsletterSettings, NewsletterMessage, LogsNewsletter
from client.models import Client


class NewsletterSettingsForm(StyleFormMixin, forms.ModelForm):
    """Форма для создания модели NewsletterSettings """
    class Meta:
        model = NewsletterSettings
        fields = ['newsletter_start', 'newsletter_finish', 'frequency']
        widgets = {
            'newsletter_start': forms.SelectDateWidget(empty_label=("Выберите год", "Выберите месяц", "Выберите день")),
            'newsletter_finish': forms.SelectDateWidget(empty_label=("Выберите год", "Выберите месяц", "Выберите день")),
        }


class NewsletterMessageForm(StyleFormMixin, forms.ModelForm):
    """Форма для создания модели NewsletterMessage """
    class Meta:
        model = NewsletterMessage
        fields = '__all__'

class LogsNewsletterForm(StyleFormMixin, forms.ModelForm):
    """ Форма для создания модели LogsNewsletter """
    class Meta:
        model = LogsNewsletter
        fields = '__all__'

# class NewsletterSettingsForm(forms.ModelForm):
#     class Meta:
#         model = NewsletterSettings
#         fields = ['newsletter_month_start', 'newsletter_month_finish', 'frequency', 'status',]
#         # widgets = {
#         #     'to_email': forms.CheckboxSelectMultiple
#         # }
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['to_email'].queryset = Client.objects.values_list('contact_email', flat=True)