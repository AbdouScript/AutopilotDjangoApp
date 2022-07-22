
from cProfile import label
from dataclasses import field, fields
from .models import ActivitesMissions, ActivitesType, Consultant, TimeSheet, Competence, ConsultantCompetence, Missions, MissionsType
from django import forms
from django.db import models
import datetime

######################################################################################################
#                                       Consultant                                                   #
######################################################################################################

class FormConsultant(forms.ModelForm): 
    nom = forms.CharField(max_length=50,label="Nom" )
    prenom = forms.CharField(max_length=50, label="Prenom")
    class Meta:
        model= Consultant
        fields=['nom', 'prenom']
class delFormConsultant(forms.ModelForm): 
        idConsultant= forms.ModelChoiceField(Consultant.objects.all())
        class Meta:
            model= Consultant
            fields=['idConsultant']
class editFormConsultant(forms.ModelForm): 
    nom = forms.CharField(max_length=50,label="Nom" )
    prenom = forms.CharField(max_length=50, label="Prenom")
    class Meta:
        model= Consultant
        fields=['nom', 'prenom']

######################################################################################################
#                                       TimeSheet                                                    #
######################################################################################################


class FormTimesheet(forms.ModelForm): 
    # idTimeSheet = forms.IntegerField()
    idConsultant= forms.ModelChoiceField(Consultant.objects.filter(nom__in=(Consultant.objects.all().values_list('nom',flat=True).distinct())).values_list('nom',flat=True))
    annee = forms.IntegerField()
    Semaine = forms.IntegerField()
    tempsPasse = forms.IntegerField()
    idMission = forms.ModelChoiceField(Missions.objects.filter(idMission__in=(TimeSheet.objects.all().values_list('idMission',flat=True).distinct())).values_list('nomMission',flat=True))
    class Meta:
        model= TimeSheet
        fields=['annee', 'Semaine', 'tempsPasse', 'idMission', 'idConsultant']

class delFormTimesheet(forms.ModelForm): 
        timesheet= forms.ModelChoiceField(Competence.objects.all())
        class Meta:
            model= Competence
            fields=['timesheet']

######################################################################################################
#                                       Competence                                                   #
######################################################################################################


class FormCompetence(forms.ModelForm):
    description = forms.CharField(max_length=50, label="description")
    class Meta:
        model = Competence
        fields = ['description']

class delFormCompetence(forms.ModelForm): 
        description= forms.ModelChoiceField(Competence.objects.filter(description__in=(Competence.objects.all().values_list('description',flat=True).distinct())).values_list('description',flat=True))
        class Meta:
            model= Competence
            fields=['description']

class editFormCompetence(forms.ModelForm):
    description = forms.CharField(max_length=50, label="description")
    class Meta:
        model = Competence
        fields = ['description']

######################################################################################################
#                                       Missions                                                     #
######################################################################################################

class FormMission(forms.ModelForm) :
    nomMission = forms.CharField(label ='Nom de la mission',max_length=50)
    idMissionType = forms.ModelChoiceField(MissionsType.objects.all(), label='MissionType')
    startDate = forms.DateField(label='Date de début')
    endDate = forms.DateField(label ='Date de fin')
    
    class Meta:
        model = Missions
        fields= ['nomMission','startDate', 'endDate', 'idMissionType']

class delFormMission(forms.ModelForm): 
        idMission = forms.ModelChoiceField(Missions.objects.filter(idMission__in=(Missions.objects.all().values_list('idMission',flat=True).distinct())).values_list('idMission',flat=True))
        class Meta:
            model = Missions
            fields= ['idMission']   

class editFormMission(forms.ModelForm):
    nomMission = forms.CharField(label ='Nom de la mission',max_length=50)
    idMissionType = forms.ModelChoiceField(MissionsType.objects.all(), label='MissionType')
    startDate = forms.DateField(label='Date de début')
    endDate = forms.DateField(label ='Date de fin')
    
    class Meta:
        model = Missions
        fields= ['nomMission','startDate', 'endDate', 'idMissionType']            

######################################################################################################
#                                       Activité Mission                                             #
######################################################################################################

class FormActiviteMission(forms.ModelForm):
    idActivitesType = forms.ModelChoiceField(ActivitesType.objects.all(), label='ActiviteType')
    idMission = forms.ModelChoiceField(Missions.objects.all(), label='Mission')
    idConsultant = forms.ModelChoiceField(Consultant.objects.all(), label='Consultant')
    tjm = forms.IntegerField(label='tjm')
    estimationCharge = forms.IntegerField(label='charge')
    devise = forms.CharField(label='devise')
    tauxChangeEur = forms.CharField(label='taux de change')
    
    class Meta:
        model = ActivitesMissions
        fields = ['idActivitesType', 'idMission', 'idConsultant', 'tjm', 'estimationCharge', 'devise', 'tauxChangeEur']
        # 

class delFormActiviteMission(forms.ModelForm):
    
    idActivitesMissions = forms.ModelChoiceField(ActivitesMissions.objects.filter(idActivitesMissions__in=(ActivitesMissions.objects.all().values_list
    ('idActivitesMissions',flat=True).distinct())).values_list('idActivitesMissions',flat=True))
    class Meta:
        model = ActivitesMissions
        fields= ["idActivitesMissions"]

class editFormActiviteMission(forms.ModelForm):
    idMission = forms.ModelChoiceField(Missions.objects.all(),label='Mission')
    tjm = forms.IntegerField(label='tjm')
    estimationCharge = forms.IntegerField(label='estimationCharge')
    idActivitesType= forms.ModelChoiceField(ActivitesType.objects.all(),label = 'Activités Type')
    idConsultant = forms.ModelChoiceField(Consultant.objects.all(),label = 'Consultant')
    devise = forms.CharField(label='devise')
    tauxChangeEur = forms.IntegerField(label='taux_ChangeEur')
    
    class Meta:
        model = ActivitesMissions
        fields= ['idActivitesType','idMission','tjm', 'estimationCharge','idConsultant','devise','tauxChangeEur']

######################################################################################################
#                                       Activité Type                                                #
######################################################################################################


class FormActiviteType(forms.ModelForm):
    description = forms.CharField()

    class Meta:
        model = ActivitesType
        fields= ['description']

class delFormActiviteType(forms.ModelForm):
    description = forms.ModelChoiceField(ActivitesType.objects.filter(description__in=(ActivitesType.objects.all().values_list
    ('description',flat=True).distinct())).values_list('description',flat=True))

    class Meta:
        model = ActivitesType
        fields= ['description']

class editFormActiviteType(forms.ModelForm):
    description = forms.CharField()

    class Meta:
        model = ActivitesType
        fields= ['description']

######################################################################################################
#                                       Mission Type                                                 #
######################################################################################################

class FormMissionType(forms.ModelForm):
    titre = forms.CharField()
    description = forms.CharField()

    class Meta:
        model = MissionsType
        fields= ['titre', 'description']

class delFormMissionType(forms.ModelForm):
    idMissionType = forms.ModelChoiceField(MissionsType.objects.filter(idMissionType__in=(MissionsType.objects.all().values_list
    ('idMissionType',flat=True).distinct())).values_list('idMissionType',flat=True))

    class Meta:
        model = MissionsType
        fields= ['idMissionType']

class editFormMissionType(forms.ModelForm):
    titre = forms.CharField()
    description = forms.CharField()

    class Meta:
        model = MissionsType
        fields= ['titre','description']