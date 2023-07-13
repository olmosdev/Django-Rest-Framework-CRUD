# A ViewSet allows to establish who can consult our data and with what methods (GET, POST, PUT & DELETE) 
from projects.models import Project # or from .models import Project
from rest_framework import viewsets, permissions
from .serializers import ProjectSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    # What queries are allowed
    # When this ViewSet is being used, using the model "Project" we will be consulting all the objects
    queryset = Project.objects.all() # Querying all the data in a table
    permission_classes = [permissions.AllowAny] # Who is allowed to make operations with this type of queries (In this case, any client)
    serializer_class = ProjectSerializer # Which serializer will use this data
