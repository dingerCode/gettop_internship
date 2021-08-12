# Created by aj at 8/12/21
Feature: Product Page Tests
  # Enter feature description here

  Scenario Outline: Home Link takes user to Home Page from product page
    Examples:
    |product_id|
    |macbook-pro-13|
    |macbook-pro-16|
    |macbook-air   |
    |iphone-11     |
    |iphone-11pro  |
    |iphone-se     |
    |ipad          |
    |ipad-pro      |
    |ipad-mini     |
    |ipad-air      |
    |ss-crew-california-sub-river-island|
    |land-tee-jack-jones                |
    |airpods                            |
    |airpods-pro                        |
    Given Open GetTop product <product_id> page
    And Click on Home link
    Then Verify user is redirected to GetTop home page

  Scenario Outline: Home Link takes user to Home Page from product category page
    Examples:
    |category|
    |macbook |
    |iphone  |
    |ipad    |
    |accessories/watch|
    |accessories/airpods|
    Given Open GetTop <category> product page
    And Click on Home link
    Then Verify user is redirected to GetTop home page