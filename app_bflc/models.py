from django.db import models

# Create your models here.
class Services(models.Model):
    titres =models.CharField(max_length=50)
    descriptions =models.TextField()
    date_aj=models.DateField(auto_now_add=True, null=True,blank=True)
    def __str__(self):
        return self.titres
    
    
class Albums(models.Model):
    titre_event=models.CharField(max_length=50)
    descriptions=models.TextField()
    photo = models.ImageField(upload_to="photo",null=True,blank=True)
    date_aj=models.DateField(auto_now_add=True,null=True,blank=True)
    def __str__(self):
        return self.titre_event
class Facture(models.Model):
    annee=models.CharField(max_length=50)
    mois=models.CharField(max_length=50)
    file = models.FileField(upload_to="photo", max_length=100)
    commentaire = models.TextField()
    date_aj=models.DateField(auto_now_add=True,null=True,blank=True)
    def __str__(self):
        return "Facture du mois de"+self.mois+" Année"+self.annee
    
class Activites(models.Model):
     photo = models.ImageField(upload_to="photo",null=True,blank=True)
     description = models.TextField()
     date_aj=models.DateField(auto_now_add=True,null=True,blank=True)
     def __str__(self):
        return "Activités du "
class Message(models.Model):
    # name=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)
    email=models.EmailField(max_length=100)
    subject=models.CharField(max_length=50)
    message=models.TextField(max_length=500)
    date_aj= models.DateField(auto_now_add=True,null=True,blank=True)
    def __str__(self):
        return self.subject
class Commande(models.Model):
    engins= models.CharField(max_length=50)
    adres = models.CharField(max_length=50)
    phone=models.CharField(max_length=50)
    date_aj= models.DateField(auto_now_add=True,null=True,blank=True)
    def __str__(self):
        return "Une Nouvel commande "+self.engins
    
    

    