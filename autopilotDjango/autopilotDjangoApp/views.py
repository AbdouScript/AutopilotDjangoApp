from distutils.log import error
from pydoc import describe
from sqlite3 import Time
from time import time
from django.shortcuts import render
from django.http import HttpResponse
from .models import ConsultantCompetence, Missions, TimeSheet, Consultant, Competence, ConsultantCompetence, MissionsType, ActivitesType, ActivitesMissions, Formulaire
from .forms import delFormActiviteMission, FormActiviteType, FormCompetence, FormTimesheet, FormConsultant, FormMission, FormActiviteMission, FormMissionType, delFormActiviteType, delFormConsultant, delFormCompetence, delFormMission, delFormActiviteMission, delFormMission, delFormMissionType, editFormActiviteMission, editFormActiviteType, editFormConsultant, editFormCompetence, editFormMission, editFormActiviteMission, editFormMissionType
from django.http import HttpResponse, HttpResponseRedirect


######################################################################################################
#                                       Affichage Template                                           #
######################################################################################################

def index(request):
    HttpResponseRedirect("/app/index")

def list_timesheets(request):
    list_TimeSheet = TimeSheet.objects.all()
    return render(request, 'autopilotDjangoApp/timesheets.html',{'timesheets':list_TimeSheet})
    # return HttpResponse(list_TimeSheet.Semaine)

def list_consultants(request):
    list_Consultant = Consultant.objects.all()
    return render(request, 'autopilotDjangoApp/consultant.html',{'consultants':list_Consultant})

def list_competences(request):
    list_Competence = Competence.objects.all()
    return render(request, 'autopilotDjangoApp/competence.html',{'competences':list_Competence})

def list_missions(request):
    list_Mission = Missions.objects.all()
    return render(request, 'autopilotDjangoApp/mission.html',{'missions':list_Mission})

def list_activitesTypes(request):
    activitesType = ActivitesType.objects.all()
    return render(request, 'autopilotDjangoApp/activite-type.html',{'activitesType':activitesType})

def list_activitesMission(request):
    activitesMissions = ActivitesMissions.objects.all()
    return render (request, 'AutopilotDjangoApp/activite-mission.html', {'activitesMissions': activitesMissions})

def list_missionsType(request):
    missionstype = MissionsType.objects.all()
    return render (request, 'AutopilotDjangoApp/mission-type.html', {'Missionstype' : missionstype})
    # return HttpResponse(missionstype.Missions_set.all())

def list_consultantscompetences(request):
    list_ConsultantCompetence = ConsultantCompetence.objects.all()
    # return HttpResponse(list_ConsultantCompetence)
    return render(request, 'autopilotDjangoApp/consultantcompetence.html',{'consultantscompetences':list_ConsultantCompetence})
   
def list_formulaire(request):
    list_Formulaire = Formulaire.objects.all()
    return HttpResponse("Page de formulaire")
    # return render(request, 'autopilotDjangoApp/consultantcompetence.html',{'consultantscompetences':list_ConsultantCompetence})

######################################################################################################
#                                       Consultant                                                   #
######################################################################################################

# Inscription consultant
def insConsultant(request):
    formInscription = FormConsultant()
    error=''
    if request.method == 'POST':
        formInscription = FormConsultant(request.POST)
        if(formInscription.is_valid()):
            user=Consultant.objects.filter(nom=formInscription.cleaned_data['nom'])
            if(user):
                error="Ce nom de famille existe déjà !"
                # return HttpResponse(error)
            else:
                if(formInscription.save()):
                    error=''    
                    return HttpResponseRedirect('/app/consultant/')
                else:
                    error="erreur lors de l\'enregistrement de l\'utilisateur"
        else:
            error='formulaire non valide'
        return render(request, 'autopilotDjangoApp/form-consultant.html',context={'form':formInscription,'error':error})    

    return render(request, 'autopilotDjangoApp/form-consultant.html',context={'form':formInscription,'error':error})

# suppression consultant
def delConsultant(request):
    formDelete = delFormConsultant()
    error=''
    if request.method == 'POST':
        # formDelete = FormConsultant(request.POST)
        User=Consultant.objects.filter(idConsultant=request.POST['idConsultant'])
        User.delete()
        print(User)
        return HttpResponseRedirect("/app/consultant/")
    return render(request, 'autopilotDjangoApp/del-consultant.html',context={'form':formDelete,'error':error})

# modification Consultant
def editConsultant(request,pk):
    consultant= Consultant.objects.get(pk=pk)
    editform = editFormConsultant(instance=consultant)

    error=''
    if request.method == 'POST':
        if(editform.is_valid):
            # form = Consultant.objects.filter(idConsultant=request.POST['idConsultant'])
            editform = editFormConsultant(request.POST,instance=consultant)
            editform.save()
            return HttpResponseRedirect('/app/consultant/')
    return render(request, 'autopilotDjangoApp/edit-consultant.html',context={'form':editform,'error':error})

    

######################################################################################################
#                                       TimeSheet                                                    #
######################################################################################################

# Inscription Timsheet
def insTimesheet(request):
    timesheet = FormTimesheet()
    error=''
    if request.method == 'POST':
        timesheet = FormTimesheet(request.POST)
        print(type(request.POST['annee']))
        if(timesheet.is_valid()):
            exit=TimeSheet.objects.get(annee=timesheet.cleaned_data['annee'])
            # enter=TimeSheet.objects.filter(idConsultant=timesheet.cleaned_data['idConsultant_id'])
            print(timesheet)
            if(exit):
                error="Tache déjà attribuée !"
                # return HttpResponse(error)
            else:
                timesheet.save()
                error=''    
                return HttpResponseRedirect('/app/timesheet/')
                # else:
                #     error="erreur lors de l'enregistrement de la tache"
        # else:
        #     error='formulaire non valide'
        # return render(request, 'autopilotDjangoApp/form-timesheet.html',context={'form':timesheet,'error':error})
    return render(request, 'autopilotDjangoApp/form-timesheet.html',context={'form':timesheet,'error':error})

######################################################################################################
#                                       Competence                                                   #
######################################################################################################

# Inscription competence
def insCompetence(request):
    formInscription = FormCompetence()
    error=''
    if request.method == 'POST':
        formInscription = FormCompetence(request.POST)
        if(formInscription.is_valid()):
            description=Competence.objects.filter(description=formInscription.cleaned_data['description'])
            if(description):
                error="Ce modèle existe déjà!"
                # return HttpResponse(error)
            else:
                if(formInscription.save()):
                    error=''    
                    return HttpResponseRedirect('/app/competence/')
                else:
                    error="erreur lors de l\'enregistrement de l\'utilisateur"
        else:
            error='formulaire non valide'
        return render(request, 'autopilotDjangoApp/form-competence.html',context={'form':formInscription,'error':error})    

    return render(request, 'autopilotDjangoApp/form-competence.html',context={'form':formInscription,'error':error})

# suppression consultant
def delCompetence(request):
    formDelete = delFormCompetence()
    error=''
    if request.method == 'POST':
        # formDelete = FormConsultant(request.POST)
        test=Competence.objects.filter(description=request.POST['description'])
        test.delete()
        print(test)
        return HttpResponseRedirect("/app/competence/")
    return render(request, 'autopilotDjangoApp/del-competence.html',context={'form':formDelete,'error':error})

# modification Competence
def editCompetence(request,pk):
    competence= Competence.objects.get(pk=pk)
    editform = editFormCompetence(instance=competence)

    error=''
    if request.method == 'POST':
        if(editform.is_valid):
            # form = Consultant.objects.filter(idConsultant=request.POST['idConsultant'])
            editform = editFormCompetence(request.POST,instance=competence)
            editform.save()
            return HttpResponseRedirect('/app/competence/')
    return render(request, 'autopilotDjangoApp/edit-competence.html',context={'form':editform,'error':error})

######################################################################################################
#                                       Mission                                                      #
######################################################################################################

def insMission(request):
    formmissions = FormMission()

    if request.method == 'POST':
        formmissions = FormMission(request.POST)
        if (formmissions.is_valid()):
                    # mission = Missions.objects.filter(
                    # nomMission = formmissions.cleaned_data ['nomMission']
                    # )
            formmissions.save()
                    #     error=''
                    #     return HttpResponseRedirect('/autopilot/missions/')
                    # else:
                    #     error='erreur lord de la création de la missions'
        
            return HttpResponseRedirect('/app/mission/')   

    return render(request, 'autopilotDjangoApp/form-mission.html',context={'form':formmissions})
# suppression mission
def delMission(request):
    formDelete = delFormMission()
    error=''
    if request.method == 'POST':
        # formDelete = FormConsultant(request.POST)
        test=Missions.objects.filter(idMission=request.POST['idMission'])
        test.delete()
        print(test)
        return HttpResponseRedirect("/app/mission/")
    return render(request, 'autopilotDjangoApp/del-mission.html',context={'form':formDelete,'error':error})

