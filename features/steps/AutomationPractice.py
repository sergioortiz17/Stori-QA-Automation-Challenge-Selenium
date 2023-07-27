from behave import *

from web.applications import Application
from support.BaseActions import BaseActions


@given(u'que ingreso a la pagina AutomationPractice')
def step_impl(context):
    try:
        context.application = Application(context.driver)
    except AssertionError as ex:
        context.driver.close()
        assert False, "Fallo el inicio de navegador\n" \
                      f" la informacion concreta del error es: {ex}"

@when(u'Select "{country}" automatically completing with your two initials')
def step_impl(context, country):
    try:
        context.application.PracticePage.insertCountry(country)
        
    except AssertionError as ex:
        context.driver.close()
        assert False, "Fallo el inicio de navegador\n" \
                      f" la informacion concreta del error es: {ex}"
        
@when(u'Select Option 1 and Option 2 in the dropdown')
def step_impl(context):
    try:
        context.application.PracticePage.selectOptionsDropDown()
        
    except AssertionError as ex:
        context.driver.close()
        assert False, "Fallo el inicio de navegador\n" \
                      f" la informacion concreta del error es: {ex}"    

@when(u'Verify money back guarantee in qaclickacademy')
def step_impl(context):
    try:
        context.application.PracticePage.verifyMoneyBackGuaranteeinQaclickacademy()
        
    except AssertionError as ex:
        context.driver.close()
        assert False, "Fallo el inicio de navegador\n" \
                      f" la informacion concreta del error es: {ex}"    

@when(u'Tab control and button screenshot')
def step_impl(context):
    try:
        context.application.PracticePage.openTabAndScreenshot() #posible improve para iframePage and QaAcademyPage
        
    except AssertionError as ex:
        context.driver.close()
        assert False, "Fallo el inicio de navegador\n" \
                      f" la informacion concreta del error es: {ex}"  
        
@when(u'Send your "{name}" to the Alert')
def step_impl(context, name):
    try:
        context.application.PracticePage.verify_name_in_Alert_expected(name)
        
    except AssertionError as ex:
        context.driver.close()
        assert False, "Fallo el inicio de navegador\n" \
                      f" la informacion concreta del error es: {ex}"  

@when(u'Get and show the courses at this "{price}"')
def step_impl(context, price):
    try:
        context.application.PracticePage.count_and_get_courses_for_this_price(price)
        
    except AssertionError as ex:
        context.driver.close()
        assert False, "Fallo el inicio de navegador\n" \
                      f" la informacion concreta del error es: {ex}"          


@when(u'Get me all the people with the "{position}"')
def step_impl(context, position):
    try:
        context.application.PracticePage.count_and_get_people_whit_this_position(position)
        
    except AssertionError as ex:
        context.driver.close()
        assert False, "Fallo el inicio de navegador\n" \
                      f" la informacion concreta del error es: {ex}"       

@when(u'Get text from iFrame')
def step_impl(context):
    try:
        context.application.PracticePage.getTextInsideiFrame()
        
    except AssertionError as ex:
        context.driver.close()
        assert False, "Fallo el inicio de navegador\n" \
                      f" la informacion concreta del error es: {ex}"             

