from django.shortcuts import render

def home(request):
<<<<<<< HEAD
    context = {}
    return render(request, 'dashboard/home.html', context)

def about(request):
    context = {}
    return render(request, 'dashboard/about.html', context)
=======

    # Important symptoms
    cough = False # Dry Cough
    shortness_of_breath = False # Implies the patient has Coronavirus in some cases
    fever = False # Greater than 100.4 (This can be subjective)

    # Higher Risk Options
    travel = False # User has traveled to an area heavily impacted by COVID-19.
    lab_covid_case = False # User has came into contact with a laboratory-confirmed case of COVID-19.
    family_member_covid = False # User has came into contact with a family memeber or close person that has confirmed COVID-19 outside a healthcare facility.
    household_precautions = False # Recommended precautions for home care and isolation followed consistently.
    family_member_covid_6feet = False # User has been in a confined indoor enviornemnt with a confirmed case greater than 6 feet apart.
    family_member_covid_confined_env = False #In a confined enviornment less than 6 feet apart.

    symptomatic = False #Symptomatic due to Cleveland Clinic Screening
    risk = ""

    if((not travel) and (not lab_covid_case) and (not symptomatic)):
        risk = "None"
    elif((not travel) and (not lab_covid_case) and symptomatic):
        risk = "None; routine medical care"
    elif((not travel) and (lab_covid_case)  and (not family_member_covid) and (not family_member_covid_6feet) and symptomatic):
        risk = "None; routine medical care"



    if request.method == 'POST':
        prescreen_checks = request.POST.getlist('covid-check')
        print(prescreen_checks)

    context = {}
    return render(request, 'dashboard/home.html', context)
>>>>>>> f7e61110e25b35eeacf4d2715058d4db4e9e7b8f
