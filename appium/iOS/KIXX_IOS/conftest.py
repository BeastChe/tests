
import pytest

from iOS.KIXX_IOS.fixture.application import Application


fixture = None

@pytest.fixture
def app(request):
    global fixture
    if fixture is None:
        fixture = Application()
        fixture.session.first_run()
    else:
        if not fixture.is_valid():
            fixture = Application()
            fixture.session.first_run()
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.logout_from_lobby()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture
