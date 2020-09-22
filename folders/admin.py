from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin # MPTTModelAdmin, 
from folders.models import Folders

admin.site.register(Folders, DraggableMPTTAdmin)

