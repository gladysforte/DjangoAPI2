from django.urls import path, include
from rest_framework.routers import DefaultRouter
from kpop import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'groupcat', views.GroupCatViewSet)
router.register(r'kpopgroups', views.KpopGroupsViewSet)
router.register(r'members', views.MembersViewSet)
router.register(r'songs', views.SongsViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    path('kpopgroups/<int:pk>/members', views.GroupMembers.as_view()),
    path('kpopgroups/<int:pk>/songs', views.GroupSongs.as_view()),
]
