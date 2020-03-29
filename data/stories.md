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
* current_numbers
    - action_current_numbers
    
* smalltalk
    - respond_smalltalk

## currently dead
* current_numbers
    - action_current_numbers
    
## currenly bundeslaender
* current_bundeslaender
    - action_current_bundeslaender
    
    
## mix
* smalltalk
    - respond_smalltalk
* current_numbers{"location": "Berlin"}
    - action_current_numbers
* current_numbers
    - action_current_numbers{"location": "Deutschland"}
* current_bundeslaender
    - action_current_bundeslaender
* current_numbers
    - action_current_numbers
* faq
    - respond_faq
* what_is{"topic": "corona"}
    - action_what_is
* what_is{"topic": "covid"}
    - action_what_is
* smalltalk
    - respond_smalltalk

## faq
* faq
    - respond_faq
    
## faq multiple
* faq
    - respond_faq
* faq
    - respond_faq
* faq
    - respond_faq
    
## smalltalk smalltalk smalltalk
* smalltalk
    - respond_smalltalk
* smalltalk
    - respond_smalltalk
* smalltalk
    - respond_smalltalk