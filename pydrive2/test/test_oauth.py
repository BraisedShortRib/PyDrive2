import unittest
import os
import time

from pydrive2.auth import GoogleAuth
from pydrive2.test.test_util import setup_credentials


class GoogleAuthTest(unittest.TestCase):
    """Tests basic OAuth2 operations of auth.GoogleAuth."""

    def test_01_LocalWebserverAuthWithClientConfigFromFile(self):
        # Delete old credentials file
        self.DeleteOldCredentialsFile("credentials/1.dat")
        # Test if authentication works with config read from file
        ga = GoogleAuth("pydrive2/test/settings/test1.yaml")
        ga.LocalWebserverAuth()
        self.assertEqual(ga.access_token_expired, False)
        # Test if correct credentials file is created
        self.CheckCredentialsFile("credentials/1.dat")
        time.sleep(1)

    def test_02_LocalWebserverAuthWithClientConfigFromSettings(self):
        # Delete old credentials file
        self.DeleteOldCredentialsFile("credentials/2.dat")
        # Test if authentication works with config read from settings
        ga = GoogleAuth("pydrive2/test/settings/test2.yaml")
        ga.LocalWebserverAuth()
        self.assertEqual(ga.access_token_expired, False)
        # Test if correct credentials file is created
        self.CheckCredentialsFile("credentials/2.dat")
        time.sleep(1)

    def test_03_LocalWebServerAuthWithNoCredentialsSaving(self):
        # Delete old credentials file
        self.DeleteOldCredentialsFile("credentials/4.dat")
        # Provide wrong credentials file
        ga = GoogleAuth("pydrive2/test/settings/test3.yaml")
        ga.LocalWebserverAuth()
        self.assertEqual(ga.access_token_expired, False)
        # Test if correct credentials file is created
        self.CheckCredentialsFile("credentials/4.dat", no_file=True)
        time.sleep(1)

    def test_04_CommandLineAuthWithClientConfigFromFile(self):
        # Delete old credentials file
        self.DeleteOldCredentialsFile("credentials/1.dat")
        # Test if authentication works with config read from file
        ga = GoogleAuth("pydrive2/test/settings/test4.yaml")
        ga.CommandLineAuth()
        self.assertEqual(ga.access_token_expired, False)
        # Test if correct credentials file is created
        self.CheckCredentialsFile("credentials/1.dat")
        time.sleep(1)

    def test_05_ConfigFromSettingsWithoutOauthScope(self):
        # Test if authentication works without oauth_scope
        ga = GoogleAuth("pydrive2/test/settings/test5.yaml")
        ga.LocalWebserverAuth()
        self.assertEqual(ga.access_token_expired, False)
        time.sleep(1)

    def test_06_ServiceAuthFromSavedCredentialsFile(self):
        setup_credentials("credentials/6.dat")
        ga = GoogleAuth("pydrive2/test/settings/test6.yaml")
        ga.ServiceAuth()
        self.assertEqual(ga.access_token_expired, False)
        time.sleep(1)

    def DeleteOldCredentialsFile(self, credentials):
        try:
            os.remove(credentials)
        except OSError:
            pass

    def CheckCredentialsFile(self, credentials, no_file=False):
        ga = GoogleAuth("pydrive2/test/settings/default.yaml")
        ga.LoadCredentialsFile(credentials)
        self.assertEqual(ga.access_token_expired, no_file)


if __name__ == "__main__":
    unittest.main()
