import pytest
import allure

@allure.MASTER_HELPER.feature("фича ебать спартак")
@allure.MASTER_HELPER.testcase("тест кейс цска сосать")
def test_post_download(app):
    with allure.MASTER_HELPER.step("пек пек"):
        app.feed_news.post_download()
