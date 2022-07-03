# BDD-RobotFramework-API

#### The aim of this project is show how one can write bdd scenarios in feature files and run that tests scenarios with RobotFramework


* The project read all feature files and leverage Robot framework API to generate robot tests dynamically according to gherkin scenarios.
* Folder tests/features contains all feature files with gherkin scenarios inside.
* Folder tests/step_def contains all files with robot keywords that correspond to the gherkin steps.
* In order to run the tests just need to execute the file main.py and a folder with execution report will be generated.


## Gherkin Sintax:

  This project, for now, only recognize basic gherkin keywords.
  
  Recognized Gherkin keywords:
  
  - Feature;
  - Scenario;
  - Scenario Outline;
  - Examples;
  - Given, When, Then, And, But;
  - | (Data Tables);
  - \# (Comments)
    
  Gherkin Keywords to add:
  
  - Rule;
  - Background;
  - Example;
  - Scenarios;
  - Scenario Template:
  - """ (Doc Strings)
  - @ (Tags)

  
 
  
  



