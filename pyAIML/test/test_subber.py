from unittest import TestCase

from core_aiml.word_sub import WordSub


class TestSubber(TestCase):
    def setUp(self):
        self.subber = WordSub()
        self.subber["apple"] = "banana"
        self.subber["orange"] = "pear"
        self.subber["banana"] = "apple"
        self.subber["he"] = "she"
        self.subber["I'd"] = "I would"

    def test_word_case(self):
        # test case insensitivity
        inStr = "I'd like one apple, one Orange and one BANANA."
        outStr = "I Would like one banana, one Pear and one APPLE."
        self.assertEqual(self.subber.sub(inStr), outStr)

        inStr = "He said he'd like to go with me"
        outStr = "She said she'd like to go with me"
        self.assertEqual(self.subber.sub(inStr), outStr)
