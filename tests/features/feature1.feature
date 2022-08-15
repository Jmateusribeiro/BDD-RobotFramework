Feature: Feature1

  # test comment
  Scenario Outline: Example
    Given email and password are definied as <email> and <password>
    When registration is executed
    Then the correct token is returned: <token>

    Examples:
      | email                      | password | token             |
      | eve.holt@reqres.in         | xpto     | QpwL5tke4Pnpja7X4 |
      | michael.lawson@reqres.in   | xpto     | QpwL5tke4Pnpja7X7 |
      | lindsay.ferguson@reqres.in | xpto     | QpwL5tke4Pnpja7X8 |


  Scenario Template: Same Example
    Given email and password are definied as <email> and <password>
    When registration is executed
    Then the correct token is returned: <token>

    Examples:
      | email                      | password | token             |
      | eve.holt@reqres.in         | xpto     | QpwL5tke4Pnpja7X4 |
      | michael.lawson@reqres.in   | xpto     | QpwL5tke4Pnpja7X7 |
      | lindsay.ferguson@reqres.in | xpto     | QpwL5tke4Pnpja7X8 |

  # comment
  Scenario: Scenario Example
    Given email and password are definied as eve.holt@reqres.in and xpto
    When registration is executed
    Then the correct token is returned: QpwL5tke4Pnpja7X4

  #comment
  Example: Same Example
    Given email and password are definied as eve.holt@reqres.in and xpto
    When registration is executed
    Then the correct token is returned: QpwL5tke4Pnpja7X4
