"""
Created on Thursday 4/9/20 ‏‎1:30:00 AM
@authors: Hady S. Salama and Jack R. Lynch
Personal Project
"""

from django.shortcuts import render

def home(request):
    risk = ""
    actions = ""
    cc_actions = ""
    gettest = False

    if request.method == 'POST':
        prescreen_checks = request.POST.getlist('covid-check')

        # Important symptoms
        cough = "cough" in prescreen_checks  # Dry Cough
        # Implies the user has Coronavirus in some cases
        shortness_of_breath = "sob" in prescreen_checks
        # Greater than 100.4 (This can be subjective)
        fever = "fever" in prescreen_checks

        # Checks if the user has a Cleveland Clinic Identified High Risk Condition.
        cc_highrisk = request.POST.get("cchighrisk")
        if cc_highrisk is not "none":
            cc_highrisk = True
        else:
            cc_highrisk = False

        # Higher Risk Options
        # User has traveled to an area heavily impacted by COVID-19.
        travel = "travel" in prescreen_checks
        # User has came into contact with a laboratory-confirmed case of COVID-19.
        lab_covid_case = "contact-positive-case" in prescreen_checks
        # User has came into contact with a family memeber or close person that has confirmed COVID-19 outside a healthcare facility.
        family_member_covid = "family-contact-positive-case" in prescreen_checks
        # Recommended precautions for home care and isolation followed consistently.
        household_precautions = "follow-precautions" in prescreen_checks
        # User has been in a confined indoor enviornemnt with a confirmed case greater than 6 feet apart.
        family_member_covid_6feet = "within-6-feet-positive-case" in prescreen_checks
        # User is in a confined enviornment less than 6 feet apart.
        family_member_covid_confined_env = "more-6-feet-positive-case" in prescreen_checks

        # Symptomatic due to Cleveland Clinic Screening
        symptomatic = cough or shortness_of_breath or fever
        gettest = (cough and fever and cc_highrisk) or (cough and shortness_of_breath and cc_highrisk) or (
            fever and cc_highrisk) or (shortness_of_breath and cc_highrisk)

        if gettest:
            cc_actions = "Based on Cleveland Clinic guidelines, it is suggested you contact your doctor immediately."
        else:
            cc_actions = "The Cleveland Clinic does not recommend testing."

        # Nested ifs correspond to the CDC Tree Diagram
        if travel:
            if lab_covid_case:
                risk = "High Risk"
                if symptomatic:
                    actions = "Immediate isolation; medical evaluation guided by PUI Definition; pre-notify healthcare services; controlled travel"
                else:
                    actions = "Remain under quarantine authority; no public activities; daily active monitoring; controlled travel"
            else:
                risk = "Medium Risk"
                if symptomatic:
                    actions = "Immediate isolation; medical evaluation guided by PUI definition; pre-notify healthcare services; control travel"
                else:
                    actions = "Stay home; active monitoring or self muttering with public health supervision; recommended to not travel"
        else:
            if lab_covid_case:
                if family_member_covid:
                    if household_precautions:
                        risk = "Medium Risk"
                        if symptomatic:
                            actions = "Immediate isolation; medical evaluation guided by PUI definition; pre-notify healthcare services; control travel"
                        else:
                            actions = "Stay home; active monitoring or self muttering with public health supervision; recommended to not travel"
                    else:
                        risk = "High Risk"
                        if symptomatic:
                            actions = "Immediate isolation; medical evaluation guided by PUI Definition; pre-notify healthcare services; controlled travel"
                        else:
                            actions = "Remain under quarantine authority; no public activities; daily active monitoring; controlled travel"
                else:
                    if family_member_covid_6feet:
                        risk = "Medium Risk"
                        if symptomatic:
                            actions = "Immediate isolation; medical evaluation guided by PUI definition; pre-notify healthcare services; control travel"
                        else:
                            actions = "Stay home; active monitoring or self muttering with public health supervision; recommended to not travel"
                    else:
                        if family_member_covid_confined_env:
                            risk = "Low Risk"
                            if symptomatic:
                                actions = "Stay home from work or school, avoid contact with others, don't travel. Seek health advice"
                            else:
                                actions = "Self observation"
                        else:
                            risk = "No Identifiable Risk"
                            if symptomatic:
                                actions = "None; routine medical care"
                            else:
                                actions = "None"
            else:
                risk = "No Identifiable Risk"
                if symptomatic:
                    actions = "None; routine medical care"
                else:
                    actions = "None"

    context = {'risk': risk, 'actions': actions, 'cc_actions': cc_actions}
    return render(request, 'dashboard/home.html', context)


def actions(request):
    context = {}
    return render(request, 'dashboard/actions.html', context)