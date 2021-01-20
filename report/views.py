from report.models import Patients
from report.tables import PatientTable

from .filters import PatientsFilter
from .forms import PatientsListFormHelper, pacInfoForm
from .utils import PagedFilteredTableView, pacInfoView

from django.shortcuts import render

class people(PagedFilteredTableView):
    model = Patients
    table_class = PatientTable
    filter_class = PatientsFilter
    formhelper_class = PatientsListFormHelper

#    def get(self, request):
#        table = PatientTable(Patients.objects.all())
#        RequestConfig(request).configure(table)
#        return render(request, 'people.html', {'table': table})

class patientInfo(pacInfoView):
    template_name = "pacInfo.HTML"
    model = Patients
    form_class  = pacInfoForm


    def get(self, request,id):
        queryset = Patients.objects.get(id=id)
        return render(request, 'pacInfo.HTML', {'form': pacInfoForm(instance=queryset)})