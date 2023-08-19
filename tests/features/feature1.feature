Feature: Feature1

  # test comment
  Scenario Outline: Example
    Given email and password are definied as <email> and <password>
    When registration is executed
    Then the correct token is returned

    Examples:
      | email                      | password |
      | eve.holt@reqres.in         | xpto     |
      | michael.lawson@reqres.in   | xpto     |
      | lindsay.ferguson@reqres.in | xpto     |


  Scenario Template: Same Example
    Given email and password are definied as <email> and <password>
    When registration is executed
    Then the correct token is returned

    Examples:
      | email                      | password |
      | eve.holt@reqres.in         | xpto     |
      | michael.lawson@reqres.in   | xpto     |
      | lindsay.ferguson@reqres.in | xpto     |

  # comment
  Scenario: Scenario Example
    Given email and password are definied as eve.holt@reqres.in and xpto
    When registration is executed
    Then the correct token is returned

  #comment
  Example: Same Example
    Given email and password are definied as eve.holt@reqres.in and xpto
    When registration is executed
    Then the correct token is returned
