from django.contrib import admin

from .forms import DataForm
from .models import Data

class DataAdmin(admin.ModelAdmin):
    list_display = ['title', 'body']
    # class Meta:
    #     model = Data
    form = DataForm

admin.site.register(Data, DataAdmin)