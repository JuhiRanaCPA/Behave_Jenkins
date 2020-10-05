@fixture.browser.Chrome
Feature: Showing off behave  in sampleTest1 feature file

  Background:
    Given user open the url

    @Sanity
  Scenario: Feature 1 sample test Tc1 -Sample Google search testcase
    When user search for python
    And user select python.or site link
    Then user will be on python.or site and the title should be "Welcome to Python.org"

 @Regression @Sanity
  Scenario Outline: Feature 1 sample test TC2- Sample Google search testcase for with parameterization
    When user search for "<search_text>"
    And user select "<link>" site link
    Then the title should be "<Title>"
    Examples:
      | search_text | Title                 | link       |
      | python      | Welcome to Python.org | python.org |
      | India       | India - Wikipedia     | wikipedia  |