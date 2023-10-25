from django.contrib import admin

import inscription
from inscription.models import Inscription, Parent, Enfant

# Register your models here.
admin.site.register(Inscription)
admin.site.register(Parent)
admin.site.register(Enfant)