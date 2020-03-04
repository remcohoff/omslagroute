from .views import *
from django.urls import path
from web.timeline.models import Moment


urlpatterns = [
    path('', DocumentList.as_view(), name='document_list'),
    path('nieuw', DocumentVersionFormSetCreate.as_view(), name='document_create'),
    path('delete/<int:pk>', DocumentDelete.as_view(), name='document_delete'),
    path('update/<int:pk>', DocumentUpdate.as_view(), name='document_update'),

    path('nieuw/<int:document>', DocumentVersionCreate.as_view(), name='add_document_version_to_document'),
    path('nieuw-voor-timeline/<int:moment_id>', CreateDocumentAddToMoment.as_view(), name='add_document_to_moment'),
    path('delete-versie/<int:pk>', DocumentVersionDelete.as_view(), name='documentversion_delete'),
    path('downloadobject', download_object, name='download_object'),
]
