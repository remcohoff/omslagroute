from .views import *
from django.urls import path


urlpatterns = [
    path('mijn-clienten/', UserCaseList.as_view(), name='cases_by_profile'),
    path('<int:pk>', CaseDetailView.as_view(), name='case'),
    path('verwijder/<int:pk>', CaseDeleteView.as_view(), name='delete_case'),
    path('nieuw/<str:slug>/', GenericCaseCreateFormView.as_view(), name='create_case'),
    path('<int:pk>/<str:slug>/', GenericCaseUpdateFormView.as_view(), name='update_case'),
    path('<int:pk>/<str:slug>/verstuur', SendCaseView.as_view(), name='send_case'),
]
