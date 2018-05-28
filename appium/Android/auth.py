from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from Android import AndroidSwipeScroll
from General import rnd_mail


def auth_mail (self):
    wait = WebDriverWait(self.driver, 5)

    try:

        AuthEmail = wait.until(
            EC.element_to_be_clickable((By.ID,
            "com.tribuna.betting:id/btnAuthEmail")))
        AuthEmail.click()

    except:

        AuthEmail = wait.until(
            EC.element_to_be_clickable((By.ID,
            "com.tribuna.betting:id/btnOnBoardingEmail")))
        AuthEmail.click()


    login = wait.until(
        EC.element_to_be_clickable((By.ID,
        "com.tribuna.betting:id/etLogin")))

    login.send_keys("qwe@sports.ru")

    password = wait.until(
        EC.element_to_be_clickable((By.ID,
        "com.tribuna.betting:id/etPassword")))
    password.send_keys("password")

    signIn = wait.until(
        EC.element_to_be_clickable((By.ID,
        "com.tribuna.betting:id/btnSignIn")))
    signIn.click()

    return


def sign_up(self):
    wait = WebDriverWait(self.driver, 5)

    try:

        sign_up = wait.until(
            EC.element_to_be_clickable((By.ID,
            "com.tribuna.betting:id/txtSignUp")))
        sign_up.click()

    except:

        sign_up = wait.until(
            EC.element_to_be_clickable((By.ID,
            "com.tribuna.betting:id/txtContinue")))
        sign_up.click()

    mail = wait.until(
        EC.element_to_be_clickable((By.ID,
        "com.tribuna.betting:id/etEmail")))
    mail.send_keys(rnd_mail.generate_random_emails())

    password = wait.until(
        EC.element_to_be_clickable((By.ID,
        "com.tribuna.betting:id/etPassword")))
    password.send_keys("q12345")

    repeat_password = wait.until(
        EC.element_to_be_clickable((By.ID,
        "com.tribuna.betting:id/etPasswordConfirm")))
    repeat_password.send_keys("q12345")

    #self.driver.hide_keyboard()

    login = wait.until(
        EC.element_to_be_clickable((By.ID,
        "com.tribuna.betting:id/btnSignUp")))
    login.click()

    return


def vk (self):
    wait = WebDriverWait(self.driver, 5)

    try:
        authVK = wait.until(
            EC.element_to_be_clickable((By.ID,
            "com.tribuna.betting:id/btnAuthVk")))
        authVK.click()

    except:
        authVK = wait.until(
            EC.element_to_be_clickable((By.ID,
            "com.tribuna.betting:id/btnOnBoardingVk")))
        authVK.click()

    try:
        wait.until(EC.element_to_be_clickable((By.XPATH, "//android.view.View/android.view.View/android.view.View[6]")))
        login = wait.until(
            EC.element_to_be_clickable((By.XPATH,
            "//android.view.View/android.view.View/android.view.View[6]")))
        login.click()

    except:
        login = wait.until(
            EC.element_to_be_clickable((By.XPATH,
            "//android.widget.ListView[1]/android.view.View[2]/android.widget.EditText")))
        login.send_keys("79645767263")

        password = wait.until(
            EC.element_to_be_clickable((By.XPATH,
            "//android.widget.ListView[2]/android.view.View[2]/android.widget.EditText")))
        password.send_keys("qwersalam")

        login = wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME,
            "android.widget.Button")))
        login.click()

        allow = wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME,
            "android.widget.Button")))
        allow.click()

        wait.until(EC.element_to_be_clickable((By.ID, "com.tribuna.betting:id/imgAvatar")))
        return



def fb(self):
    wait = WebDriverWait(self.driver, 5)

    try:
        authFB = wait.until(
            EC.element_to_be_clickable((By.ID,
            "com.tribuna.betting:id/btnAuthFacebook")))
        authFB.click()

    except:
        authFB = wait.until(
            EC.element_to_be_clickable((By.ID,
            "com.tribuna.betting:id/btnOnBoardingFacebook")))
        authFB.click()

    try:
        pass

    except:

        login = wait.until(
            EC.element_to_be_clickable((By.XPATH,
            "//android.view.View[3]/android.widget.EditText[1]")))
        login.send_keys("79691487427")

        password = wait.until(
            EC.element_to_be_clickable((By.XPATH,
            "//android.view.View[3]/android.widget.EditText[2]")))
        password.send_keys("habib1488f")

        login = wait.until(
            EC.element_to_be_clickable((By.ID,
            "Log In")))
        login.click()

        allow = wait.until(
            EC.element_to_be_clickable((By.ID,
            "Продолжить")))
        allow.click()

    return


def google (self):
    wait = WebDriverWait(self.driver, 5)

    try:
        authG = wait.until(
            EC.element_to_be_clickable((By.ID,
            "com.tribuna.betting:id/btnAuthGoogle")))
        authG.click()

    except:
        authG = wait.until(
            EC.element_to_be_clickable((By.ID,
            "com.tribuna.betting:id/btnOnBoardingGoogle")))
        authG.click()


    # login = wait.until(
    #     EC.element_to_be_clickable((By.ID,
    #     "/Email or phone")))
    # login.send_keys("testforappium@gmail.com")
    #
    # next = wait.until(
    #     EC.element_to_be_clickable((By.ID,
    #     "NEXT")))
    # next.click()
    #
    # password = wait.until(
    #     EC.element_to_be_clickable((By.ID,
    #     "Password")))
    # password.send_keys("qw12345x")
    #
    # next = wait.until(
    #     EC.element_to_be_clickable((By.ID,
    #     "NEXT")))
    # next.click()
    #
    # next = wait.until(
    #     EC.element_to_be_clickable((By.ID,
    #     "ACCEPT")))
    # next.click()
    #
    # login = wait.until(
    #     EC.element_to_be_clickable((By.ID,
    #     "com.google.android.gms:id/suw_navbar_next")))
    # login.click()
    #
    #
    # allow = wait.until(
    #     EC.element_to_be_clickable((By.ID,
    #     "com.google.android.gms:id/accept_button")))
    # allow.click()

    name = wait.until(
        EC.element_to_be_clickable((By.XPATH,
         "//android.widget.LinearLayout[1]/android.widget.LinearLayout")))
    name.click()

    return


def step_logout(self):
    wait = WebDriverWait(self.driver, 5)

    settings = wait.until(
        EC.element_to_be_clickable((By.ID,
        "com.tribuna.betting:id/miSettings")))
    settings.click()

    point = AndroidSwipeScroll.up(self)
    self.driver.swipe(point[0], point[1], point[2], point[3], 1000)

    logout = wait.until(
        EC.element_to_be_clickable((By.ID,
        "com.tribuna.betting:id/cvExit")))
    logout.click()

    back = wait.until(
        EC.element_to_be_clickable((By.XPATH,
        "//android.widget.ImageButton")))
    back.click()

    return

