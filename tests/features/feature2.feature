Feature: Registration


  Scenario Outline: Successful Registration
    Given email and password are definied as <email> and <password>
    When registration is executed
    Then the correct token is returned: <token>

    Examples:
      | email                      | password | token             |
      | eve.holt@reqres.in         | xpto     | QpwL5tke4Pnpja7X4 |
      | michael.lawson@reqres.in   | xpto     | QpwL5tke4Pnpja7X7 |
      | lindsay.ferguson@reqres.in | xpto     | QpwL5tke4Pnpja7X8 |