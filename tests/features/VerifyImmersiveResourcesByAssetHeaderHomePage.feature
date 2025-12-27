Feature: Verify Immersive Resources by asset Header Home Page

#    The following things are performed in this test:
#    - Navigate to the Immersive Resources home page and verify all the asset sections

    Background:
#        @given(parsers.parse('Navigate to the "{application}" public app'))
        Given Navigate to the "Immersive" public app

    Scenario: VerifyImmersiveResourcesByAssetHeaderHomePage
        Then Verify Immersive public landing page should be displayed
#        @when(parsers.parse('Select "{dropdown_menu_option}" option from "{nav_bar_dropdown}" dropdown'))
        When Select "Resources Home" option from "Resources" dropdown
        When Select the "Dropdown" for the "Resources" option on the nav bar
        Then Verify Resources page is open
        When Handle Accept cookies settings
        #@when(parsers.parse('Select "{asset_section}" section by "{asset_type}" from resources home page'))
        When Select "Resources Home" option from "Resources" dropdown
        Then Verify Resources page is open
        When Select "Sandbox" section by "Header" from resources home page
        Then Verify Sandbox page is open
        When Select "Resources Home" option from "Resources" dropdown
        Then Verify Resources page is open
        When Select "Game-Based Learning" section by "Header" from resources home page
        Then Verify Game-Based Learning page is open
        When Select "Resources Home" option from "Resources" dropdown
        Then Verify Resources page is open
        When Select "Interactives" section by "Header" from resources home page
        Then Verify Interactives page is open
        When Select "Resources Home" option from "Resources" dropdown
        Then Verify Resources page is open
        When Select "Virtual Field Trip" section by "Header" from resources home page
        Then Verify Virtual Field Trip page is open
        When Select "Resources Home" option from "Resources" dropdown
        Then Verify Resources page is open
        When Select "Educator Professional Development" section by "Header" from resources home page
        Then Verify Professional Development page is open
        When Select "Resources Home" option from "Resources" dropdown
        Then Verify Resources page is open
        When Select "TimePod Adventures" section by "Header" from resources home page
        When Verify TimePod Adventures page and navigate to the TimePod Adventures resource page
        Then Verify TimePod Adventures page is open