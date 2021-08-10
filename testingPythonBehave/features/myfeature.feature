Feature: Search bar

  Scenario Outline: Navigate through products
    Given open browser
    When navigate through product "<category>"
    Then display results

    Examples:
      | category |
      | Phones   |
      | Laptops  |
      | Monitors |

  Scenario: Navigate through laptops
    Given open browser
    When navigate through product "Laptops"
    Then display results

  Scenario: Add laptops to cart,remove and pay
    Given open browser
    When navigate through product "Laptops"
    And add laptop "Dell i7 8gb"
    And go to homepage
    And navigate through product "Laptops"
    And add laptop "Sony vaio i5"
    And go to cart
    And delete laptop "Dell i7 8gb"
    And place order
      | name | country | city      | card          | year | month |
      | radu | romania | bucharest | 3243243253456 | 24   | 12    |
    Then verify amount



