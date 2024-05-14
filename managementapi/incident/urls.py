from django.urls import path
from incident.views import *

app_name = "incident"
## Define here our urls

urlpatterns = [
    path("signup-user/", UserSignUpView.as_view(), name="create-user"),
    path("login-user/", UserLoginView.as_view(), name="login-user-get-token"),
    path("create_incident/", IncidentCreateView.as_view(), name="create-incident"),
    path("get_incident/", IncidentDetailsView.as_view(), name="get-incident_details"),
    path("get-update-incident/<int:pk>/", UpdateIncident.as_view(), name="get-update-incident-details"),
    path("search-incident/", SearchIncidentView.as_view(), name="search-incident-information"),
]
