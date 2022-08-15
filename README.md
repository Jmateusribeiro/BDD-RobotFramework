# BDD-RobotFramework-API

#### The aim of this project is show how one can write bdd scenarios in feature files and run that tests scenarios with RobotFramework


* The project read all feature files and leverage Robot framework API to generate robot tests dynamically according to gherkin scenarios.
* Folder tests/features contains all feature files with gherkin scenarios inside.
* Folder tests/step_def contains all files with robot keywords that correspond to the gherkin steps.
* In order to run the tests just need to execute the file main.py and a folder with execution report will be generated.


### If one want to reuse the project just need to put the feature files inside the features folder and the robot keywords file inside step_defs folder


## Gherkin Sintax:

  This project, for now, only recognize the most used gherkin keywords.
  
  Recognized Gherkin keywords:
  
  - Feature;
  - Scenario / Example;
  - Scenario Outline / Scenario Template;
  - Examples Table;
  - Given, When, Then, And, But;
  - \# (Comments)
    
  Gherkin Keywords to add:
  
  - Rule;
  - Background;
  - """ (Doc Strings)
  - @ (Tags)
  - | (Data Tables)

  
 
  
  



