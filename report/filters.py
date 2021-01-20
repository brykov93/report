import django_filters as df
from .models import Patients
import django_filters


queryset = Patients.objects.all()
organization_CHOICES =[organization.organization for organization in queryset]
organization_CHOICES=list(dict.fromkeys(organization_CHOICES))
a=(())
for org in organization_CHOICES:
    b=(org,org)
    a=a+(b,)



class PatientsFilter(df.FilterSet):
    organization=django_filters.ChoiceFilter(choices=a)


    class Meta:
        model = Patients
        #fields = ['organization', ]
        fields ={'organization': ['exact',],
                 'enterDate':['exact',],}