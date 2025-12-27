from pytest_bdd import when, parsers, then, scenarios
from tests.step_defs.framework.de_common import *
from tests.step_defs import common_locators
from tests.step_defs.atlassites.data.test_atlassites_data import AtlasSiteData
from tests.step_defs.atlassites.locators.test_atlassites_locators import AtlassitesLocators
from tests.step_defs.common_locators import CommonLocators
from tests.step_defs.framework.browser import TWO_SECOND_TIMEOUT, SHORT_DEFAULT_TIMEOUT, DEFAULT_TIMEOUT, \
    LONG_DEFAULT_TIMEOUT
import time
from datetime import datetime

scenarios('../../features')

@when(parsers.parse('Select "{dropdown_menu_option}" option from "{nav_bar_dropdown}" dropdown'))
def select_dropdown_menu_option_from_nav_bar_dropdown(browser, dropdown_menu_option, nav_bar_dropdown, env):
    if nav_bar_dropdown == "Immersive Learning":
        index = 1
    elif nav_bar_dropdown == "Resources":
        index = 3
    else:
        raise Exception("Parameter did not match")
    if browser.is_element_not_displayed(AtlassitesLocators.immersive_learning_nav_bar_dropdown_options_by_guid(AtlasSiteData.immersive_learning_dropdown_options_guids[dropdown_menu_option])):
        browser.wait_for_element_displayed(AtlassitesLocators.immersive_learning_nav_bar_option_dropdown_by_index(index))
        browser.click(AtlassitesLocators.immersive_learning_nav_bar_option_dropdown_by_index(index))
    browser.wait_for_element_displayed(AtlassitesLocators.immersive_learning_nav_bar_dropdown_options_by_guid(AtlasSiteData.immersive_learning_dropdown_options_guids[dropdown_menu_option]))
    browser.click(AtlassitesLocators.immersive_learning_nav_bar_dropdown_options_by_guid(AtlasSiteData.immersive_learning_dropdown_options_guids[dropdown_menu_option]))

@when(parsers.parse('Select the "{button_or_dropdown}" for the "{nav_bar_option}" option on the nav bar'))
def select_button_or_dropdown_for_option_on_nav_bar(browser, button_or_dropdown, nav_bar_option, env):
    browser.is_element_not_displayed_for_period(CommonLocators.pageload_component_spinner, TWO_SECOND_TIMEOUT)
    if nav_bar_option == "Immersive Learning":
        index = 1
    elif nav_bar_option == "Professional Development":
        index = 2
    elif nav_bar_option == "Resources":
        index = 3
    elif nav_bar_option == "News & Events":
        index = 4
    else:
        raise Exception("Parameter did not match")
    if button_or_dropdown == "Button":
        browser.wait_for_element_displayed(AtlassitesLocators.immersive_learning_nav_bar_option_by_index(index))
        browser.click(AtlassitesLocators.immersive_learning_nav_bar_option_by_index(index))
    elif button_or_dropdown == "Dropdown":
        browser.wait_for_element_displayed(AtlassitesLocators.immersive_learning_nav_bar_option_dropdown_by_index(index))
        browser.click(AtlassitesLocators.immersive_learning_nav_bar_option_dropdown_by_index(index))
    else:
        raise Exception("Nav bar option parameter did not match")

@then('Verify Resources page is open')
def verify_resources_page_is_open(browser):
    browser.wait_for_element_displayed(AtlassitesLocators.immersive_learning_hero_image_by_guid(AtlasSiteData.immersive_learning_section_guids['Hero Image, Resources page']))
    browser.wait_for_element_displayed(AtlassitesLocators.immersive_learning_hero_image_timepod_adventure)
    browser.wait_for_element_displayed(AtlassitesLocators.lesson_title_by_guid(AtlasSiteData.immersive_learning_section_guids['Sandbox AR']))

@when('Handle Accept cookies settings')
def handle_Accept_cookies_settings(browser):
    browser.is_element_not_displayed_for_period(CommonLocators.take_survey_pop_up, SHORT_DEFAULT_TIMEOUT)
    if browser.is_element_displayed(AtlassitesLocators.consent_banner_accept_cookies_button):
        browser.not_visible_click(AtlassitesLocators.consent_banner_accept_cookies_button)
        browser.wait_for_element_not_displayed(AtlassitesLocators.consent_banner_accept_cookies_button)

@when(parsers.parse('Select "{asset_section}" section by "{asset_type}" from resources home page'))
def select_section_from_resources_home_page(browser, asset_section, asset_type):
    if asset_type == "Image":
        browser.wait_for_element_to_be_clickable(AtlassitesLocators.immersive_resource_section_image_by_guid(AtlasSiteData.immersive_learning_dropdown_options_guids[asset_section]))
        browser.mouse_hover(AtlassitesLocators.immersive_resource_section_image_by_guid(AtlasSiteData.immersive_learning_dropdown_options_guids[asset_section]))
        browser.wait_for_element_displayed(AtlassitesLocators.immersive_resource_section_image_by_guid(AtlasSiteData.immersive_learning_dropdown_options_guids[asset_section]))
        browser.click(AtlassitesLocators.immersive_resource_section_image_by_guid(AtlasSiteData.immersive_learning_dropdown_options_guids[asset_section]))
    elif asset_type == "Header":
        browser.wait_for_element_to_be_clickable(AtlassitesLocators.immersive_resource_section_title_by_guid(AtlasSiteData.immersive_learning_dropdown_options_guids[asset_section]))
        browser.mouse_hover(AtlassitesLocators.immersive_resource_section_title_by_guid(AtlasSiteData.immersive_learning_dropdown_options_guids[asset_section]))
        browser.wait_for_element_displayed(AtlassitesLocators.immersive_resource_section_title_by_guid(AtlasSiteData.immersive_learning_dropdown_options_guids[asset_section]))
        browser.click(AtlassitesLocators.immersive_resource_section_title_by_guid(AtlasSiteData.immersive_learning_dropdown_options_guids[asset_section]))
    elif asset_type == "Learn More Button":
        browser.wait_for_element_to_be_clickable(AtlassitesLocators.immersive_resource_section_Learn_more_button_by_guid(AtlasSiteData.immersive_learning_dropdown_options_guids[asset_section]))
        browser.mouse_hover(AtlassitesLocators.immersive_resource_section_Learn_more_button_by_guid(AtlasSiteData.immersive_learning_dropdown_options_guids[asset_section]))
        browser.wait_for_element_displayed(AtlassitesLocators.immersive_resource_section_Learn_more_button_by_guid(AtlasSiteData.immersive_learning_dropdown_options_guids[asset_section]))
        browser.not_visible_click(AtlassitesLocators.immersive_resource_section_Learn_more_button_by_guid(AtlasSiteData.immersive_learning_dropdown_options_guids[asset_section]))
    else:
        raise Exception("Parameter not matched")
    pass

@when('Verify TimePod Adventures page and navigate to the TimePod Adventures resource page')
def verify_timepod_adventures_page_and_navigate_to_resource_page(browser):
    browser.is_element_not_displayed_for_period(CommonLocators.pageload_component_spinner, DEFAULT_TIMEOUT)
    browser.wait_for_element_displayed(AtlassitesLocators.timepod_logo)
    browser.wait_for_element_displayed(AtlassitesLocators.classroom_resources_tab)
    browser.click_missed(AtlassitesLocators.classroom_resources_tab)
    browser.wait_for_element_not_displayed(CommonLocators.pageload_component_spinner, DEFAULT_TIMEOUT)
    browser.switch_to_new_window()

@then('Verify TimePod Adventures page is open')
def verify_timepod_adventures_page_is_open(browser):
    browser.is_element_not_displayed_for_period(CommonLocators.pageload_component_spinner, SHORT_DEFAULT_TIMEOUT)
    browser.wait_for_element_displayed(AtlassitesLocators.section_title_by_guid(AtlasSiteData.immersive_learning_section_guids['TimePod Adventures header']))
    browser.verify_text_within_text_on_page(AtlassitesLocators.section_title_by_guid(AtlasSiteData.immersive_learning_section_guids['TimePod Adventures header']), AtlasSiteData.resources_dropdown_options_text[1])
    browser.wait_for_element_displayed(AtlassitesLocators.section_title_by_guid(AtlasSiteData.immersive_learning_section_guids['Prehistoric Earth, TimePod Adventures page']))

