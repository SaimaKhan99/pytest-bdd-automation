Feature:Verify Junior Fire Marshal PublicApp Homepage Student Activities Deputization Partners & DE Section
    # Opening Junior Fire Marshal url in browser
    # Verifying url is navigated to Junior Fire Marshal homepage landing page
    # Verify student Activities sections
    # Verify Deputization sections
    # Verify partners section
    # Verify DE section
    # Verify Sign up section and Page
    # Verify footer quick links

    Background:
        Given Navigate to the "juniorfiremarshal" public app

    Scenario: VerifyJuniorFireMarshalPublicAppHomepageStudentActivitiesDeputizationPartners&DESection

        Then  Verify Junior Fire Marshal home page should be displayed
        Then  Verify quicklinks bar in homepage
        # @when(parsers.parse('Click on the "{link}" link in quicklinks'))
        When  Click on the "Student Activities" link in quicklinks
        Then  Verify the Student activities page cards, thumbnail, description
        When  Click on the "Deputization Resources" link in quicklinks
        Then  Verify the Deputization Resources page title,Subtext and description
        Then  Verify the activity, certificate and order helmet here buttons and thumbnail
        And   Verify Hero Flex Wrapper Image
        When  Click on the "About" link in quicklinks
        Then  Verify About the program section
        Then  Verify Partners and Hartford section
        When  Click Visit The Hartford button and verify landing page
        Then  Verify Discovery Education Section
        When  Click Visit Discovery Education button and verify landing page
        And   Click Learn More button and verify Sign Up landing page
        #@when(parsers.parse('Click and verify nebula footer "{link}" for Jr. Marshal'))
        When  Click and verify nebula footer "Terms of Use Jr Marshal" for Jr. Marshal
        And   Click and verify nebula footer "Privacy Policy Marshal" for Jr. Marshal
        And   Click and verify nebula footer "About Us" for Jr. Marshal
        And   Click and verify nebula footer "Copyright" for Jr. Marshal
        And   Click and Verify back to top button