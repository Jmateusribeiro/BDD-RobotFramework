Feature: Registration


  Scenario Outline: Successful Registration
    Given email and password are definied as <email> and <password>
    When registration is executed
    Then the correct token is returned

    Examples:
      | email                      | password |
      | eve.holt@reqres.in         | xpto     |
      | michael.lawson@reqres.in   | xpto     |
      | lindsay.ferguson@reqres.in | xpto     |