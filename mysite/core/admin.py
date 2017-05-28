from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import Consultation


admin.site.register(Consultation, MarkdownxModelAdmin)