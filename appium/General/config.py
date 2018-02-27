import os


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


platform_name = 'Android'
platform_version = '6.0'
device_name = 'Huawei'


def android_desired_caps():
    desired_caps = {
        'platformName': platform_name,
        'platformVersion': platform_version,
        'deviceName': device_name,
        'app': PATH('/Users/chechetkin/PycharmProjects/appium/app/Betting Insider_com.tribuna.betting.apk'),
        'newCommandTimeout': '5000',
        'appWaitActivity': '*'

    }
    return desired_caps

def android_noreset_desired_caps():
    desired_caps = {
        'platformName': platform_name,
        'platformVersion': platform_version,
        'deviceName': device_name,
        'app': PATH('/Users/chechetkin/PycharmProjects/appium/app/Betting Insider_com.tribuna.betting.apk'),
        'newCommandTimeout': '5000',
        'appWaitActivity': '*',
        'noReset': 'true'

    }
    return desired_caps





def ios_desired_caps():
    desired_caps = {
        'platformName': 'iOS',
        'platformVersion': '11.2',
        'deviceName': 'iPhone 7',
        'app': PATH('/Users/chechetkin/PycharmProjects/appium/app/Kixx.app'),
        'autoAcceptAlerts': 'true',
        'newCommandTimeout': '50000',
        'launchTimeout': '50000'
    }
    return desired_caps


def ios_noreset_desired_caps():
    desired_caps = {
        'platformName': 'iOS',
        'platformVersion': '11.2',
        'deviceName': 'iPhone 7',
        'app': PATH('/Users/chechetkin/PycharmProjects/appium/app/Kixx.app'),
        'autoAcceptAlerts': 'true',
        'noReset': 'true'
    }
    return desired_caps
