Feature: Email Validation

Scenario Outline: Customer Email Field
    Given an email <email>
    then validate_email should return <result>

Examples: Email
    | email             | result |
    | Fred@gmail.com    | True   |
    | Fred@             | False  |
    | Fred-jr@gmail.com | True   |
    | @gmail.com        | False  |
    | tim.gerschner@kc.school.nz | True |
