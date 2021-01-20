import django_tables2 as tables
from .models import Patients

class PatientTable(tables.Table):
    Info = tables.TemplateColumn('<a href="{{record.id}}">{{"Информация"}}</a>')
    class Meta:
        model = Patients
        # add class="paleblue" to <table> tag
        attrs = {'class': 'paleblue'}
        fields  = ['organization','patientFIO','male','age','enterDate']
        per_page = 30