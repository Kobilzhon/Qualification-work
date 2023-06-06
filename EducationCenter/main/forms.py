from .models import *
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
    content = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'rows': 4, 'placeholder': 'Add comment',}),
        # required=False,

    )



