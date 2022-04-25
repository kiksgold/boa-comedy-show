# BOA Comedy Show 

Boa Comedy Show is a python survey input that collects sales numbers from the user, calculate unsold tickets and recommend sales numbers for each caetgory of tickets for their future event.

## Introduction
The show is an annual comedy show that sells different categories of tickets for their event.

<p>For each event the organizers pre-sell tickets, if they sell out of a particular category, the organizers print more tickets to sell while the unsold ones are thrashed after the event.</p>

## Our main goal
Our goal is to save the company some time by automating a repetitive task and help reduce the unsold tickets by better predicting ticket sales for future events.

## Here is the live version of my project.

![ImageHere]()

## How it works
<ul>
<li>
Our program will collect ticket-sales numbers from the user
</li>
<li>
Validate the numbers collected are integers and valid
</li>
<li>
The numbers will be added to our ticket-sales worksheet
</li>
<li>
We will then calculate the unsold tickets
</li>
<li>
Update the unsold tickets worksheet
</li>
<li>
Calculate the average ticket sales for the last 3 events
</li>
<li>
Update calculated future-tickets numbers into the future-tickets worksheet
</li>
<li>
Print Recommendations
</li>
</ul>

## Features
<ul>
    <li>Request ticket sales numbers from the user
    </li>
        <ul>
        <li>validate numbers to ensure the user has provided exactly 3 numbers
        </li>
        <li>validate numbers to ensure the values are all integers
        </li>
        <li>create while loop to repeat request for numbers until valid
        </li>
        <li>update our ticket worksheet
        </li>
        </ul>

![ImageHere]()

   <li>Calculate the unsold-tickets
    </li>
        <ul>
        <li>compare tickets sold with the inventory inorder to calculate the unsold (if any) for each category
        </li>
        <li>calculate the unsold tickets
        </li>
        <li>updates the unsold worksheet in our spreadsheet
        </li>
        </ul>

![ImageHere]()

<li>Calculate inventory based on averages from the last 3 events
</li>
    <ul>
    <li>calculate the average inventory
    </li>
    <li>the user adds a 20% margin to the calculated averages for future events
    </li>
    <li>updates our inventory worksheet
    </li>
    <li>make recommendations
    </li>
    </ul>

![ImageHere]()    
    
</ul>


## Data Model
<p> We imported a spreadsheet from google sheet, where we have our survey data </p>
<p>Our spreadsheet has 3 columns for the different categories of ticket-sales</p>
<p>It contains 10 rows of numbers from past events</p>
<p>It has 3 worksheets for ticket-sales, unsold tickets and future-tickets </p>

## Testing
I have manually tested this project by doing the following:
<ul>
<li>
</li>
<li>
</li>
</ul>

## Bugs


## Validator Testing


## Deployment


## Credits