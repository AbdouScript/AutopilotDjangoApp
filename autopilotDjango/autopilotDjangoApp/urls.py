from . import views
from django.contrib import admin
from django.urls import path,include
app_name='autopilotDjangoApp'

urlpatterns = [
    path("timesheet/", views.list_timesheets, name = "timesheet"),
    path("consultant/", views.list_consultants, name = "consultant"),
    path("competence/", views.list_competences, name = "competence"),
    path("consultantcompetence/", views.list_consultantscompetences, name = "consultantscompetences"),
    # path("timeconsultant/", views.details, name = "utilisateur"),
    path("activite-mission/", views.list_activitesMission, name = "activite-mission"),
    path("activite-type/", views.list_activitesTypes, name = "activite-type"),
    path("mission-type/", views.list_missionsType, name = "mission-type"),
    path("mission/", views.list_missions, name = "utilisateur"),
    path("formulaire/", views.list_formulaire, name = "formualire"),

    path("register-mission/", views.insMission, name = "registerMission"),
    path("supprimerMission/", views.delMission, name = "supprimerMission"),
    path("<int:pk>/modifierMission/", views.editMission, name = "modifierMission"),

    path("register-activiteMission/", views.insActivitesMission, name = "registerActiviteMission"),
    path("supprimerActiviteMission/", views.delActivitesMission, name = "supprimerActiviteMission"),
    path("<int:pk>/modifierActiviteMission/", views.editActivitesMission, name = "modifierActiviteMission"),
    
    path("register-activiteType/", views.insActivitesType, name = "registerActiviteType"),
    path("supprimerActiviteType/", views.delActivitesType, name = "supprimerActivitetype"),
    path("<int:pk>/modifierActiviteType/", views.editActivitesType, name = "modifierActiviteType"),
    
    path("register-missionType/", views.insMissionType, name = "registerMissionType"),
    path("supprimerMissionType/", views.delMissionType, name = "supprimerMissionType"),
    path("<int:pk>/modifierMissionType/", views.editMissionType, name = "modifierMissionType"),

    path("register-consultant/", views.insConsultant, name = "registerConsultant"),
    path("supprimerConsultant/", views.delConsultant, name = "supprimerConsultant"),
    path("<int:pk>/modifierConsultant/", views.editConsultant, name = "modifierConsultant"),

    path("register-timesheet/", views.insTimesheet, name = "registerTimesheet"),

    path("register-competence/", views.insCompetence, name = "registerCompetence"),
    path("supprimerCompetence/", views.delCompetence, name = "supprimerCompetence"),
    path("<int:pk>/modifierCompetence/", views.editCompetence, name = "modifierCompetence")
]