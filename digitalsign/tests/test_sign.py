import unittest
import hashlib
import digitalsign

class TestSign(unittest.TestCase):

    def setUp(self):
        self.testMsg = "Hello world from Mobivity San Diego!"
        self.testSecret = digitalsign.DEFAULT_SECRET
        self.hashDigest = hashlib.sha1(self.testMsg+self.testSecret).hexdigest()

    def tearDown(self):
        pass

    def testCreate(self):
        self.assertEqual(self.hashDigest, digitalsign.createSignature(self.testMsg))

    def testVerify(self):
        self.assertTrue(digitalsign.verifySignature(self.testMsg, self.hashDigest))
        self.assertFalse(digitalsign.verifySignature("Hello world.", self.hashDigest))

if __name__ == '__main__':
    unittest.main()

