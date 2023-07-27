Feature: AutomationPractice
  Background:
    Given que ingreso a la pagina AutomationPractice

  Scenario Outline: Prueba Automatizada
    When Select "<country>" automatically completing with your two initials
    When Select Option 1 and Option 2 in the dropdown
    When Verify money back guarantee in qaclickacademy
    When Tab control and button screenshot
    When Send your "<name>" to the Alert
    When Get and show the courses at this "<price>"
    When Get me all the people with the "<position>"
    When Get text from iFrame
    
    
    
    Examples:

      | country  |   name     | price |  position |     
      | Mexico   | Stori Card |  25   | Engineer | 

