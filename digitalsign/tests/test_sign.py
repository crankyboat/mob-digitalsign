import unittest
import digitalsign
import sha1
import uuid

# Test against SHA-1 implementation with pure Python https://github.com/ajalt/python-sha1
class TestSign(unittest.TestCase):

    def setUp(self):
        self.testMsg = "Hello world from Mobivity San Diego!"

    def tearDown(self):
        pass

    def testCreate(self):
        hashedMsg = digitalsign.createSignature(self.testMsg)
        _,salt = hashedMsg.split(':')
        testHashedMsg = sha1.sha1(self.testMsg.encode()+salt.encode()) + ':' + salt
        self.assertEqual(hashedMsg, testHashedMsg)

    def testVerify(self):
        salt = uuid.uuid4().hex
        testHashedMsg = sha1.sha1(self.testMsg.encode()+salt.encode()) + ':' + salt
        self.assertTrue(digitalsign.verifySignature(self.testMsg, testHashedMsg))
        self.assertFalse(digitalsign.verifySignature("Hello world.", testHashedMsg))

if __name__ == '__main__':
    unittest.main()

