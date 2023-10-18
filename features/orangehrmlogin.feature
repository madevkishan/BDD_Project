Feature: OrangeHRM Logo
    Scenario: Logo presence on OrangeHRM Home Page
    Given Launch Chrome Browser
    When Open OrangeHRM HomePage
    And Enter username '{user}' and password '{pwd}'
    And click on login button
    Then User must sucuessfully login to the Dashboard page
    Then Close Browser