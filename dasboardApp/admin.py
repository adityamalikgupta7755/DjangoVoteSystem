from django.contrib import admin

# Register your models here.
from .models import Pofile, Gender_Table, Mail_Tempalte, SendInvite, BatchInvite

admin.site.register(Pofile)
admin.site.register(Gender_Table)
admin.site.register(Mail_Tempalte)
admin.site.register(SendInvite)
admin.site.register(BatchInvite)



