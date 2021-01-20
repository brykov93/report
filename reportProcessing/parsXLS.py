

import requests
from bs4 import BeautifulSoup
import logging

import xlrd
import psycopg2

import time
#logging.basicConfig(level=logging.DEBUG)


sqls=[    '''DELETE FROM public.report_patients
	WHERE report_patients."patientFIO" = 'пациентов нет' ''',

    '''DELETE FROM public.report_patients
	WHERE report_patients."patientFIO" = '' ''',

    '''DELETE FROM public.report_patients
	WHERE report_patients."patientFIO" = 'нет пациентов' ''',

    '''DELETE FROM public.report_patients
	WHERE report_patients."patientFIO" = '0.0' ''',

    '''DELETE FROM public.report_patients
	WHERE report_patients."patientFIO" = '00' ''',

    '''DELETE FROM public.report_patients
	WHERE report_patients."patientFIO" like '%пациент%' ''',

    '''DELETE FROM public.report_patients
	WHERE report_patients."patientFIO" like '%Пациент%' ''',

    '''DELETE FROM public.report_patients
	WHERE report_patients."patientFIO" like '%больных%' ''',

    '''DELETE FROM public.report_patients
	WHERE report_patients."patientFIO" like '%ПАЦИЕНТОВ%' ''',

    '''DELETE FROM public.report_patients
	WHERE report_patients."patientFIO" like '%пациетов%' ''',

    '''DELETE FROM public.report_patients
	WHERE report_patients."patientFIO" like '%Больных%' ''',

    '''DELETE FROM public.report_patients
	WHERE report_patients."patientFIO" like '%БОЛЬНЫХ%' ''']

url = 'http://report.skmiac.local'
def updateReport():
    try:
        with requests.Session() as session:
            session.trust_env = False
            print('Подключаемся к МИАЦ')
            r = session.get(url)
            cookieJar = session.cookies
            soup = BeautifulSoup(r.content, features="lxml")
            csrftoken = soup.find('input', dict(name='_csrf'))['value']
            login_data = {}
            login_data['_csrf'] = csrftoken
            login_data['LoginForm[username]'] = 'логин report.skmiac.local'
            login_data['LoginForm[password]'] = 'пароль report.skmiac.local'
            login_data['LoginForm[rememberMe]'] = 0
            login_data['LoginForm[rememberMe]'] = 1
            login_data['login-button'] = ''
            print('Вход в РЕПОРТ')
            responsePost=session.post(url+'/site/login', data=login_data)
            print('Вход в РЕПОРТ выполнен')
            print('Скачиваем отчет')
            responseGet = session.get(url+'/report-summary/export-excel?id=1712&reportTemplateTableId=837',
                                      params={'id' : 1712}, cookies=session.cookies)
            print('Сохраняем отчет')
            open('Report.xlsx', 'wb').write(responseGet.content)
            print('Закрываем сессию')
            session.close()
    except:
        print('Ошибка получения отчета')
        return
    try:
        rb = xlrd.open_workbook(r'Report.xlsx')
        sheet = rb.sheet_by_index(0)
    except:
        print('Ошибка открытия отчета')
        return
    conn = psycopg2.connect(database='reportProcessing', user='postgres',
            password='15061993')
    cur = conn.cursor()
    sql = 'DELETE FROM  public.report_patients'
    print('Чистим таблицу')
    cur.execute(sql)
    conn.commit()

    sql = '''INSERT INTO public.report_patients(
    organization, "patientFIO", male, age, length, weigth, "pregantPeriod", "childStatus", "sopDiagnoses", "bodyTemperature", 
    "breethTemp", "heartRate", "AD", "o2Level", dyspnea, cough, sputum, hemoglobin, leukocytes, lymphocytes, platelets, "ESR", 
    "cReactiveProtein", "oxygenTension", "pH", "oxygenFraction", "respirationRate", "respiratoryVolume", "endExpiratoryPressure", 
    "ventilationMode", status, doctor, phone, "eMail", "daysUndersupervision", "enterDate", "entryDate")
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
    %s, %s, %s, %s, %s, %s, %s);'''
    print('Загружаем данные в таблицу')
    for rownum in range(sheet.nrows):
        row = sheet.row_values(rownum)
        if rownum > 0:
            cur.execute(sql, tuple(row))
            conn.commit()
    print('Очищаем ненужные данные')
    for sql in sqls:
        cur.execute(sql)
        conn.commit()
    cur.close()
    conn.close()


firstStep=True
while True:
    if firstStep:
        print('Первый проход, обновляем таблицу')
        pass
    else:
        print('Следующее обновление данных произойдет в через 10 мин.')
        time.sleep(600)
    print('Обновление данных...')
    updateReport()
    print('Обновление данных выполнено.')
    firstStep = False

