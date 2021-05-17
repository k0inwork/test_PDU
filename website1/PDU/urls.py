from django.urls import path
from .views import pdu_view,pdu_switchoff

urlpatterns = [
     path('pdus', pdu_view),
     path('disablePDU', pdu_switchoff),
 ]