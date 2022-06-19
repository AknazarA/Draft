from django.contrib import admin
from .models import *

admin.site.register(Category)
admin.site.register(Termin)

admin.site.register(Post)
admin.site.register(ImageBlock)
admin.site.register(TextBlock)
admin.site.register(CodeBlock)