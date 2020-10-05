#Feature: Showing off behave in sampleTest2 feature file
#
#  Background:
#    Given user open the second app url
#
#  @Sanity @smoke
#  Scenario Outline: Feature 2 Validate login functionality
#    When Enter "<UserID>" and "<Password>"
#    Then user will be logged into application
#    Examples:
#      | UserID                  | Password  |
#      | 2131110038@cs.ku.edu.kw | Amnah1234 |
#
#
#  @Regression  @smoke
#  Scenario Outline: Feature 2 sample test TC2- Validate change password functionality
#    When Login into application using "<UserID>" and "<Password>"
#    And Change password to "<new_Password>"
#    Then Password should be changes sucessfully
#    And Change password back to "<Password>" from "<new_Password>" for "<UserID>"
#    Examples:
#      | UserID                  | Password  | new_Password |
#      | 2131110038@cs.ku.edu.kw | Amnah1234 | pass         |