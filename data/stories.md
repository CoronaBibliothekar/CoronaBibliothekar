## what is
* what_is{"topic": "corona"}
    - action_what_is

## what is 2x
* what_is{"topic": "corona"}
    - action_what_is
* what_is{"topic": "covid"}
    - action_what_is

## difference
* difference{"topic": "mers"}
    - action_difference
    
## difference 2x
* difference{"topic": "sars"}
    - action_difference
* difference{"topic": "flu"}
    - action_difference
    
## what is difference
* what_is{"topic": "covid"}
    - action_what_is
* difference{"topic": "flu"}
    - action_difference
    
## difference what is
* difference{"topic": "sars"}
    - action_difference
* what_is{"topic": "covid"}
    - action_what_is

## currently infected
* current_infected
    - action_current_infected
    
## greet
* greet
    - utter_greet
    
## goodbye
* goodbye
    - utter_bye

## currently dead
* current_deaths
    - action_current_deaths
    
## currenly bundeslaender
* current_bundeslaender
    - action_current_bundeslaender
    
    
## virus origin
* virus_origin
    - utter_virus_origin
    
## propability infection
* prpability_infection
    - utter_prpability_infection
    
## infection_behavior
* infection_behavior
    - utter_infection_behavior
    
## antibiotics
* antibiotics
    - utter_antibiotics
    
## vaccine
* vaccine
    - utter_vaccine
    
## vaccine and antibiotics
* vaccine
    - utter_vaccine
* antibiotics
    - utter_antibiotics    

## mix
* greet
    - utter_greet
* current_infected
    - action_current_infected
* current_deaths
    - action_current_deaths
* current_bundeslaender
    - action_current_bundeslaender
* current_deaths
    - action_current_deaths
* vaccine
    - utter_vaccine
* antibiotics
    - utter_antibiotics
* virus_origin
    - utter_virus_origin
* what_is{"topic": "corona"}
    - action_what_is
* what_is{"topic": "covid"}
    - action_what_is
* goodbye
    - utter_bye
    
## more conversations 1
* current_deaths
    - action_current_deaths
* vaccine
    - utter_vaccine
* antibiotics
    - utter_antibiotics
* virus_origin
    - utter_virus_origin
