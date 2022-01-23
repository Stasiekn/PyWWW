from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Fieldset, ButtonHolder, Layout

from main.models import Post


class PostForm(forms.Form):
    class Meta:
        model = Post
        fields = ['title', 'content', 'published', 'spondored', 'image']
        labels = {
            "title" : "Tytuł",
            "content" : "Treść",
            "published" : "Opublikowany",
            "spondored" : "Sponsorowany"
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action = 'contact'
        self.helper.layout = Layout(
            Fieldset(
                'Dodaj post',
                'title',
                'content',
                'published',
                'spondored',
                'image'
            ),
            ButtonHolder(
                Submit('submit', 'Dodaj', css_class='btn btn-primary'),
                css_class="d-flex justify-content-end"
            )
        )

