Feature: Order API
  Background:
    Given openapi ./api_order_v1.yaml
    And value auth from auth.spec

  Scenario Outline: Fetch product details
    When GET /products/(id:number)
    Then status 200

    Examples:
      | id |
      | 10 |

  Scenario Outline: Update product details
    When POST /products/(id:number)
    Then status 204

    Examples:
      | name     | type   | inventory | id | Authenticate  |
      | XYZ Fone | gadget | 10        | 10 | ($auth.token) |

  Scenario Outline: Delete a product
    When DELETE /products/(id:number)
    Then status 204

    Examples:
      | id | Authenticate  |
      | 20 | ($auth.token) |

  Scenario Outline: Add a new product
    When POST /products
    Then status 201

    Examples:
      | name       | type   | inventory | Authenticate  |
      | XYZ Laptop | gadget | 10        | ($auth.token) |

  Scenario Outline: Search for products
    When GET /products?name=(string)&type=(string)
    Then status 200

    Examples:
      | type   | name |
      | gadget |      |
      | gadget | XYZ  |

  Scenario Outline: Search for products
    When GET /products?name=(string)&type=(string)
    Then status 500

    Examples:
      | type | name |
      | book |      |

  Scenario Outline: Create an order
    When POST /orders
    Then status 201

    Examples:
      | productid | count | status  | Authenticate  |
      | 10        | 1     | pending | ($auth.token) |

  Scenario Outline: Get details of an order
    When GET /orders/(id:number)
    Then status 200

    Examples:
      | id |
      | 10 |

  Scenario Outline: Cancel an order
    When DELETE /orders/(id:number)
    Then status 204

    Examples:
      | id | Authenticate  |
      | 20 | ($auth.token) |

  Scenario Outline: Update details of an order
    When POST /orders/(id:number)
    Then status 204

    Examples:
      | productid | count | status    | id | Authenticate  |
      | 10        | 1     | fulfilled | 10 | ($auth.token) |

  Scenario Outline: Search for orders
    When GET /orders?productid=(number)&status=(string)
    Then status 200

    Examples:
      | productid | status    |
      | 10        | fulfilled |
