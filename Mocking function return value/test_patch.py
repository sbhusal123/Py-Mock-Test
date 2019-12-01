from test_package.module1 import User
from unittest.mock import patch
import unittest
from unittest import TestCase

class TestUser(TestCase):
    def test_user_is_superUser(self):
        with patch("test_package.module1.permission_dict") as pd:
            
            # pd is an alias for the function we want to patch
            pd.return_value = {'super_user':True}

            user = User()
            usr_permission = user.get_permission()
            self.assertEqual(usr_permission,"Super user permission.")
            

if __name__ =="__main__":
    unittest.main()
