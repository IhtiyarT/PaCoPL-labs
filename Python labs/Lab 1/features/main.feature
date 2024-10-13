Feature: Biquadratic equation solving
  As a user I want to solve equation

  Scenario: User gets correct ans with 4 roots
    When User passes arguments "1 -13 36"
    Then Result is "3 -3 2 -2

  Scenario: User gets correct ans with 3 ans
    When User passes arguments "-4 36 0"
    Then Result is "0 3.0 -3.0

  Scenario: User gets correct ans with 2 ans
    When User passes arguments "1 -50 625"
    Then Result is "5.0 -5.0

  Scenario: User gets correct ans with 1 ans
    When User passes arguments "170 0 0"
    Then Result is "0
