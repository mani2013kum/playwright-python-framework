Feature: Order Transaction
    Tests Related to Order Transactions


Scenario Outline: Verify Order Success message shown in details
       Given place order with <username> and <password>
       And user is on  landing page
       When I login to portal with <username> and <password>
       And Navigate to orders page
       And select the order
       Then order message is successfully displayed
    Examples:
        | username              | password      |
        | mani2013kum@gmail.com | Manisha@1996  | 

    