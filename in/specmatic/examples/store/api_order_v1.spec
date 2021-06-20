Feature: Contract for the order API

  Background:
    Given enum ProductType (string) values book,food,gadget,other
    And type Product
      | name | (string)      |
      | type | (ProductType) |
      | id   | (number)      |
    And type Products (Product*)
    And enum OrderStatus (string) values fulfilled,pending
    And type Order
      | productid | (number)      |
      | count     | (number)      |
      | status    | (OrderStatus) |
      | id        | (number)      |
    And type Orders (Order*)
    And value auth from auth.spec

  Scenario Outline: Fetch product details
    When GET /products/(id:number)
    Then status 200
    And response-body (Product)
    Examples:
      | id |
      | 10 |

  Scenario Outline: Update product details
    When POST /products/(id:number)
    And request-header Authenticate (string)
    And request-body (Product)
    Then status 204

    Examples:
      | name     | type   | id | Authenticate  |
      | XYZ Fone | gadget | 10 | ($auth.token) |

  Scenario Outline: Delete a product
    When DELETE /products/(id:number)
    And request-header Authenticate (string)
    Then status 204

    Examples:
      | id | Authenticate  |
      | 20 | ($auth.token) |

  Scenario Outline: Add a new product
    And pattern Product
      | name | (string)      |
      | type | (ProductType) |
    When POST /products
    And request-header Authenticate (string)
    And request-body (Product)
    Then status 201
    And response-body (number)

    Examples:
      | name       | type   | Authenticate  |
      | XYZ Laptop | gadget | ($auth.token) |

  Scenario Outline: Search for products
    When GET /products?name=(string)&type=(ProductType)
    Then status 200
    And response-body (Products)

    Examples:
      | type   | name |
      | gadget |      |
      | gadget | XYZ  |

  Scenario Outline: Create an order
    Given type Order
      | productid | (number)      |
      | count     | (number)      |
      | status    | (OrderStatus) |
    When POST /orders
    And request-header Authenticate (string)
    And request-body (Order)
    Then status 201
    And response-body (number)

    Examples:
      | productid | count | status  | Authenticate  |
      | 10        | 1     | pending | ($auth.token) |

  Scenario Outline: Get details of an order
    When GET /orders/(id:number)
    Then status 200
    And response-body (Order)

    Examples:
      | id |
      | 10 |

  Scenario Outline: Delete an order
    When DELETE /orders/(id:number)
    And request-header Authenticate (string)
    Then status 204

    Examples:
      | id | Authenticate  |
      | 20 | ($auth.token) |

  Scenario Outline: Update details of an order
    When POST /orders/(id:number)
    And request-header Authenticate (string)
    And request-body (Order)
    Then status 204

    Examples:
      | productid | count | status    | id | Authenticate  |
      | 10        | 1     | fulfilled | 10 | ($auth.token) |

  Scenario Outline: Search for orders
    When GET /orders?productid=(number)&status=(OrderStatus)
    Then status 200
    And response-body (Orders)

    Examples:
      | productid | status    |
      | 10        | fulfilled |

  Scenario Outline: Add inventory
    When POST /inventory
    And request-header Authenticate (string)
    And request-body
      | productid | (number) |
      | quantity  | (number) |
    Then status 204

    Examples:
      | productid | quantity | Authenticate  |
      | 10        | 5        | ($auth.token) |

  Scenario Outline: Query inventory
    When GET /inventory?productid=(number)
    Then status 200
    And response-body (number)

    Examples:
      | productid |
      | 10        |