from django.forms import ModelForm
from .models import *


class CategoryForm(ModelForm):

	class Meta:
		model = Category
		fields = ['name', 'image']



class TerminForm(ModelForm):

	class Meta:
		model = Termin
		exclude = ('user',)