# modification Competence
def editMission(request,pk):
    mission= Missions.objects.get(pk=pk)
    editform = editFormMission(instance=mission)

    error=''
    if request.method == 'POST':
        if(editform.is_valid):
            # form = Consultant.objects.filter(idConsultant=request.POST['idConsultant'])
            editform = editFormMission(request.POST,instance=mission)
            editform.save()
            return HttpResponseRedirect('/app/mission/')
    return render(request, 'autopilotDjangoApp/edit-mission.html',context={'form':editform,'error':error})

######################################################################################################
#                                       Activité Mission                                             #
######################################################################################################

def insActivitesMission(request):
    formactivitesmissions = FormActiviteMission()

    if request.method == 'POST':
        formactivitesmissions = FormActiviteMission(request.POST)
        if(formactivitesmissions.is_valid()):

                formactivitesmissions.save()

                return HttpResponseRedirect('/app/activite-mission')
    
    return render(request, 'AutopilotDjangoApp/form-activitesMission.html',context={'form':formactivitesmissions})    

def delActivitesMission(request):
    formDelete = delFormActiviteMission()
    
    if request.method == 'POST':
        
        test=ActivitesMissions.objects.filter(idActivitesMissions=request.POST['idActivitesMissions'])
        test.delete()
        print(test)
        return HttpResponseRedirect("/app/activite-mission/")
    return render(request, 'AutopilotDjangoApp/del-activitesMission.html',context={'form':formDelete})

def editActivitesMission(request,pk):
    activites= ActivitesMissions.objects.get(pk=pk)
    editform = editFormActiviteMission(instance=activites)

    if request.method == 'POST':
        if(editform.is_valid):
            editform = editFormActiviteMission(request.POST,instance=activites)

            editform.save()
            return HttpResponseRedirect('/app/activite-mission/')

    return render(request, 'AutopilotDjangoApp/edit-activitesMission.html',context={'form':editform,})

######################################################################################################
#                                       Activité Type                                                #
######################################################################################################

def insActivitesType(request):
    formactivitesType = FormActiviteType()

    if request.method == 'POST':
        formActivitesType = FormActiviteType(request.POST)
        if(formActivitesType.is_valid()):

                formActivitesType.save()

                return HttpResponseRedirect('/app/activite-type')
    
    return render(request, 'AutopilotDjangoApp/form-activitesType.html',context={'form':formactivitesType})

def delActivitesType(request):
    formDelete = delFormActiviteType()
    
    if request.method == 'POST':
        
        test=ActivitesType.objects.filter(description=request.POST['description'])
        test.delete()
        print(test)
        return HttpResponseRedirect("/app/activite-type/")
    return render(request, 'AutopilotDjangoApp/del-activitesType.html',context={'form':formDelete})

def editActivitesType(request,pk):
    activitesType= ActivitesType.objects.get(pk=pk)
    editform = editFormActiviteType(instance=activitesType)

    if request.method == 'POST':
        if(editform.is_valid):
            editform = editFormActiviteType(request.POST,instance=activitesType)

            editform.save()
            return HttpResponseRedirect('/app/activite-type/')

    return render(request, 'AutopilotDjangoApp/edit-activitesType.html',context={'form':editform,})

######################################################################################################
#                                       Mission Type                                                 #
######################################################################################################

def insMissionType(request):
    formMissionType = FormMissionType()

    if request.method == 'POST':
        formMissionType =FormMissionType(request.POST)
        if(formMissionType.is_valid()):

                formMissionType.save()

                return HttpResponseRedirect('/app/mission-type')
    
    return render(request, 'AutopilotDjangoApp/form-missionType.html',context={'form':formMissionType})

def delMissionType(request):
    formDelete = delFormMissionType()
    
    if request.method == 'POST':
        
        test=MissionsType.objects.filter(idMissionType=request.POST['idMissionType'])
        test.delete()
        print(test)
        return HttpResponseRedirect("/app/mission-type/")
    return render(request, 'AutopilotDjangoApp/del-missionType.html',context={'form':formDelete})

def editMissionType(request,pk):
    MissionTypes= MissionsType.objects.get(pk=pk)
    editform = editFormMissionType(instance=MissionTypes)

    if request.method == 'POST':
        if(editform.is_valid):
            editform = editFormMissionType(request.POST,instance=MissionTypes)

            editform.save()
            return HttpResponseRedirect('/app/mission-type/')

    return render(request, 'AutopilotDjangoApp/edit-missionType.html',context={'form':editform})