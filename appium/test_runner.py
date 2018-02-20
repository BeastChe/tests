
import unittest

from Android.test import tour, auth_profile, auth_onboarding, auth_popup

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(tour.tour))
suite.addTest(unittest.makeSuite(auth_profile.auth_profile))
suite.addTest(unittest.makeSuite(auth_popup.popup))
suite.addTest(unittest.makeSuite(auth_onboarding.auth_onbording))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)











