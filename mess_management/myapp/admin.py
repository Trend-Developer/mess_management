from django.contrib import admin

from .models import *

admin.site.register(MessUser)
admin.site.register(Student)
admin.site.register(StudentMessDetails)
admin.site.register(MessMenu)
admin.site.register(BillModel)
admin.site.register(Cost)