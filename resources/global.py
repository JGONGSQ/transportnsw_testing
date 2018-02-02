import os
import sys
from random import randint


def get_variables(profile):
    """
    Sets the desired capabilities, confgirations and environment variables to run the tests.
    Based on the profile parameter the variables are selected here.

    Configurations such as which browser, which environment (local/remote/saucelabs) are set here.

    Some configurations are hard coded and static. They need to move to a proper configuration file
    preferably in JSON format.
    """

    # Variable dictionary initialisation
    variables = dict()

    # Base path definition
    variables["ROOT_DIR"] = os.path.abspath(os.path.join(__file__, '..','..')).replace("\\", "/")
    variables["RESOURCES_DIR"] = "/".join((variables["ROOT_DIR"], "resources"))

    variables["DELAY"] = "0"
    variables["SELENIUM_TIMEOUT_MIN"] = "5 seconds"
    variables["SELENIUM_TIMEOUT_MAX"] = "5 seconds"
    variables["SELENIUM_TIMEOUT_IMPLICIT_WAIT"] = "0 second"
    variables["ACTION_TIMEOUT"] = "2 seconds"
    variables["ACTION_RETRY_INTERVAL"] = "1 seconds"

    HTTP_PORT = os.getenv("HTTP_PORT", "7000")
    variables["HTTP_PORT"] = HTTP_PORT


    # Applitools Eye Configuration
    variables['ENABLE_EYES_ON_CLICK'] = False


    # Profile definition
    profile = profile.upper()
    if profile == 'LOCAL':
        variables['REMOTE_URL'] = None
        variables['DESIRED_CAPABILITIES'] = None
        variables['BROWSER'] = "firefox"
        variables['PLATFORM'] = "Windows"
        variables['FIREFOX_PROFILE'] = "/".join((variables["RESOURCES_DIR"], "firefoxprofile_local"))

    if profile == 'GRIDLASTIC':
        variables['REMOTE_URL'] = "http://52.63.102.129:4444/wd/hub"
        variables['DESIRED_CAPABILITIES'] = None
        variables['BROWSER'] = "firefox"
        variables['PLATFORM'] = "Windows"
        
        variables["SELENIUM_TIMEOUT_MIN"] = "5 seconds"
        variables["SELENIUM_TIMEOUT_MAX"] = "5 seconds"
        variables["ACTION_TIMEOUT"] = "5 seconds"

    if profile == 'LOCAL_REMOTE':
        variables['REMOTE_URL'] = "http://localhost:4444/wd/hub"
        variables['DESIRED_CAPABILITIES'] = None
        variables['BROWSER'] = "firefox"
        variables['PLATFORM'] = "Windows"
        variables['FIREFOX_PROFILE'] = "/".join((variables["RESOURCES_DIR"], "firefoxprofile_local"))

    if profile == 'BUILD_BAMBOO_LOCAL_AWS':
        variables['REMOTE_URL'] = "http://%s:4444/wd/hub" % os.environ['SELENIUM_HOST']
        variables['DESIRED_CAPABILITIES'] = None
        variables['BROWSER'] = "chrome"
        variables['PLATFORM'] = "Windows"
        variables['FIREFOX_PROFILE'] = "/".join((variables["RESOURCES_DIR"], "firefoxprofile_local"))

        variables["SELENIUM_TIMEOUT_MIN"] = "10 seconds"
        variables["SELENIUM_TIMEOUT_MAX"] = "10 seconds"
        variables["ACTION_TIMEOUT"] = "10 seconds"


    if profile == 'BUILD_BAMBOO':
        variables['REMOTE_URL'] = "http://192.168.80.9:4444/wd/hub"
        variables['DESIRED_CAPABILITIES'] = None
        variables['BROWSER'] = "firefox"
        variables['PLATFORM'] = "Windows"
        #variables['FIREFOX_PROFILE'] = "/".join((variables["RESOURCES_DIR"], "firefoxprofile_local"))
        variables["SERVER"] = 'http://192.168.80.9:%s' % HTTP_PORT

    if profile == 'BUILD_BAMBOO_SAUCELABS':
        variables['REMOTE_URL'] = "http://%s:%s@%s:%s/wd/hub" % (os.environ['SAUCE_USER_NAME'], os.environ['SAUCE_API_KEY'], os.environ['SELENIUM_HOST'], os.environ['SELENIUM_PORT'])
        variables['BROWSER'] = os.environ['SELENIUM_BROWSER']
        variables['PLATFORM'] = "%s" % os.environ['SELENIUM_PLATFORM']
        desired_capabilities = "ignore-ssl-errors:true,javascriptEnabled:True"
        desired_capabilities += ",platform:%s" % os.environ['SELENIUM_PLATFORM']
        desired_capabilities += ",version:%s" % os.getenv('SELENIUM_VERSION', '')
        desired_capabilities += ",browser:%s" % os.environ['SELENIUM_BROWSER']
        desired_capabilities += ",screen-resolution:1024x768"
        #desired_capabilities += ",device:%s" % os.environ['SELENIUM_BROWSER']
        variables['desired_capabilities'] = desired_capabilities

        variables["SELENIUM_TIMEOUT_MIN"] = "4 seconds"
        variables["SELENIUM_TIMEOUT_MAX"] = "4 seconds"
        variables["ACTION_TIMEOUT"] = "4 seconds"

        variables["SERVER"] = 'http://192.168.80.9:%s' % HTTP_PORT

    if profile == 'BUILD_BAMBOO_BROWSERSTACK':
        variables['REMOTE_URL'] = "http://%s:%s@hub.browserstack.com/wd/hub" % ('julesbarnes', 'xtFXHQqQT9mpZkoxgZsJ')
        variables['BROWSER'] = 'Firefox'
        # variables['BROWSER_VERSION'] = '55.0'
        # variables['OS'] = 'Windows'
        # variables['OS_VERSION'] = '7'

        desired_capabilities = "ignore-ssl-errors:true,javascriptEnabled:True"
        desired_capabilities += ",browser:Firefox"
        desired_capabilities += ",browser_version:55.0"
        desired_capabilities += ",os:Windows"
        desired_capabilities += ",os_version:7"

        # desired_capabilities += ",resolution:1600x1200"
        variables['DESIRED_CAPABILITIES'] = desired_capabilities

        # variables['REMOTE_URL'] = "http://%s:%s@%s:%s/wd/hub" % (os.environ['CLOUD_USER_NAME'], os.environ['CLOUD_API_KEY'], os.environ['SELENIUM_HOST'], os.environ['SELENIUM_PORT'])
        # variables['BROWSER'] = os.environ['SELENIUM_BROWSER']
        # desired_capabilities = "ignore-ssl-errors:true,javascriptEnabled:True"
        # desired_capabilities += ",os:%s" % os.environ['SELENIUM_OS']
        # desired_capabilities += ",browser_version:%s" % os.environ['SELENIUM_BROWSER_VERSION']
        # desired_capabilities += ",browser:%s" % os.environ['SELENIUM_BROWSER']
        # desired_capabilities += ",resolution:1600x1200"
        # variables['desired_capabilities'] = desired_capabilities

        variables["SELENIUM_TIMEOUT_MIN"] = "4 seconds"
        variables["SELENIUM_TIMEOUT_MAX"] = "4 seconds"
        variables["ACTION_TIMEOUT"] = "4 seconds"

        variables["SERVER"] = 'http://192.168.80.9:%s' % HTTP_PORT

    # Global variables
    variables["RANDOM_NO"] = randint(1000000000, 9999999999)


    return variables
