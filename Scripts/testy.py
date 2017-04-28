# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import StaleElementReferenceException
import unittest
import time

# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

SLEEP_TIME_BASE = 1
TIMEOUT_TIME_BASE = 5
IMPLICIT_WAIT = 15
MENU_RETRIES = 3
TABLE_RETRIES = 5
STORE_RETRIES = 3


class Testy(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Remote(
            command_executor='http://mys01.fit.vutbr.cz:4444/wd/hub',
            desired_capabilities={
                "desiredCapabilities": {
                    "browserName": "firefox",
                    "javascriptEnabled": True,
                    "version": "",
                    "platform": "ANY"
                }
            }
        )
        self.driver.implicitly_wait(IMPLICIT_WAIT)
        self.base_url = "http://mys01.fit.vutbr.cz:8038/admin/"
        self.verificationErrors = []
        self.accept_next_alert = True

###############################################################
# TESTS
###############################################################

    def test_shouldFilterQuantity0SamsungTablet(self):
        driver = self.driver
        driver.get(self.base_url)

        # Get to the product list
        self.login_to_admin()
        self.open_products_tab()

        # Do the filtering
        self.filter_text_input("input-quantity", "0")

        # Check the results
        self.assertEqual("Samsung Galaxy Tab 10.1",
                         driver.find_element_by_css_selector("tbody > tr > td.text-left").text)
        self.expect_missing_element(By.CSS_SELECTOR, "tbody tr:nth-child(2)")

        # Logout
        self.logout_from_admin()

    def test_shouldFilterPrice80NikonCamera(self):
        driver = self.driver
        driver.get(self.base_url)

        # Get to the product list
        self.login_to_admin()
        self.open_products_tab()

        # Do the filtering
        self.filter_text_input("input-price", "80")

        # Check the results
        self.assertEqual("Nikon D300",
                         driver.find_element_by_css_selector("tbody > tr > td.text-left").text)
        self.expect_missing_element(By.CSS_SELECTOR, "tbody tr:nth-child(2)")

        # Logout
        self.logout_from_admin()

    def test_shouldFilterStatusDisabledNoResults(self):
        driver = self.driver
        driver.get(self.base_url)

        # Get to the product list
        self.login_to_admin()
        self.open_products_tab()

        # Do the filtering
        self.filter_dropdown_input("input-status", "Disabled")

        # Check the results
        self.assertEqual("No results!", driver.find_element_by_css_selector("tbody > tr > td.text-center").text)

        # Logout
        self.logout_from_admin()

    def test_shouldFilterProductNameSonyVAIO(self):
        driver = self.driver
        driver.get(self.base_url)

        # Get to the product list
        self.login_to_admin()
        self.open_products_tab()

        # Do the filtering
        self.filter_text_input("input-name", "Sony VAIO")

        # Check the results
        self.assertEqual("Sony VAIO",
                         driver.find_element_by_css_selector("tbody > tr > td.text-left").text)
        self.expect_missing_element(By.CSS_SELECTOR, "tbody tr:nth-child(2)")

        # Logout
        self.logout_from_admin()

    def test_shouldFilterModelProduct18MacBookPro(self):
        driver = self.driver
        driver.get(self.base_url)

        # Get to the product list
        self.login_to_admin()
        self.open_products_tab()

        # Do the filtering
        self.filter_text_input("input-model", "Product 18")

        # Check the results
        self.assertEqual("MacBook Pro",
                         driver.find_element_by_css_selector("tbody > tr > td.text-left").text)
        self.expect_missing_element(By.CSS_SELECTOR, "tbody tr:nth-child(2)")

        # Logout
        self.logout_from_admin()

    def test_shouldAddPalmTreoProSpecial(self):
        driver = self.driver
        driver.get(self.base_url)

        # Get to the product list
        self.login_to_admin()
        self.open_products_tab()

        # Check if the product exists and does not already have special
        row = self.find_first_product_by_name("Palm Treo Pro")
        self.expect_missing_element(By.CSS_SELECTOR, "tr:nth-child({0}) .text-danger".format(row))

        # Add the special
        self.add_special(row, "249.9999")

        # Check the results
        self.assertEqual("249.9999", driver.find_element_by_xpath(
            "//form[@id='form-product']/div/table/tbody/tr[{0}]/td[5]/div".format(row)).text)

        # Do the cleanup - remove the special
        self.remove_special(row, 0)

        # Logout
        self.logout_from_admin()

    def test_shouldAddHPLP3065SpecialNotNumber(self):
        driver = self.driver
        driver.get(self.base_url)

        # Get to the product list
        self.login_to_admin()
        self.open_products_tab()

        # Check if the product exists and does not already have special
        row = self.find_first_product_by_name("HP LP3065")
        self.expect_missing_element(By.CSS_SELECTOR, "tr:nth-child({0}) .text-danger".format(row))

        # Add the special
        self.add_special(row, "nan")

        # Check the results
        self.assertEqual("0.0000", driver.find_element_by_xpath(
            "//form[@id='form-product']/div/table/tbody/tr[{0}]/td[5]/div".format(row)).text)

        # Do the cleanup - remove the special
        self.remove_special(row, 0)

        # Logout
        self.logout_from_admin()

    def test_shouldAddHTCTouchHDSpecialNegative(self):
        driver = self.driver
        driver.get(self.base_url)

        # Get to the product list
        self.login_to_admin()
        self.open_products_tab()

        # Check if the product exists and does not already have special
        row = self.find_first_product_by_name("HTC Touch HD")
        self.expect_missing_element(By.CSS_SELECTOR, "tr:nth-child({0}) .text-danger".format(row))

        # Add the special
        self.add_special(row, "-100.0")

        # Check the results
        self.assertEqual("-100.0000", driver.find_element_by_xpath(
            "//form[@id='form-product']/div/table/tbody/tr[{0}]/td[5]/div".format(row)).text)

        # Do the cleanup - remove the special
        self.remove_special(row, 0)

        # Logout
        self.logout_from_admin()

    def test_shouldAddPalmTreoProDiscount2Pieces(self):
        driver = self.driver
        driver.get(self.base_url)

        # Get to the product list
        self.login_to_admin()
        self.open_products_tab()

        # Check if the product exists and add the discount
        row = self.find_first_product_by_name("Palm Treo Pro")
        self.add_discount(row, "2", "229.9999")
        self.logout_from_admin()

        # Check the results in store
        details = self.locate_product_in_store(
            By.CSS_SELECTOR, ".list-group-item:nth-child(6)", By.LINK_TEXT, "Palm Treo Pro")
        self.assertTrue("2 or more" in details)

        # Do the cleanup - remove the discount
        driver.get(self.base_url)
        self.login_to_admin()
        self.open_products_tab()
        self.remove_discount(row, 0)

        # Logout
        self.logout_from_admin()

    def test_shouldAddiPodShuffleDiscount0(self):
        driver = self.driver
        driver.get(self.base_url)

        # Get to the product list
        self.login_to_admin()
        self.open_products_tab()

        # Check if the product exists and add the discount
        row = self.find_first_product_by_name("iPod Shuffle")
        self.add_discount(row, "0", "20")
        self.logout_from_admin()

        # Check the results in store
        details = self.locate_product_in_store(
            By.CSS_SELECTOR, ".list-group-item:nth-child(8)", By.LINK_TEXT, "iPod Shuffle")
        self.assertFalse("0 or more" in details)

        # Do the cleanup - remove the discount
        driver.get(self.base_url)
        self.login_to_admin()
        self.open_products_tab()
        self.remove_discount(row, 0)

        # Logout
        self.logout_from_admin()

    def test_shouldRemoveAppleCinemaDiscount20Pieces(self):
        driver = self.driver
        driver.get(self.base_url)

        # Get to the product list
        self.login_to_admin()
        self.open_products_tab()

        # Check if the product exists and remove the discount
        row = self.find_first_product_by_name("Apple Cinema 30\"")
        self.remove_discount(row, 1)
        self.logout_from_admin()

        # Check if the discount is not present in the store
        details = self.locate_product_in_store(
            By.CSS_SELECTOR, ".list-group-item:nth-child(1)", By.LINK_TEXT, "Apple Cinema 30\"")
        self.assertFalse("20 or more" in details)

        # Do the cleanup - add the discount back
        driver.get(self.base_url)
        self.login_to_admin()
        self.open_products_tab()
        self.add_discount(row, "20", "77.0000", "1")

        # Logout
        self.logout_from_admin()

    def test_shouldRemoveAppleCinemaSpecial(self):
        driver = self.driver
        driver.get(self.base_url)

        # Get to the product list
        self.login_to_admin()
        self.open_products_tab()

        # Check if the product exists and has a special
        row = self.find_first_product_by_name("Apple Cinema 30\"")
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "tr:nth-child({0}) .text-danger".format(row)))

        # Remove the special
        self.remove_special(row, 0)

        # Check if the special is missing
        self.expect_missing_element(By.CSS_SELECTOR, "tr:nth-child({0}) .text-danger".format(row))

        # Do the cleanup - create the special
        self.add_special(row, "90.0000")

        # Logout
        self.logout_from_admin()

    def test_shouldEditiMacQuantityTo1000(self):
        driver = self.driver
        driver.get(self.base_url)

        # Get to the product list
        self.login_to_admin()
        self.open_products_tab()

        # Check if the product exists and the quantity is different than 1000
        row = self.find_first_product_by_name("iMac")
        self.assertNotEqual("1000", driver.find_element_by_xpath(
            "//form[@id='form-product']/div/table/tbody/tr[{0}]/td[6]/span".format(row)).text)

        # Set the quantity
        self.edit_parameter(row, "Data", "input-quantity", "1000")

        # Check if the quantity was set
        self.assertEqual("1000", driver.find_element_by_xpath(
            "//form[@id='form-product']/div/table/tbody/tr[{0}]/td[6]/span".format(row)).text)

        # Do the cleanup - change the quantity back
        self.edit_parameter(row, "Data", "input-quantity", "977")

        # Logout
        self.logout_from_admin()

    # TODO: rename in testplan / report
    def test_shouldEditiPodNanoQuantityNegative(self):
        driver = self.driver
        driver.get(self.base_url)

        # Get to the product list
        self.login_to_admin()
        self.open_products_tab()

        # Check if the product exists and if the quantity is not -10
        row = self.find_first_product_by_name("iPod Nano")
        self.assertNotEqual("-10", driver.find_element_by_xpath(
            "//form[@id='form-product']/div/table/tbody/tr[{0}]/td[6]/span".format(row)).text)

        # Set the quantity
        self.edit_parameter(row, "Data", "input-quantity", "-10")

        # Check if the quantity was set
        self.assertEqual("-10", driver.find_element_by_xpath(
            "//form[@id='form-product']/div/table/tbody/tr[{0}]/td[6]/span".format(row)).text)

        # Do the cleanup - change the quantity back
        self.edit_parameter(row, "Data", "input-quantity", "994")

        # Logout
        self.logout_from_admin()

    def test_shouldEditSamsungTabletOutOfStockStatus(self):
        driver = self.driver
        driver.get(self.base_url)

        # Get to the product list
        self.login_to_admin()
        self.open_products_tab()

        # Check if the product exists and check if the quantity is 0
        row = self.find_first_product_by_name("Samsung Galaxy Tab 10.1")
        self.assertEqual("0", driver.find_element_by_xpath(
            "//form[@id='form-product']/div/table/tbody/tr[{0}]/td[6]/span".format(row)).text)

        # Set the Out Of Stock status
        self._change_out_of_stock_status(row, "Out Of Stock")
        self.logout_from_admin()

        # Check the status in the store
        self.locate_product_in_store(
            By.CSS_SELECTOR, ".list-group-item:nth-child(4)", By.LINK_TEXT, "Samsung Galaxy Tab 10.1")
        self.assertEqual("Availability: Out Of Stock",
                         driver.find_element_by_xpath("//div[@id='content']/div/div[2]/ul/li[3]").text)

        # Do the cleanup - change the status back
        driver.get(self.base_url)
        self.login_to_admin()
        self.open_products_tab()
        self._change_out_of_stock_status(row, "Pre-Order")

        # Logout
        self.logout_from_admin()

    def test_shouldEditiPhonePriceTo150(self):
        driver = self.driver
        driver.get(self.base_url)

        # Get to the product list
        self.login_to_admin()
        self.open_products_tab()

        # Check if product exists and if the price is not 150.0000
        row = self.find_first_product_by_name("iPhone")
        self.assertNotEqual("150.0000", driver.find_element_by_xpath(
            "//form[@id='form-product']/div/table/tbody/tr[{0}]/td[5]".format(row)).text)

        # Set the new price
        self.edit_parameter(row, "Data", "input-price", "150.0000")

        # Check if the price was set
        self.assertEqual("150.0000", driver.find_element_by_xpath(
            "//form[@id='form-product']/div/table/tbody/tr[{0}]/td[5]".format(row)).text)

        # Do the cleanup - change the price back
        self.edit_parameter(row, "Data", "input-price", "101.0000")

        # Logout
        self.logout_from_admin()

    def test_shouldAddProductAligatorPhone(self):
        driver = self.driver
        driver.get(self.base_url)

        # Get to the product list
        self.login_to_admin()
        self.open_products_tab()

        # Check if the product already exists
        self.check_product_not_exists("Aligator Phone")

        # Add the Aligator Phone
        self.add_product("Aligator Phone", "Aligator Phone", "Model 1")

        # Check if the product was inserted
        row = self.check_product_exists_once("Aligator Phone")

        # Do the cleanup - remove the product
        self.remove_product(row)

        # Logout
        self.logout_from_admin()

    def test_shouldCopyProduct8(self):
        driver = self.driver
        driver.get(self.base_url)

        # Get to the product list
        self.login_to_admin()
        self.open_products_tab()

        # Check if the product exists
        row = self.check_product_exists_once("Product 8")

        # Copy the product
        self.copy_product(row)

        # Check if the product is duplicated
        if self.count_products_by_name("Product 8") != 2:
            print "\nERROR: Product count is not 2"
            self.assertEqual(True, False)

        # Do the cleanup - remove the duplicate
        row = self.find_first_product_by_name("Product 8", "Disabled")
        self.remove_product(row)

        # Logout
        self.logout_from_admin()

    def test_shouldRemoveProductMacBook(self):
        driver = self.driver
        driver.get(self.base_url)

        # Get to the product list
        self.login_to_admin()
        self.open_products_tab()

        # Check if the product exists
        row = self.check_product_exists_once("MacBook")

        # Remove the product
        self.remove_product(row)

        # Check if product is gone
        self.check_product_not_exists("MacBook")

        # Do the cleanup - insert the product back (with different parameters)
        self.add_product("MacBook", "MacBook", "Product 16")

        # Logout
        self.logout_from_admin()

