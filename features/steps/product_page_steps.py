from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open GetTop product {product_id} page')
def open_amazon_product(context, product_id):
    context.driver.get(f'https://www.gettop.us/product/{product_id}/')

@given('Open GetTop {category_id} product page')
def open_amazon_category_page(context, category_id):
    context.driver.get(f'https://www.gettop.us/product-category/{category_id}/')

@given('Click on Home link')
def click_home_link(context):
    # context.driver.find_element(By.XPATH, "//a[(@href='https://gettop.us')]").click()
    context.app.product_page.click_home_link()

@then('Verify user is redirected to GetTop home page')
def verify_base_url(context):
    assert 'https://gettop.us/' in context.driver.current_url, \
        f'Url https://gettop.us/ not in {context.driver.current_url}'
