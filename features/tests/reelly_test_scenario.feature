# Created by rachael at 1/15/25
Feature:

Scenario: User can filter by sale status Out of Stocks
  Given Open Reelly Main Page
  Then Log in to the page
  Then Click “off plan” at the left side menu
  Then Verify Correct Page Opened
  Then Click on Sale Status Filter
  When Change Sale Status to “Out of Stocks”
  Then Verify Each Product Contains Out Of Stock Tag