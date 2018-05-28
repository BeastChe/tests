import unittest
import time

from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from Android import AndroidSwipeScroll
from General import config

class tour(unittest.TestCase):
    def setUp(self):
        desired_caps = config.android_desired_caps()
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_tour(self):
        wait = WebDriverWait(self.driver, 10)


        def tour_localization(rus,eng):
            localization = wait.until(
                EC.element_to_be_clickable((By.ID,
                "com.tribuna.betting:id/txtTitle")))
            if localization.text == rus or localization.text == eng:
                localization.click()
            else:
                print('Result', localization.text)
                print("Expected Result", rus, " / ", eng)
                return



        for x in range(0, 4):
            point = AndroidSwipeScroll.left(self)
            self.driver.swipe(point[0], point[1], point[2], point[3], 1000)

        tour5 = wait.until(
            EC.element_to_be_clickable((By.ID,
            "com.tribuna.betting:id/txtContinue")))
        tour5.click()

        tour_localization ("Повторяйте ставки прямо из ленты прогнозов", "Replicate bets right from the tips feed")

        profile = wait.until(
            EC.element_to_be_clickable((By.ID,
            "com.tribuna.betting:id/action_profile")))
        profile.click()

        AuthEmail = wait.until(
            EC.element_to_be_clickable((By.ID,
            "com.tribuna.betting:id/btnAuthEmail")))
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

        tour_localization ("Подпишитесь на интересующие вас команды и турниры", "Subscribe to teams and tournaments you're interested yet")

        settings = wait.until(
            EC.element_to_be_clickable((By.ID,
            "com.tribuna.betting:id/miSettings")))
        settings.click()

        tour_localization ("Если ваш баланс менее 1000 и у вас нет ставок в игре — получите еще денег", "If your balance is below 1000 and you have no current bets — get more money")

        back = wait.until(
            EC.element_to_be_clickable((By.XPATH,
            "//android.widget.ImageButton")))
        back.click()

        raiting = wait.until(
            EC.element_to_be_clickable((By.ID,
                                        "com.tribuna.betting:id/action_rating")))
        raiting.click()

        try:

            wait.until(EC.visibility_of_element_located((By.ID, "com.tribuna.betting:id/ltFirstPlace")))

        except:

            raiting_all_time = wait.until(
                EC.element_to_be_clickable((By.XPATH,
                    "//android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]")))
            raiting_all_time.click()


        tour_localization("Лучшие ставочники за неделю получают денежные призы, попробуйте и вы!", "Best cappers win money every week, try it!")

        mc = wait.until(
            EC.element_to_be_clickable((By.ID,
            "com.tribuna.betting:id/action_mc")))
        mc.click()

        tour_localization ("Внутри матча вы найдете актуальные коэффициенты и прогнозы", "Tap on a match to find current odds and tips")


        i=0
        while  i<10:
            try:

                match_bets = wait.until(
                    EC.element_to_be_clickable((By.ID,
                                                "com.tribuna.betting:id/llBets")))
                match_bets.click()
                i = 10

            except:

                next_day = wait.until(
                    EC.element_to_be_clickable((By.XPATH,
                                                "//android.widget.LinearLayout[5]")))
                next_day.click()
                i = i+1

        bet = wait.until(
            EC.element_to_be_clickable((By.ID,
                "com.tribuna.betting:id/txtBetValue")))
        bet.click()

        tour_localization ("Не забудьте добавить текстовое описание вашей ставки", "Don't forget to add a description to your bet")

        bet = wait.until(
            EC.element_to_be_clickable((By.ID,
            "com.tribuna.betting:id/txtMakeBet")))
        bet.click()

        tour_localization ("Не забудьте добавить текстовое описание вашей ставки", "Don't forget to add a description to your bet")

        point = AndroidSwipeScroll.down(self)
        self.driver.swipe(point[0], point[1], point[2], point[3], 1000)
        time.sleep(1)

        back = wait.until(
            EC.element_to_be_clickable((By.XPATH,
            "//android.widget.ImageButton")))
        back.click()

        predictions = wait.until(
            EC.element_to_be_clickable((By.ID,
            "com.tribuna.betting:id/action_tips")))
        predictions.click()

        tour_localization ("Показывать все прогнозы в ленте или только с описанием?", "Should all predictions be shown in the feed or only those that have a description?")

        user = wait.until(
            EC.element_to_be_clickable((By.ID,
            "com.tribuna.betting:id/imgForecaster")))
        user.click()

        tour_localization ("Получайте пуш-уведомления о новых прогнозах", "Receive push notifications about new tips")

        back = wait.until(
            EC.element_to_be_clickable((By.XPATH,
            "//android.widget.ImageButton")))
        back.click()

        raiting = wait.until(
            EC.element_to_be_clickable((By.ID,
            "com.tribuna.betting:id/action_rating")))
        raiting.click()

        tour_localization ("Еженедельный розыгрыш 100$! Подробнее в правилах.", "Weekly $100 award! See Rules for more info")

        profile = wait.until(
            EC.element_to_be_clickable((By.ID,
            "com.tribuna.betting:id/action_profile")))
        profile.click()

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


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(tour)
    unittest.TextTestRunner(verbosity=2).run(suite)




"com.tribuna.betting:id/llBets"



