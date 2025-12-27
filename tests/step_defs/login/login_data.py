def login_url(env):
    return {
        'dev-us': 'https://app.dev.discoveryeducation.com/learn/signin',
        'qa-us': 'https://app.qa.discoveryeducation.com/learn/signin',
        'stage-us': 'https://app.stage.discoveryeducation.com/learn/signin',
        'prod-us': 'https://app.discoveryeducation.com/learn/signin',
        'dev-ca': 'https://app.dev.discoveryeducation.ca/learn/signin',
        'qa-ca': 'https://app.qa.discoveryeducation.ca/learn/signin',
        'stage-ca': 'https://app.stage.discoveryeducation.ca/learn/signin',
        'prod-ca': 'https://app.discoveryeducation.ca/learn/signin',
        'dev-uk': 'https://app.dev.discoveryeducation.co.uk/learn/signin',
        'qa-uk': 'https://app.qa.discoveryeducation.co.uk/learn/signin',
        'stage-uk': 'https://app.stage.discoveryeducation.co.uk/learn/signin',
        'prod-uk': 'https://app.discoveryeducation.co.uk/learn/signin',
    }[env]


def login_editorial_url(env):

    if env == 'qa-us':
        return 'https://editorial.{}.discoveryeducation.com'.format("qa")
    elif env == 'stage-us':
        return 'https://editorial.{}.discoveryeducation.com'.format("stage")
    elif env == 'dev-us':
        return 'https://editorial.{}.discoveryeducation.com'.format("dev")
    elif env == 'prod':
        return 'https://editorial.discoveryeducation.com'


class LoginData:
    default_password = 'disc0verme'
    grades = {'grade_band_k_to_2': 'grade_bands[K-2]',
              'grade_band_3_to_5': 'grade_bands[3-5]',
              'grade_band_6_to_8': 'grade_bands[6-8]',
              'grade_band_9_to_12': 'grade_bands[9-12]',
              }
    subjects_id = {'mathematics_id': '2f4b8ab8-09a8-46d9-9625-b6489f22face',
                   'science_id': '9434db0f-6e25-4f88-a7ef-48e895a41f66',
                   'social_studies_id': 'eef9bd96-3a5c-45fa-b64c-b4d93b91e4ec',
                   }
    doodle_admin_password = 'Discovery!2024'
    pass

def login_url_doodle_uk(env):
    return {
        'dev-us': 'https://app.dev.discoveryeducation.co.uk/learn/signin',
        'qa-us': 'https://app.qa.discoveryeducation.co.uk/learn/signin',
        'stage-us': 'https://app.stage.discoveryeducation.co.uk/learn/signin',
        'prod-us': 'https://app.discoveryeducation.co.uk/learn/signin',
    }[env]

