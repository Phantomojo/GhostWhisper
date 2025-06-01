import unittest
from core.message import Message

class TestMessage(unittest.TestCase):
    def test_serialize_deserialize(self):
        original = Message(sender='alice', receiver='bob', content='Hello, Bob!')
        serialized = original.serialize()
        deserialized = Message.deserialize(serialized)

        self.assertEqual(original.sender, deserialized.sender)
        self.assertEqual(original.receiver, deserialized.receiver)
        self.assertEqual(original.content, deserialized.content)
        self.assertEqual(original.timestamp, deserialized.timestamp)

if __name__ == '__main__':
    unittest.main()
