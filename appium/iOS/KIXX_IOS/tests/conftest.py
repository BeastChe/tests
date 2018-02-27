
import pytest

from iOS.KIXX_IOS.fixsture.application import Application

@pytest.fixture (scope= "session")
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture