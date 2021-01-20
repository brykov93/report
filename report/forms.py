from .models import Patients
from crispy_forms.helper import FormHelper
from django.forms import ModelForm, Textarea, EmailInput
from crispy_forms.layout import Layout, Submit, Div, Column, ButtonHolder, Reset, HTML


class PatientsListFormHelper(FormHelper):
    model = Patients
    form_tag = True
    layout = Layout(Div(Column('organization', style='display:inline-block', css_style=''),
                        Column('enterDate', style='display:inline-block', css_style='''css_class="bigdivs"'''),
                        Column(ButtonHolder(Submit('submit', 'Отфильтровать', css_class='button white right')
                                            ), style='display:inline-block'),
                        Column(ButtonHolder(
                            Reset('reset', 'Очистить', css_class='button white right', onclick="myFunction()")
                            ), style='display:inline-block')
                        ))


class pacInfoForm(ModelForm):
    class Meta:
        model = Patients
        # fields = ('organization',)
        fields = '__all__'
        widgets = {
            'enterDate': Textarea(attrs={'rows': 1, 'cols': 10, 'readonly': 'readonly'}),
            'organization': Textarea(attrs={'rows': 1, 'cols': 100, 'readonly': 'readonly'}),
            'daysUndersupervision': Textarea(attrs={'rows': 1, 'cols': 5, 'readonly': 'readonly'}),
            'entryDate': Textarea(attrs={'rows': 1, 'cols': 10, 'readonly': 'readonly'}),

            'patientFIO': Textarea(attrs={'rows': 1, 'cols': 50, 'readonly': 'readonly'}),
            'male': Textarea(attrs={'rows': 1, 'cols': 5, 'readonly': 'readonly'}),
            'age': Textarea(attrs={'rows': 1, 'cols': 5, 'readonly': 'readonly'}),

            'length': Textarea(attrs={'rows': 1, 'cols': 5}),
            'weigth': Textarea(attrs={'rows': 1, 'cols': 5}),

            'pregantPeriod': Textarea(attrs={'rows': 1, 'cols': 10, 'readonly': 'readonly'}),
            'childStatus': Textarea(attrs={'rows': 2, 'cols': 50, 'readonly': 'readonly'}),

            'bodyTemperature': Textarea(attrs={'rows': 1, 'cols': 20, 'readonly': 'readonly'}),
            'breethTemp': Textarea(attrs={'rows': 1, 'cols': 20, 'readonly': 'readonly'}),
            'heartRate': Textarea(attrs={'rows': 1, 'cols': 20, 'readonly': 'readonly'}),
            'AD': Textarea(attrs={'rows': 1, 'cols': 20, 'readonly': 'readonly'}),
            'o2Level': Textarea(attrs={'rows': 1, 'cols': 20, 'readonly': 'readonly'}),

            'dyspnea': Textarea(attrs={'rows': 1, 'cols': 20, 'readonly': 'readonly'}),
            'cough': Textarea(attrs={'rows': 1, 'cols': 20, 'readonly': 'readonly'}),
            'sputum': Textarea(attrs={'rows': 1, 'cols': 20, 'readonly': 'readonly'}),

            'hemoglobin': Textarea(attrs={'rows': 1, 'cols': 20, 'readonly': 'readonly'}),
            'leukocytes': Textarea(attrs={'rows': 1, 'cols': 20, 'readonly': 'readonly'}),
            'lymphocytes': Textarea(attrs={'rows': 1, 'cols': 20, 'readonly': 'readonly'}),
            'platelets': Textarea(attrs={'rows': 1, 'cols': 20, 'readonly': 'readonly'}),
            'ESR': Textarea(attrs={'rows': 1, 'cols': 20, 'readonly': 'readonly'}),
            'cReactiveProtein': Textarea(attrs={'rows': 1, 'cols': 20, 'readonly': 'readonly'}),
            'oxygenTension': Textarea(attrs={'rows': 1, 'cols': 20, 'readonly': 'readonly'}),
            'pH': Textarea(attrs={'rows': 1, 'cols': 20, 'readonly': 'readonly'}),

            'oxygenFraction': Textarea(attrs={'rows': 1, 'cols': 20, 'readonly': 'readonly'}),
            'respirationRate': Textarea(attrs={'rows': 1, 'cols': 20, 'readonly': 'readonly'}),
            'respiratoryVolume': Textarea(attrs={'rows': 1, 'cols': 20, 'readonly': 'readonly'}),
            'endExpiratoryPressure': Textarea(attrs={'rows': 1, 'cols': 20, 'readonly': 'readonly'}),
            'ventilationMode': Textarea(attrs={'rows': 1, 'cols': 20, 'readonly': 'readonly'}),

            'status': Textarea(attrs={'rows': 2, 'cols': 50, 'readonly': 'readonly'}),
            'sopDiagnoses': Textarea(attrs={'rows': 2, 'cols': 50, 'readonly': 'readonly'}),

            'doctor': Textarea(attrs={'rows': 1, 'cols': 50, 'readonly': 'readonly'}),
            'phone': Textarea(attrs={'rows': 1, 'cols': 25, 'readonly': 'readonly'}),
            'eMail': Textarea(attrs={'rows': 1, 'cols': 50, 'readonly': 'readonly'}),
        }

    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.layout = Layout(HTML('<section><h1>Общая информация</h1>'),
                           Div(
                               Column('organization', style=''),
                               Column('enterDate', style=''),
                               Column('entryDate', style=''),
                               Column('daysUndersupervision', style=''), css_id='div_main'),
                           HTML('</section><section><h1>Информация о пациенте</h1><h4>Персональные данные</h4>'),
                           Div(
                               Column('patientFIO', style=''),
                               Column('male', style=''),
                               Column('age', style=''), css_id='div_pers'),
                           HTML('<h4><a href="#" onclick="antropShow(\'div_antrop\')">Антропометрические '
                                'показатели</a></h4>'),
                           Div(
                               Column('length', style=''),
                               Column('weigth', style=''), css_id='div_antrop'),
                           HTML('<h4><a href="#" onclick="antropShow(\'div_pregant\')">Беременность</a></h4>'),
                           Div(
                               Column('pregantPeriod', style=''),
                               Column('childStatus', style=''), css_id='div_pregant'),
                           HTML('<h4><a href="#" onclick="antropShow(\'div_func\')">Функциональное состояние '
                                'пациента</a></h4>'),
                           Div(
                               Column('bodyTemperature', style=''),
                               Column('breethTemp', style=''),
                               Column('heartRate', style=''),
                               Column('AD', style=''),
                               Column('o2Level', style=''), css_id='div_func'),
                           HTML('<h4><a href="#" onclick="antropShow(\'div_lung\')">Состояние легких</a></h4>'),
                           Div(
                               Column('dyspnea', style=''),
                               Column('cough', style=''),
                               Column('sputum', style=''), css_id='div_lung'),
                           HTML('<h4><a href="#" onclick="antropShow(\'div_analize\')">Показатели анализа крови</a></h4>'),
                           Div(
                               Column('hemoglobin', style=''),
                               Column('leukocytes', style=''),
                               Column('lymphocytes', style=''),
                               Column('platelets', style=''),
                               Column('ESR', style=''),
                               Column('cReactiveProtein', style=''),
                               Column('oxygenTension', style=''),
                               Column('pH', style=''), css_id='div_analize'),
                           HTML(
                               '<h4><a href="#" onclick="antropShow(\'div_breeth\')">Состояние дыхательных функций</a></h4>'),
                           Div(
                               Column('oxygenFraction', style=''),
                               Column('respirationRate', style=''),
                               Column('respiratoryVolume', style=''),
                               Column('endExpiratoryPressure', style=''),
                               Column('ventilationMode', style=''), css_id='div_breeth'),
                           Div(
                               Column('status', style=''),
                               Column('sopDiagnoses', style=''), css_id='div_diagnoses'),
                           Div(
                               Column('doctor', style=''),
                               Column('phone', style=''),
                               Column('eMail', style='')),
                           HTML('</section>'),
                           )
    form_tag = True
    # helper.layout = Layout(Div(Column('organization', style='display:inline-block'),
    #                           Column('enterDate', style='display:inline-block'),
    #                           Column('entryDate', style='display:inline-block')))
