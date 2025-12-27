from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.expected_conditions import visibility_of_element_located, element_to_be_clickable, \
    text_to_be_present_in_element, visibility_of, invisibility_of_element
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

# from tests.step_defs.common_data import CommonData

DEFAULT_TIMEOUT = 30
LONG_DEFAULT_TIMEOUT = 60
TEN_SECOND_TIMEOUT = 10
SHORT_DEFAULT_TIMEOUT = 5
TWO_SECOND_TIMEOUT = 2


class Browser:

    def __init__(self, driver):
        self.wait = WebDriverWait(driver, DEFAULT_TIMEOUT)
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def close(self):
        self.driver.close()

    def quit(self):
        self.driver.quit()

    def refresh(self):
        self.driver.refresh()

    def find_element(self, locator):
        by, expression = locator
        return self.driver.find_element(by, expression)

    def find_elements(self, locator):
        by, expression = locator
        return self.driver.find_elements(by, expression)

    def click(self, locator):
        return self.find_element(locator).click()

    def click_missed(self, locator):
        self.mouse_hover(locator)
        self.not_visible_click(locator)

    def not_visible_click(self, locator):
        ele = self.find_element(locator)
        self.driver.execute_script("arguments[0].click();", ele)

    def get_text(self, locator):
       ele = self.find_element(locator)
       text = self.driver.execute_script("return arguments[0].innerText;", ele)
       return text

    def mouse_hover(self, locator):
        action = ActionChains(self.driver)
        element = self.find_element(locator)
        action.move_to_element(element)
        action.perform()

    def mouse_hover_click(self, locator):
        action = ActionChains(self.driver)
        element = self.find_element(locator)
        action.move_to_element(element).click().perform()

    def switch_back_to_first_window(self):
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[0])

    def switch_to_new_window(self):
        new_window_position = len(self.driver.window_handles) - 1
        self.driver.switch_to.window(self.driver.window_handles[new_window_position])

    def switch_to_iframe(self, iframe, timeout=DEFAULT_TIMEOUT):
        self.wait_for_element_displayed(iframe, timeout)
        self.driver.switch_to.frame(self.find_element(iframe))

    def switch_to_default_content(self):
        self.driver.switch_to.default_content()

    def is_displayed(self):
        self.driver.is_displayed()

    def wait_for_element_displayed(self, locator, timeout=DEFAULT_TIMEOUT):
        if timeout != DEFAULT_TIMEOUT:
            webdriver_wait = WebDriverWait(self.driver, timeout)
        else:
            webdriver_wait = self.wait
        webdriver_wait.until(visibility_of_element_located(locator))

    def wait_for_element_not_displayed(self, locator, timeout=DEFAULT_TIMEOUT):
        if timeout != DEFAULT_TIMEOUT:
            webdriver_wait = WebDriverWait(self.driver, timeout)
        else:
            webdriver_wait = self.wait
        webdriver_wait.until_not(visibility_of_element_located(locator))

    def text_to_be_present_in_element(self, locator, value):
        self.wait.until(text_to_be_present_in_element(locator, value))

    def wait_for_element_to_be_clickable(self, locator):
        self.wait_for_element_displayed(locator)
        self.wait.until(element_to_be_clickable(locator))

    def type(self, locator, value):
        self.wait_for_element_displayed(locator)
        element = self.find_element(locator)
        element.send_keys(value)

    def text(self, locator):
        return self.find_element(locator).text

    def verify_text_on_page(self, locator, text):
        self.wait_for_element_displayed(locator)
        text_found = self.find_element(locator).text
        if text_found == text:
            return True
        else:
            raise Exception(CommonData.text_mismatch_at_location_exception(locator, text, text_found))

    def select_option_from_menu(self, locator, option):
        dropdown = Select(self.find_element(locator))
        dropdown.select_by_value(option)

    def select_option_from_menu_by_text(self, locator, option):
        dropdown = Select(self.find_element(locator))
        dropdown.select_by_visible_text(option)

    def verify_css_property(self, locator, css_attribute, expected_value):
        self.wait_for_element_displayed(locator)
        actual_value = self.find_element(locator).value_of_css_property(css_attribute)
        if expected_value in actual_value:
            return True
        else:
            raise Exception(
                CommonData.css_attribute_mismatch_at_location_exception(locator, css_attribute, expected_value,
                                                                        actual_value))

    def is_element_displayed(self, locator):
        try:
            self.find_element(locator).is_displayed()
        except NoSuchElementException:
            return False
        return True

    def is_element_not_displayed(self, locator):
        try:
            self.find_element(locator).is_displayed()
        except NoSuchElementException:
            return True
        return False

    def get_selected_option_from_menu(self, locator):
        dropdown = Select(self.find_element(locator))
        return dropdown.first_selected_option.text

    def get_all_options_from_menu(self, locator):
        dropdown = Select(self.find_element(locator))
        return dropdown.options

    def verify_text_within_text_on_page(self, locator, text):
        self.wait_for_element_displayed(locator)
        text_found = self.find_element(locator).text
        if text in text_found:
            return True
        else:
            raise Exception(CommonData.text_mismatch_at_location_exception(locator, text, text_found))

    def close_current_window_and_switch_back_to_first_window(self):
        self.close()
        self.switch_back_to_first_window()

    def drag_and_drop(self, locator, xaxis=None, yaxis=None):
        self.wait_for_element_displayed(locator)
        dragdrop = ActionChains(self.driver)
        element = self.find_element(locator)
        if xaxis is None and yaxis is None:
            dragdrop.drag_and_drop_by_offset(element, 1, 30).perform()
        else:
            dragdrop.drag_and_drop_by_offset(element, xaxis, yaxis).perform()

    def get_current_url(self):
        return self.driver.current_url

    def wait_for_element_to_be_enabled(self, element):
        webdriver_wait = self.wait
        webdriver_wait.until(visibility_of(element))
        if element and element.is_enabled():
            return element
        else:
            return False

    def wait_for_web_element_to_be_displayed(self, element, timeout=DEFAULT_TIMEOUT):
        if timeout != DEFAULT_TIMEOUT:
            webdriver_wait = WebDriverWait(self.driver, timeout)
        else:
            webdriver_wait = self.wait
        webdriver_wait.until(visibility_of(element))

    def click_back_button(self):
        return self.driver.back()

    def is_element_not_displayed_for_period(self, element, timeout):
            try:
                self.wait_for_element_displayed(element, timeout=timeout)
            except:
                return True
            return True

    def is_element_selected(self, locator):
            try:
                self.find_element(locator).is_selected()
            except Exception:
                return False
            return True

    def drag_and_drop_by_locators(self,source,target):
        self.wait_for_element_displayed(source)
        self.wait_for_element_displayed(target)
        dragdrop = ActionChains(self.driver)
        sourceelement = self.find_element(source)
        targetelement = self.find_element(target)
        dragdrop.click_and_hold(sourceelement).move_to_element(targetelement).release(targetelement).perform()

    def page_scroll_down(self,xaxis,yaxis):
        command="window.scrollBy({},{});".format(xaxis, yaxis)
        self.driver.execute_script(command)

    def key_press_plus_click(self, key, locator):
        self.wait_for_element_displayed(locator)
        action = ActionChains(self.driver)
        element = self.find_element(locator)
        action.key_down(key).click(element).key_up(key).perform()

    def mouse_click_and_hold(self, locator):
        self.wait_for_element_displayed(locator)
        action = ActionChains(self.driver)
        element = self.find_element(locator)
        action.click_and_hold(element).perform()

    def mouse_release(self, locator):
        self.wait_for_element_displayed(locator)
        action = ActionChains(self.driver)
        element = self.find_element(locator)
        action.release(element).perform()

    def wait_until_text_is_present_in_element(self, locator, expected_text, timeout=DEFAULT_TIMEOUT):
        self.wait_for_element_displayed(locator)
        if timeout != DEFAULT_TIMEOUT:
            webdriver_wait = WebDriverWait(self.driver, timeout)
        else:
            webdriver_wait = self.wait
        webdriver_wait.until(text_to_be_present_in_element(locator, expected_text))

    def wait_until_text_not_present_in_element(self, locator, expected_text, timeout=DEFAULT_TIMEOUT):
        self.wait_for_element_displayed(locator)
        if timeout != DEFAULT_TIMEOUT:
            webdriver_wait = WebDriverWait(self.driver, timeout)
        else:
            webdriver_wait = self.wait
        webdriver_wait.until_not(text_to_be_present_in_element(locator, expected_text))

    def accept_alert_popup(self):
        alert = Alert(self.driver)
        alert.accept()

    def scroll_until_element_is_visible(self, locator, max_scrolls=15, x_axis=0, y_axis=350):
        webdriver_wait = WebDriverWait(self.driver, 2)
        scroll_attempt = 0
        element = None
        while scroll_attempt < max_scrolls:
            try:
                element = webdriver_wait.until(visibility_of_element_located(locator))
                break
            except Exception:
                self.driver.execute_script("window.scrollBy(arguments[0], arguments[1]);", x_axis, y_axis)
                scroll_attempt += 1
        if not element:
            raise Exception("Element not found after scrolling.")
        return True
