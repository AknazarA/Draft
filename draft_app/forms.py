from django.forms import ModelForm, FileInput
from .models import *


class CategoryForm(ModelForm):

	class Meta:
		model = Category
		fields = ['name', 'image']
		widgets = {"image": FileInput(attrs={"onchange": "preview_image(event)"})}



class TerminForm(ModelForm):

	class Meta:
		model = Termin
		exclude = ('user',)
		widgets = {"image": FileInput(attrs={"onchange": "preview_image(event)"})}


class PostForm(ModelForm):
	class Meta:
		model = Post
		fields = "__all__"

# class TopicForm(forms.ModelForm):
#     class Meta:
#         model = Topic
#         fields = ["heading", "body", "image", "user"]

#         widgets = {"image": forms.FileInput(attrs={"onchange": "preview_image(event)"})}