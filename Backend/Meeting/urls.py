from django.urls import path, include
from .views import MeetingApi,MeetEditApi,OwnerTimeApi,CheckURL,EditTimeApi,InvitationLinkApi
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
      path('api/event/add', MeetingApi.as_view()),
      path('api/event/<int:meetid>/edit/', MeetEditApi.as_view()),
      path('api/event/<int:meetid>/time/', OwnerTimeApi.as_view()),
      path('api/event/<int:meetid>/time/edit/', EditTimeApi.as_view()),
      path('<str:meeturl>/', InvitationLinkApi.as_view()),
      path('api/event/checkurl/', CheckURL.as_view())
]