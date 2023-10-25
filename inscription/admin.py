from django.contrib import admin

import inscription
from inscription.models import Parent, Enfant, InscriptionSaison, Saison

# Register your models here.
admin.site.register(InscriptionSaison)
admin.site.register(Parent)
admin.site.register(Enfant)
admin.site.register(Saison)