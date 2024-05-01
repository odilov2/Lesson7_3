from django.contrib import admin
from .models import Albom, Artist, Songs

admin.site.register(Artist)
admin.site.register(Albom)
admin.site.register(Songs)