###############################################################
# HELPERS
###############################################################

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException:
            return False
        return True
    
    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException:
            return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def login_to_admin(self):
        # Login to the admin section
        self.driver.find_element_by_id("input-username").clear()
        self.driver.find_element_by_id("input-username").send_keys("admin")
        self.driver.find_element_by_id("input-password").clear()
        self.driver.find_element_by_id("input-password").send_keys("admin")
        self.driver.find_element_by_css_selector("button.btn.btn-primary").click()
        time.sleep(SLEEP_TIME_BASE)

    def logout_from_admin(self):
        # Logout from the admin section
        self.driver.find_element_by_link_text("Logout").click()
        try:
            WebDriverWait(self.driver, TIMEOUT_TIME_BASE).until(
                ec.presence_of_element_located((By.XPATH, "//button[contains(.,' Login')]"))
            )
        except TimeoutException:
            pass

    def open_products_tab(self):
        for i in range(0, MENU_RETRIES):
            try:
                # The menu might not be fully loaded, the animations take time etc.
                time.sleep(SLEEP_TIME_BASE + i)
                self.driver.find_element_by_id("button-menu").click()
                time.sleep(SLEEP_TIME_BASE + i)
                self.driver.find_element_by_link_text("Catalog").click()
                time.sleep(SLEEP_TIME_BASE + i)
                self.driver.find_element_by_xpath("//li[@id='catalog']/ul/li[2]/a").click()
                time.sleep(SLEEP_TIME_BASE + i)
                self.driver.find_element_by_id("button-menu").click()
                time.sleep(SLEEP_TIME_BASE)
                self._wait_for_table_load("none")
                return
            except StaleElementReferenceException:
                continue
        print "\nERROR: Products tab opening failed"

    def find_first_product_by_name(self, product_name, status=None):
        # Maximum 2 pages
        for page in range(0, 2):
            # Get the table dimensions
            table_spec = self._get_table_specification()
            table_spec = table_spec.split()
            table_rows = int(table_spec[3]) - int(table_spec[1]) + 1
            table_pages = int(table_spec[6][1:])

            # Iterate the table, try to find the match
            for i in range(1, table_rows + 1):
                product = self.driver.find_element_by_xpath(
                    "//form[@id='form-product']/div/table/tbody/tr[{0}]/td[3]".format(i))
                # Searching only by the name
                if status is None and product.text == product_name:
                    return i
                # Searching for status match also
                elif status is not None:
                    product_status = self.driver.find_element_by_xpath(
                        "//form[@id='form-product']/div/table/tbody/tr[{0}]/td[7]".format(i))
                    if product.text == product_name and product_status.text == status:
                        return i
            # Product not found, back to first page if needed
            if page == 1:
                self._page_switch_to(1)
                return None
            # Get to the new page
            if table_pages > 1:
                self._page_switch_to(2)
            else:
                # No new page and product not found
                return

    def count_products_by_name(self, product_name):
        counter = 0
        # Maximum 2 pages
        for page in range(0, 2):
            # Get the table dimensions
            table_spec = self._get_table_specification()
            table_spec = table_spec.split()
            table_rows = int(table_spec[3]) - int(table_spec[1]) + 1
            table_pages = int(table_spec[6][1:])

            # Iterate the table and count
            for i in range(1, table_rows + 1):
                product = self.driver.find_element_by_xpath(
                    "//form[@id='form-product']/div/table/tbody/tr[{0}]/td[3]".format(i))
                if product.text == product_name:
                    counter += 1
            # Counting finished
            if page == 1:
                self._page_switch_to(1)
                return counter
            # Get to the new page
            if table_pages > 1:
                self._page_switch_to(2)
            else:
                # Only one page
                return counter

    def _page_switch_to(self, page):
        # Check for supported pages
        if page != 1 and page != 2:
            return
        # Update the variant
        button_text = "|<"
        if page == 2:
            button_text = ">|"

        # Click and wait for refresh
        old_spec = self._get_table_specification()
        self.driver.find_element_by_xpath("//a[contains(.,'{0}')]".format(button_text)).click()
        try:
            # Wait for change in active page
            WebDriverWait(self.driver, TIMEOUT_TIME_BASE).until(
                ec.text_to_be_present_in_element((By.CSS_SELECTOR, "#content .active span"), str(page))
            )
            # Wait for change in table specification
            self._wait_for_table_load(old_spec)
        except TimeoutException:
            print "\nERROR: Page select timeout"
            return None

    def _wait_for_table_load(self, old_spec):
        # Tries to check if table specification has changed
        for i in range(0, TABLE_RETRIES):
            # First get the table specification
            new_spec = self._get_table_specification()

            # Specification loaded, compare
            if old_spec == new_spec:
                time.sleep(SLEEP_TIME_BASE + i)
            else:
                return

        # The table specification has not changed, error
        print "\nERROR: Product table timeout"
        self.assertEqual(True, False)

    def _wait_for_success_alert_and_close(self):
        # Wait for the success alert message and close it
        try:
            WebDriverWait(self.driver, TIMEOUT_TIME_BASE).until(
                ec.presence_of_element_located((By.CSS_SELECTOR, "div.alert.alert-success"))
            )
            self.driver.find_element_by_css_selector("button.close").click()
        except TimeoutException:
            print "\nERROR: success alert not found"
            self.assertEqual(True, False)

    def _get_table_specification(self):
        # Wait for the specification to appear
        # Possible staleness errors, recommended to retry the element finding
        for i in range(0, TABLE_RETRIES):
            try:
                WebDriverWait(self.driver, TIMEOUT_TIME_BASE).until(
                    ec.presence_of_element_located((By.XPATH, "//div[@class='col-sm-6 text-right']"))
                )
                # Return the spec
                return self.driver.find_element_by_xpath("//div[@class='col-sm-6 text-right']").text
            except TimeoutException:
                print "\nERROR: Product table timeout"
                self.assertEqual(True, False)
            except StaleElementReferenceException:
                time.sleep(SLEEP_TIME_BASE)
                continue

    def check_product_exists_once(self, product_name):
        if self.count_products_by_name(product_name) > 1:
            # Product is in database multiple times
            print "\nERROR: Multiple products in the database"
            self.assertEqual(True, False)

        row = self.find_first_product_by_name(product_name)
        if row is None:
            # Product is not in database
            print "\nERROR: Product not in database"
            self.assertEqual(True, False)
        else:
            return row

    def check_product_not_exists(self, product_name):
        row = self.find_first_product_by_name(product_name)
        if row is not None:
            # Product is in database
            print "\nERROR: Product is in database"
            self.assertEqual(True, False)

    def remove_product(self, row):
        # Select the product and remove it
        self.driver.find_element_by_xpath("(//input[@name='selected[]'])[{0}]".format(row)).click()
        self.driver.find_element_by_css_selector("button.btn.btn-danger").click()
        # Handle the confirmation alert
        old_spec = self._get_table_specification()
        try:
            # Wait for it
            WebDriverWait(self.driver, TIMEOUT_TIME_BASE).until(ec.alert_is_present())
            # Confirm
            alert = self.driver.switch_to_alert()
            alert.accept()

            # Wait for it to apply the changes - no waiting results in not finished removal
            # Wait for success alert + table refresh
            self._wait_for_success_alert_and_close()
            self._wait_for_table_load(old_spec)
            time.sleep(SLEEP_TIME_BASE)  # Just to be sure
        except TimeoutException:
            print "\nERROR: Removal alert handling failed"
            self.assertEqual(True, False)

    def add_product(self, name, meta, model):
        # Add new product
        old_spec = self._get_table_specification()
        self.driver.find_element_by_css_selector("a.btn.btn-primary").click()
        time.sleep(SLEEP_TIME_BASE)
        # Set name
        self.driver.find_element_by_id("input-name1").clear()
        self.driver.find_element_by_id("input-name1").send_keys(str(name))
        # Set meta tag title
        self.driver.find_element_by_id("input-meta-title1").clear()
        self.driver.find_element_by_id("input-meta-title1").send_keys(str(meta))
        # Set model
        self.driver.find_element_by_link_text("Data").click()
        self.driver.find_element_by_id("input-model").clear()
        self.driver.find_element_by_id("input-model").send_keys(str(model))
        # Save
        self.driver.find_element_by_css_selector("button.btn.btn-primary").click()

        # Wait for update
        self._wait_for_success_alert_and_close()
        self._wait_for_table_load(old_spec)

    def copy_product(self, row):
        # Check the box and click the copy
        old_spec = self._get_table_specification()
        self.driver.find_element_by_xpath("(//input[@name='selected[]'])[{0}]".format(row)).click()
        self.driver.find_element_by_css_selector("button.btn.btn-default").click()

        # Wait for update
        self._wait_for_success_alert_and_close()
        self._wait_for_table_load(old_spec)

    def edit_parameter(self, row, tab, form, value):
        # Edit some text product parameter specified by the table row
        self.driver.find_element_by_xpath(
            "//form[@id='form-product']/div/table/tbody/tr[{0}]/td[8]/a".format(row)).click()
        self.driver.find_element_by_link_text(tab).click()
        self.driver.find_element_by_id(form).clear()
        self.driver.find_element_by_id(form).send_keys(value)
        self.driver.find_element_by_css_selector("button.btn.btn-primary").click()

        # Wait for update
        self._wait_for_success_alert_and_close()
        self._wait_for_table_load("none")

    def filter_text_input(self, form, value):
        # Filter by some textual input form
        spec = self._get_table_specification()
        self.driver.find_element_by_id(form).clear()
        self.driver.find_element_by_id(form).send_keys(value)
        self.driver.find_element_by_id("button-filter").click()

        # Wait for update
        self._wait_for_table_load(spec)

    def filter_dropdown_input(self, form, value):
        # Filter by some dropdown menu
        spec = self._get_table_specification()
        Select(self.driver.find_element_by_id(form)).select_by_visible_text(value)
        self.driver.find_element_by_id("button-filter").click()

        # Wait for update
        self._wait_for_table_load(spec)

    def expect_missing_element(self, how, what):
        # Check if some element is missing as expected
        self.driver.implicitly_wait(SLEEP_TIME_BASE)
        try:
            self.assertFalse(self.is_element_present(how, what))
        finally:
            self.driver.implicitly_wait(IMPLICIT_WAIT)

    def remove_special(self, row, special_num):
        # Remove special offer from the product specified by the row
        self.driver.find_element_by_xpath(
            "//form[@id='form-product']/div/table/tbody/tr[{0}]/td[8]/a".format(row)).click()
        self.driver.find_element_by_link_text("Special").click()
        self.driver.find_element_by_css_selector(
            "#special-row{0} > td.text-left > button.btn.btn-danger".format(str(special_num))).click()
        self.driver.find_element_by_css_selector("button.btn.btn-primary").click()

        # Wait for update
        self._wait_for_success_alert_and_close()
        self._wait_for_table_load("none")

    def add_special(self, row, price):
        # Add special offer to the product specified by the row
        self.driver.find_element_by_xpath(
            "//form[@id='form-product']/div/table/tbody/tr[{0}]/td[8]/a".format(row)).click()
        self.driver.find_element_by_link_text("Special").click()
        self.driver.find_element_by_css_selector(
            "#special > tfoot > tr > td.text-left > button.btn.btn-primary").click()
        self.driver.find_element_by_name("product_special[0][price]").clear()
        self.driver.find_element_by_name("product_special[0][price]").send_keys(str(price))
        self.driver.find_element_by_css_selector("button.btn.btn-primary").click()

        # Wait for update
        self._wait_for_success_alert_and_close()
        self._wait_for_table_load("none")

    def add_discount(self, row, quantity, price, priority=None):
        # Add new discount for product specified by the row
        self.driver.find_element_by_xpath(
            "//form[@id='form-product']/div/table/tbody/tr[{0}]/td[8]/a".format(row)).click()
        self.driver.find_element_by_link_text("Discount").click()
        self.driver.find_element_by_css_selector(
            "#discount > tfoot > tr > td.text-left > button.btn.btn-primary").click()
        # The mouse might click too slow and click the remove instead, add some more time
        time.sleep(2)
        self.driver.find_element_by_name("product_discount[0][quantity]").clear()
        self.driver.find_element_by_name("product_discount[0][quantity]").send_keys(str(quantity))
        self.driver.find_element_by_name("product_discount[0][price]").clear()
        self.driver.find_element_by_name("product_discount[0][price]").send_keys(str(price))
        # Also add the priority if needed
        if priority is not None:
            self.driver.find_element_by_name("product_discount[0][priority]").clear()
            self.driver.find_element_by_name("product_discount[0][priority]").send_keys(str(priority))
        self.driver.find_element_by_css_selector("button.btn.btn-primary").click()

        # Wait for update
        self._wait_for_success_alert_and_close()
        self._wait_for_table_load("none")

    def remove_discount(self, row, discount_num):
        # Remove discount from product specified by the row
        self.driver.find_element_by_xpath(
            "//form[@id='form-product']/div/table/tbody/tr[{0}]/td[8]/a".format(row)).click()
        self.driver.find_element_by_link_text("Discount").click()
        self.driver.find_element_by_css_selector("#discount-row{0} .btn-danger".format(discount_num)).click()
        self.driver.find_element_by_css_selector("button.btn.btn-primary").click()

        # Wait for update
        self._wait_for_success_alert_and_close()
        self._wait_for_table_load("none")

    def locate_product_in_store(self, category_how, category_what, product_how, product_what):
        # Get to the product page in the store following the specified links
        self.driver.get("http://mys01.fit.vutbr.cz:8038/")
        self._store_follow_link(By.LINK_TEXT, "Tablets")
        self._store_follow_link(category_how, category_what)
        self._store_follow_link(product_how, product_what)

        # Get the content of the product details (after they load up) for further use
        for i in range(0, STORE_RETRIES):
            try:
                WebDriverWait(self.driver, TIMEOUT_TIME_BASE).until(
                    ec.presence_of_element_located((By.CSS_SELECTOR, "#content .col-sm-4"))
                )
                return self.driver.find_element_by_css_selector("#content .col-sm-4").text
            except TimeoutException:
                print "\nERROR: store product search timeout"
                self.assertEqual(True, False)
            except StaleElementReferenceException:
                time.sleep(SLEEP_TIME_BASE)
                continue

    def _store_follow_link(self, how, what):
        # Follow the specified store link safely
        for i in range(0, STORE_RETRIES):
            try:
                WebDriverWait(self.driver, TIMEOUT_TIME_BASE).until(
                    ec.presence_of_element_located((how, what))
                )
                self.driver.find_element(how, what).click()
            except TimeoutException:
                print "\nERROR: store product search timeout"
                self.assertEqual(True, False)
            except StaleElementReferenceException:
                time.sleep(SLEEP_TIME_BASE)
                continue

    def _change_out_of_stock_status(self, row, value):
        # Change out of stock status for product specified by the row
        self.driver.find_element_by_xpath(
            "//form[@id='form-product']/div/table/tbody/tr[{0}]/td[8]/a".format(row)).click()
        # Get to the details and click the option list
        self.driver.find_element_by_link_text("Data").click()
        select = WebDriverWait(self.driver, TIMEOUT_TIME_BASE).until(
            ec.presence_of_element_located((By.XPATH, "//select[@id='input-stock-status']")))
        select.click()

        # Get the selected option and compare it
        selected_option = WebDriverWait(self.driver, TIMEOUT_TIME_BASE).until(
            ec.presence_of_element_located(
                (By.XPATH, "//select[@id='input-stock-status']/option[@selected='selected']")))
        self.assertNotEqual(selected_option.text, value)

        # Change the selected value
        Select(self.driver.find_element_by_id("input-stock-status")).select_by_visible_text(value)
        self.driver.find_element_by_css_selector("button.btn.btn-primary").click()

        # Wait for update
        self._wait_for_success_alert_and_close()
        self._wait_for_table_load("none")
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
