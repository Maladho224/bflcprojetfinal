from django.contrib import admin
from .models import *

# Register your models here.
admin.site.site_header="ESPACE D'ADMINISTRATION DU SITE BFLC"
admin.site.site_title="SITE SITE DE L'ENTREPRISE BFLC"
class DisplayServices(admin.ModelAdmin):
    list_display=('titres','descriptions')
class DisplayAlbum(admin.ModelAdmin):
    list_display=('titre_event','descriptions','photo')
class DisplayActivites(admin.ModelAdmin):
    list_display=('date_aj','description','photo')
class DisplayFactures(admin.ModelAdmin):
    list_display=('annee','mois','commentaire','file')
class DisplayMessage(admin.ModelAdmin):
    list_display=('date_aj','subject')
admin.site.register(Services,DisplayServices)
admin.site.register(Albums,DisplayAlbum)
admin.site.register(Activites,DisplayActivites)
admin.site.register(Facture,DisplayFactures)
admin.site.register(Message,DisplayMessage)
