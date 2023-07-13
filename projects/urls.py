# Creeating paths for clients to use
from rest_framework import routers
from .api import ProjectViewSet

# This is going to create the CRUD (For GET, POST, PUT & DELETE)
router = routers.DefaultRouter()
router.register('api/projects', ProjectViewSet, 'projects') # Route, dataset, name of this route
urlpatterns = router.urls