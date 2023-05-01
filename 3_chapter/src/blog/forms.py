from django import forms

from .models import Comment


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25, initial="Andrii", label="User")
    email = forms.EmailField(
        initial="77nefedov@gmail.com",
        required=True,
        label="Ваш электронный адрес",
        help_text="Пожалуйста, введите действительный адрес электронной почты",
    )
    to = forms.EmailField(
        required=True,
        label="Электронный адрес получателя",
    )
    comments = forms.CharField(
        required=False,
        widget=forms.Textarea,
        initial="Пишите ваше сообщение здесь",
    )


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["name", "email", "body"]