@then('Verify Junior Fire Marshal home page should be displayed')
def verify_junior_fire_marshal_public_landing_displayed(browser):
    browser.wait_for_element_not_displayed(AccessValidationLocators.loading_spinner, LONG_DEFAULT_TIMEOUT)
    browser.is_element_not_displayed_for_period(AccessValidationLocators.loading_bar, DEFAULT_TIMEOUT)
    browser.wait_for_element_displayed(AtlassitesLocators.De_log)
    browser.wait_for_element_displayed(AtlassitesLocators.junior_firemarshal)
    browser.wait_for_element_displayed(AtlassitesLocators.hero_image)
    browser.wait_for_element_displayed(AtlassitesLocators.partner_text)
    browser.wait_for_element_displayed(AtlassitesLocators.hartford_logo)
    browser.wait_for_element_displayed(AccessValidationLocators.junior_marshalTraining_text)
    browser.wait_for_element_displayed(AtlassitesLocators.feature_subtitle)
    browser.wait_for_element_displayed(AtlassitesLocators.feature_description)
    browser.wait_for_element_displayed(AtlassitesLocators.feature_image)

@then('Verify quicklinks bar in homepage')
def verify_quicklinks_bar_in_homepage(browser):
    browser.wait_for_element_displayed(AccessValidationLocators.quickLinks)

@when(parsers.parse('Click on the "{link}" link in quicklinks'))
def Click_on_thelinkinquicklinks(browser,link):
    browser.wait_for_element_displayed(AtlassitesLocators.video_link_count)
    browser.mouse_hover(AtlassitesLocators.video_link_count)
    link_Count = browser.find_elements(AtlassitesLocators.video_link_count)
    for i in range(len(link_Count)):
        if browser.text(AtlassitesLocators.video_link_index(i+2))==link:
            browser.not_visible_click(AtlassitesLocators.video_link_index(i+2))
            return True
    raise Exception(link+" link not present")

@then('Verify the Student activities page cards, thumbnail, description')
def verify_student_activities_page_card(browser):
    browser.wait_for_element_displayed(AtlassitesLocators.student_activites_header)
    browser.wait_for_element_displayed(AtlassitesLocators.student_activites_description)
    browser.wait_for_element_displayed(AtlassitesLocators.student_activities_card_header)
    browser.wait_for_element_displayed(AtlassitesLocators.student_activites_link)
    elements_activities_card= browser.find_elements(AtlassitesLocators.student_activities_card)
    elementcount_activities_card = len(elements_activities_card)
    assert elementcount_activities_card is 4
    browser.wait_for_element_displayed(AtlassitesLocators.student_activities_thumbnail)
    browser.wait_for_element_displayed(AtlassitesLocators.student_activities_badge)

@then('Verify the Deputization Resources page title,Subtext and description')
def verify_the_deputization_resources_page(browser):
    browser.wait_for_element_displayed(AtlassitesLocators.deputization_Resources)
    browser.verify_text_on_page(AtlassitesLocators.deputization_Resources, AtlasSiteData.deputization_text)
    browser.wait_for_element_displayed(AtlassitesLocators.deputization_Resources_description)

@then('Verify the activity, certificate and order helmet here buttons and thumbnail')
def verify_activity_certificate_and_order_helmet_here_button(browser):
    browser.wait_for_element_displayed(AtlassitesLocators.deputization_resources_activity_bundle)
    browser.wait_for_element_displayed(AtlassitesLocators.deputization_resources_certificate_button)
    browser.wait_for_element_displayed(AtlassitesLocators.deputization_resources_image)

@then('Verify Hero Flex Wrapper Image')
def verify_hero_flex_image(browser):
    browser.wait_for_element_displayed(AtlassitesLocators.hero_flex_wrapper_image)
    pass

@then('Verify About the program section')
def verify_about_the_program(browser):
    browser.wait_for_element_displayed(AtlassitesLocators.about_the_program_header)
    browser.verify_text_on_page(AtlassitesLocators.about_the_program_header, AtlasSiteData.about_the_program_text)
    browser.wait_for_element_displayed(AtlassitesLocators.about_the_program_description)
    browser.wait_for_element_displayed(AtlassitesLocators.about_the_program_description_text)
    browser.wait_for_element_displayed(AtlassitesLocators.about_the_program_image)
    pass

@then('Verify Partners and Hartford section')
def verify_partners_section(browser):
    browser.wait_for_element_displayed(AtlassitesLocators.partner_header_text)
    browser.verify_text_on_page(AtlassitesLocators.partner_header_text, AtlasSiteData.partner_text[0])
    browser.wait_for_element_displayed(AtlassitesLocators.the_hartford_header_text)
    browser.verify_text_on_page(AtlassitesLocators.the_hartford_header_text, AtlasSiteData.partner_text[1])
    browser.wait_for_element_displayed(AtlassitesLocators.the_hartford_description)
    browser.wait_for_element_displayed(AtlassitesLocators.partners_logo)
    pass

@when('Click Visit The Hartford button and verify landing page')
def click_and_verify_partners_button(browser):
    browser.wait_for_element_displayed(AtlassitesLocators.visit_hartford_button)
    browser.not_visible_click(AtlassitesLocators.visit_hartford_button)
    browser.switch_to_new_window()
    browser.wait_for_element_displayed(AtlassitesLocators.hartford_header_logo)
    browser.wait_for_element_displayed(AtlassitesLocators.hartford_navbar)
    browser.switch_back_to_first_window()
    pass

@then('Verify Discovery Education Section')
def verify_de_section(browser):
    browser.wait_for_element_displayed(AtlassitesLocators.de_section_header_text)
    browser.verify_text_on_page(AtlassitesLocators.de_section_header_text, AtlasSiteData.partner_text[2])
    browser.wait_for_element_displayed(AtlassitesLocators.de_section_description)
    browser.wait_for_element_displayed(AtlassitesLocators.de_section_logo)
    pass

@when('Click Visit Discovery Education button and verify landing page')
def click_and_verify_de_button(browser):
    browser.wait_for_element_displayed(AtlassitesLocators.visit_de_button)
    browser.not_visible_click(AtlassitesLocators.visit_de_button)
    browser.switch_to_new_window()
    browser.wait_for_element_displayed(AtlassitesLocators.de_landing_page_header_logo)
    browser.wait_for_element_displayed(AtlassitesLocators.de_landing_page_navbar)
    browser.switch_back_to_first_window()
    pass

@when('Click Learn More button and verify Sign Up landing page')
def click_and_verify_sign_up_page(browser):
    browser.wait_for_element_displayed(AtlassitesLocators.learn_more_button)
    browser.not_visible_click(AtlassitesLocators.learn_more_button)
    browser.switch_to_new_window()
    browser.wait_for_element_displayed(AtlassitesLocators.sign_up_form_header)
    browser.verify_text_on_page(AtlassitesLocators.sign_up_form_header, AtlasSiteData.sign_up_form_text[4])
    browser.close_current_window_and_switch_back_to_first_window()
    pass

@when(parsers.parse('Click and verify nebula footer "{link}" for Jr. Marshal'))
def click_on_nebula_footer_link_jr_marshal(browser, link):
    current_year = datetime.now().year
    browser.wait_for_element_displayed(AtlassitesLocators.footer_de_logo)
    if link == "Terms of Use Jr Marshal":
        browser.wait_for_element_displayed(AtlassitesLocators.terms_of_use_link)
        browser.not_visible_click(AtlassitesLocators.terms_of_use_link)
        browser.switch_to_new_window()
        browser.wait_for_element_not_displayed(AccessValidationLocators.loading_spinner, DEFAULT_TIMEOUT)
        browser.is_element_not_displayed_for_period(AccessValidationLocators.loading_bar, DEFAULT_TIMEOUT)
        handle_de_consent_banner_in_popup(browser)
        browser.wait_for_element_displayed(AtlassitesLocators.terms_of_use_marshal_header_text)
        browser.verify_text_on_page(AtlassitesLocators.terms_of_use_marshal_header_text,  AtlasSiteData.quick_lists_text[3])
        browser.wait_for_element_displayed(AtlassitesLocators.website_terms_of_use)
        browser.wait_for_element_displayed(AtlassitesLocators.standard_terms_of_service)
        browser.wait_for_element_displayed(AtlassitesLocators.subscription_service_terms)
        browser.close_current_window_and_switch_back_to_first_window()
    elif link == "Privacy Policy Marshal":
        browser.wait_for_element_displayed(AtlassitesLocators.privacy_policy_link)
        browser.not_visible_click(AtlassitesLocators.privacy_policy_link)
        browser.switch_to_new_window()
        browser.wait_for_element_not_displayed(AccessValidationLocators.loading_spinner, DEFAULT_TIMEOUT)
        browser.is_element_not_displayed_for_period(AccessValidationLocators.loading_bar, DEFAULT_TIMEOUT)
        browser.wait_for_element_displayed(AtlassitesLocators.privacy_policy_header_text)
        browser.verify_text_within_text_on_page(AtlassitesLocators.privacy_policy_header_text, AtlasSiteData.quick_lists_text[4])
        browser.wait_for_element_displayed(AtlassitesLocators.de_privacy_policy)
        browser.verify_text_on_page(AtlassitesLocators.de_privacy_policy, AtlasSiteData.footer_links_page_text[0])
        browser.close_current_window_and_switch_back_to_first_window()
    elif link == "About Us":
        browser.wait_for_element_displayed(AtlassitesLocators.about_us_link)
        browser.not_visible_click(AtlassitesLocators.about_us_link)
        browser.switch_to_new_window()
        browser.wait_for_element_not_displayed(AccessValidationLocators.loading_spinner, DEFAULT_TIMEOUT)
        browser.wait_for_element_displayed(AtlassitesLocators.about_us_header_text)
        browser.wait_for_element_displayed(AtlassitesLocators.desktop_de_logo)
        browser.close_current_window_and_switch_back_to_first_window()
    elif link == "Copyright":
        browser.wait_for_element_displayed(AtlassitesLocators.copyright_text)
        browser.verify_text_on_page(AtlassitesLocators.copyright_text, AtlasSiteData.copyright_text_with_current_year(
            current_year))
    else:
        raise Exception("Navigation menu option does not match")
    pass

