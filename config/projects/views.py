from rest_framework import viewsets
from .models import Projects
from .serializers import ProjectsSerializer
from config.permissions import IsAdminOrReadOnly




class ProjectsAPIViews(viewsets.ModelViewSet):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer
    permission_classes = (IsAdminOrReadOnly,)