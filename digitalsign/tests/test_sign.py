import unittest
import digitalsign
import sha1

# Test against SHA-1 implementation with pure Python https://github.com/ajalt/python-sha1

class TestSign(unittest.TestCase):

    def setUp(self):
        self.testMsg = "Hello world from Mobivity San Diego!"
        self.testSecret = digitalsign.DEFAULT_SECRET
        self.hashDigest = sha1.sha1(self.testMsg.encode()+self.testSecret.encode())

    def tearDown(self):
        pass

    def testCreate(self):
        self.assertEqual(self.hashDigest, digitalsign.createSignature(self.testMsg))

    def testVerify(self):
        self.assertTrue(digitalsign.verifySignature(self.testMsg, self.hashDigest))
        self.assertFalse(digitalsign.verifySignature("Hello world.", self.hashDigest))

if __name__ == '__main__':
    unittest.main()