@when('Click and Verify back to top button')
def click_and_verify_btt_button(browser):
    browser.mouse_hover(AtlassitesLocators.footer_de_logo)
    browser.wait_for_element_displayed(AtlassitesLocators.back_to_top_button)
    browser.not_visible_click(AtlassitesLocators.back_to_top_button)
    pass

@then('Verify Sandbox page is open')
def verify_sandbox_page_is_open(browser):
    browser.wait_for_element_displayed(AtlassitesLocators.section_title_by_guid(AtlasSiteData.immersive_learning_section_guids['Sandbox header']))
    browser.verify_text_within_text_on_page(AtlassitesLocators.section_title_by_guid(AtlasSiteData.immersive_learning_section_guids['Sandbox header']), AtlasSiteData.resources_dropdown_options_text[2])
    browser.wait_for_element_displayed(AtlassitesLocators.nebula_card_title_by_guid(AtlasSiteData.immersive_learning_section_guids['Sandbox Solar System']))

@then('Verify Game-Based Learning page is open')
def verify_game_based_learning_page_is_open(browser):
    browser.wait_for_element_displayed(AtlassitesLocators.section_title_by_guid(AtlasSiteData.immersive_learning_section_guids['Games-Based Learning header']))
    browser.verify_text_within_text_on_page(AtlassitesLocators.section_title_by_guid(AtlasSiteData.immersive_learning_section_guids['Games-Based Learning header']), AtlasSiteData.resources_dropdown_options_text[3])

@then('Verify Interactives page is open')
def verify_interactives_page_is_open(browser):
    browser.wait_for_element_displayed(AtlassitesLocators.section_title_by_guid(AtlasSiteData.immersive_learning_section_guids['Interactives Resources header']))
    browser.verify_text_within_text_on_page(AtlassitesLocators.section_title_by_guid(AtlasSiteData.immersive_learning_section_guids['Interactives Resources header']), AtlasSiteData.interactives_header_text)
    browser.wait_for_element_displayed(AtlassitesLocators.asset_title_by_data_click_asset_id_interactives_page(AtlasSiteData.immersive_learning_section_guids['Antigen Attack']))

@then('Verify Virtual Field Trip page is open')
def verify_virtual_field_trip_page_is_open(browser):
    browser.wait_until_text_is_present_in_element(AtlassitesLocators.current_breadcrumb, AtlasSiteData.resources_dropdown_options_text[5])
    browser.wait_for_element_displayed(AtlassitesLocators.immersion_resource_virtual_content)

@then('Verify News & Events page is open')
def verify_news_and_events_page_is_open(browser):
    browser.wait_for_element_displayed(AtlassitesLocators.immersive_learning_hero_image_by_guid(AtlasSiteData.immersive_learning_section_guids['Hero Image, News & Events']))
    browser.wait_for_element_displayed(AtlassitesLocators.section_title_by_guid(AtlasSiteData.immersive_learning_section_guids['News & Events asset section']))

@then('Verify Professional Development page is open')
def verify_professional_development_page_is_open(browser):
    browser.wait_for_element_displayed(AtlassitesLocators.immersive_learning_hero_image_by_guid(AtlasSiteData.immersive_learning_section_guids['Hero Image, Professional Development page']))
    browser.wait_for_element_displayed(AtlassitesLocators.asset_title_by_data_click_asset_id(AtlasSiteData.immersive_learning_section_guids['Classroom Management asset']))
