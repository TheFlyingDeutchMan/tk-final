Feature: Customer Name Validation

Scenario Outline: Customer Name Field
    Given a name <name>
    then validate_name should return <result>

Examples: Single Name
    | name    | result |
    | Fred    | True   |
    | J       | False  |
    | Mo      | True   |
    | 2       | False  |
    | Fred Jr | True   |
    | 2b      | False  |
    | Jo      | True   |
    |         | False  |
