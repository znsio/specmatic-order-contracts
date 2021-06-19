Feature: Petstore auth
    Scenario Outline: Authentication
        When POST /auth
        And request-body
            | username | (string) |
            | password | (string) |
        Then status 200
        And response-body (string)
        And export token = response-body

        Examples:
            | username    | password    |
            | ($username) | ($password) |
