
import pytest

from iOS.KIXX_IOS.fixsture.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture