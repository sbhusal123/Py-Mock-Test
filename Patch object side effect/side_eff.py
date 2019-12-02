import time

import unittest
from unittest.mock import patch
from unittest import TestCase

class Handler:
    
    def is_connected(self):
        # returns true if connected to backend database
        return False

class Backend:

    def initConnection(self):
        handlr = Handler()
        while(True):
            is_conn =  handlr.is_connected()
            print(is_conn)
            if(is_conn):
                break


class TestBackendConnection(TestCase):


    def test_connection_waiting(self):

        """Test that the backend waits for connection untill the handler connects"""
        with patch(Handler,"is_connected") as isconn:

            isconn.side_effect = [False] * 10 + [True]
            # Simulating is_connected method to return False for first 10 time
            # and True on 11th time 
            bknd = Backend()
            bknd.initConnection()

            self.assertEqual(isconn.call_count,11)

if __name__ == "__main__":
    unittest.main()
