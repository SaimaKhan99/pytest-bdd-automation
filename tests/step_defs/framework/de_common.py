from pytest_bdd import then, parsers, given, scenarios

from tests.step_defs.common_locators import CommonLocators
from tests.step_defs_accessvalidation.accessvalidation.accessvalidation_commonfunctions import \
    juniorfiremarshal_App_Urls, Immersive_App_Urls
from tests.step_defs_accessvalidation.accessvalidation.locators.test_accessvalidation_locators import \
    AccessValidationLocators
from tests.step_defs.framework.browser import SHORT_DEFAULT_TIMEOUT

scenarios('../../features')

@given(parsers.parse('Navigate to the "{application}" public app'))
def visit_page(browser, env,application):
    if application=="juniorfiremarshal":
        browser.open(juniorfiremarshal_App_Urls(env))
    elif application == "Immersive":
        browser.open(Immersive_App_Urls(env))
    else:
        raise Exception('Parameter not matched')

@then('Verify Immersive public landing page should be displayed')
def verify_Immersive_publiclanding_displayed(browser):
    browser.wait_for_element_not_displayed(AccessValidationLocators.loading_spinner)
    browser.is_element_not_displayed_for_period(AccessValidationLocators.loading_bar, SHORT_DEFAULT_TIMEOUT)
    browser.wait_for_element_displayed(AccessValidationLocators.loaded_screen)
    browser.wait_for_element_displayed(AccessValidationLocators.video_card)
    browser.wait_for_element_displayed(AccessValidationLocators.card_title)
    browser.mouse_hover(AccessValidationLocators.our_mission)
    browser.wait_for_element_displayed(AccessValidationLocators.our_mission)

def handle_de_consent_banner_in_popup(browser):
    if browser.is_element_displayed(CommonLocators.de_consent_banner_cookies_button):
        browser.not_visible_click(CommonLocators.de_consent_banner_cookies_button)
        browser.wait_for_element_not_displayed(CommonLocators.de_consent_banner_cookies_button)
    else:
        raise Exception("Handle De Consent Banner pop is not present")
