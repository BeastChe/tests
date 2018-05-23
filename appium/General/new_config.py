
import os

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


def new_desired_caps():
    # Получаемые значения
    platform_name = 'Android'
    platform_version = '7.0'
    device_name = 'Samsung'
    no_reset = False

    desired_caps = {
        'platformName': platform_name,
        'platformVersion': platform_version,
        'deviceName': device_name
    }

    if no_reset is True:
        desired_caps.update({'noReset': 'true'})

    if platform_name == 'Android':
        desired_caps.update(
            {'appWaitActivity': '*', 'app': PATH('/Users/chechetkin/PycharmProjects/appium/app/app-debug.apk')})

    return desired_caps
