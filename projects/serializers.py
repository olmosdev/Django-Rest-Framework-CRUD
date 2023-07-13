# Those serializers allow us to call special models of Rest Framework
from rest_framework import serializers

# This is based on a recently created project (the project that was called "Project")
# With this, Django will know that it has to answer when a request is made (POST, GET, PUT & DELETE)
from .models import Project

# This converts s simple model to data that can be queried
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        # Name of the model
        model = Project
        # Data that can be consulted
        fields = ('id', 'title', 'description', 'technology', 'created_at')
        read_only_fields = ('created_at', ) # We always need to add a coma at the end
