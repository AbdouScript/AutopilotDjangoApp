from django.db import models
from django.conf import settings

# Create your models here.
class Consultant(models.Model) : 
    idConsultant=models.fields.BigAutoField(primary_key= True, null=False)
    nom = models.fields.CharField(max_length=50)
    prenom = models.fields.CharField(max_length=50)

    class Meta:
            managed = False
            db_table = 'consultant'
    def __str__(self):
        return str(self.nom + ' ' + self.prenom)

class Competence(models.Model) : 
    idCompetence = models.fields.BigAutoField(primary_key= True, null=False)
    description = models.fields.CharField(max_length=50)

    class Meta:
            managed = False
            db_table = 'competences'
    def __str__(self):
        return str(self.description)

class Missions(models.Model) :
    idMission = models.fields.BigAutoField(primary_key= True, null=False)
    idMissionType =models.ForeignKey('MissionsType', on_delete= models.CASCADE, db_column = 'idMissionType')
    startDate = models.DateField()
    endDate = models.DateField()
    nomMission = models.TextField()
    class Meta:
            managed = False
            db_table = 'missions'
    def __str__(self):
        return str(self.nomMission)

class MissionsType(models.Model) :
    idMissionType = models.fields.BigAutoField(primary_key = True, null=False, db_column='idMissionType')
    titre = models.TextField()
    description = models.TextField()
    class Meta:
        managed=False
        db_table = 'MissionsType'
    def __str__(self):
        return str(self.idMissionType)

class ActivitesType(models.Model):
    idActivitesType = models.fields.BigAutoField(primary_key = True, null=False, db_column='idActivitesType') 
    description = models.TextField()
    class Meta:
        managed=False
        db_table = 'ActivitesType'
    def __str__(self):
        return (self.description)
        

class ActivitesMissions(models.Model):
    idActivitesMissions = models.fields.BigAutoField(primary_key= True, null= False, db_column= 'idActivitesMissions')
    idActivitesType = models.ForeignKey('ActivitesType', on_delete=models.CASCADE, db_column= 'idActivitesType')
    idMission = models.ForeignKey('Missions', on_delete= models.CASCADE, db_column= 'idMission')
    idConsultant = models.ForeignKey('Consultant',on_delete= models.CASCADE, db_column= 'idConsultant')
    tjm = models.IntegerField()
    estimationCharge = models.IntegerField()
    devise = models.TextField()
    tauxChangeEur = models.TextField()
    class Meta:
        managed=False
        db_table = 'activitesMissions'
    def __str__(self):
        return (self.idMission)

class TimeSheet(models.Model) :
    idTimeSheet = models.fields.BigAutoField(primary_key= True, null=False)
    idMission = models.ForeignKey(
    'Missions',
    db_column="idMission",
    on_delete=models.CASCADE,
    )
    idConsultant= models.ForeignKey(
    'Consultant',
    db_column="idConsultant",
    on_delete = models.CASCADE,
)
    annee = models.IntegerField()
    Semaine = models.fields.SmallIntegerField()
    tempsPasse = models.FloatField(db_column='tempsPassé')

 
    class Meta:
            managed = False
            db_table = 'timeSheet'
    def __str__(self):
        return str(self.idTimeSheet)
    

class ConsultantCompetence(models.Model) : 
    idCompetence = models.ForeignKey(
    'Competence',
    db_column="idCompetence",
    on_delete=models.CASCADE,
)
    idConsultant = models.ForeignKey(
    
    'Consultant',
    db_column="idConsultant",
    on_delete=models.CASCADE,
)
    id = models.fields.BigAutoField(primary_key= True, null=False)

    class Meta:
            managed = False
            db_table = 'consultantsCompetences'
    def __str__(self):
        return str(self.id)

class Formulaire(models.Model):
    name = models.CharField(max_length=20)
    firstName = models.CharField(max_length=20)

