from django.contrib import admin
from .models import Contact
from .models import Portfolio
from .models import Blog
from .models import Quote

admin.site.register(Contact)
admin.site.register(Portfolio)
admin.site.register(Blog)
admin.site.register(Quote)