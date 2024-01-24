from django import forms
from django.contrib.auth.forms import PasswordChangeForm, UserChangeForm
from django.contrib.auth.models import User

from newsApp import models


class UpdateProfile(UserChangeForm):
    username = forms.CharField(
        max_length=250, help_text="Foydalanuvchi nomi majburiy.")
    email = forms.EmailField(
        max_length=250, help_text="Elektron pochta majburiy.")
    first_name = forms.CharField(
        max_length=250, help_text="Ism majburiy.")
    last_name = forms.CharField(
        max_length=250, help_text="Familiya majburiy.")
    current_password = forms.CharField(max_length=250)

    class Meta:
        model = User
        fields = ('email', 'username', 'first_name', 'last_name')

    def clean_current_password(self):
        if not self.instance.check_password(self.cleaned_data['current_password']):
            raise forms.ValidationError(f"Parol noto'g'ri")

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            user = User.objects.exclude(
                id=self.cleaned_data['id']).get(email=email)
        except Exception as e:
            return email
        raise forms.ValidationError(
            f"The {user.email} mail is already exists/taken")

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            user = User.objects.exclude(
                id=self.cleaned_data['id']).get(username=username)
        except Exception as e:
            return username
        raise forms.ValidationError(
            f"The {user.username} mail is already exists/taken")


class UpdatePasswords(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control form-control-sm rounded-0'}), label="Eski parol")
    new_password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control form-control-sm rounded-0'}), label="Yangi parol")
    new_password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control form-control-sm rounded-0'}), label="Yangi parolni tasdiqlash")


    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')


class savePost(forms.ModelForm):
    user = forms.CharField(max_length=30, label="Muallif")
    category = forms.CharField(max_length=30, label="Kategoriya")
    title = forms.CharField(max_length=250, label="Sarlavha")
    short_description = forms.Textarea()
    content = forms.Textarea()
    meta_keywords = forms.Textarea()
    banner_path = forms.ImageField(label="Banner Rasmi")
    status = forms.CharField(max_length=2)


    class Meta():
        model = models.Post
        fields = ('user', 'category', 'title', 'short_description',
                  'content', 'meta_keywords', 'banner_path', 'status',)


    def clean_category(self):
        catID = self.cleaned_data['category']
        try:
            category = models.Category.objects.get(id=catID)
            return category
        except:
            raise forms.ValidationError("Noto'g'ri kategoriya tanlandi")


    def clean_user(self):
        userID = self.cleaned_data['user']
        try:
            user = models.User.objects.get(id=userID)
            return user
        except:
            raise forms.ValidationError("Noto'g'ri foydalanuvchi tanlandi")


class saveComment(forms.ModelForm):
    post = forms.CharField(max_length=30, label="Maqola")
    name = forms.CharField(max_length=250, label="Ism")
    email = forms.CharField(max_length=250, label="Elektron pochta")
    subject = forms.CharField(max_length=250, label="Mavzu")
    message = forms.Textarea()


    class Meta():
        model = models.Comment
        fields = ('post', 'name', 'email', 'subject', 'message',)


    def clean_post(self):
        postID = self.cleaned_data['post']
        try:
            post = models.Post.objects.get(id=postID)
            return post
        except:
            raise forms.ValidationError("Maqola IDsi noto'g'ri")
