from unittest import TestCase

from core_aiml.utils import sentences


class TestUtils(TestCase):
    def test_sentences(self):
        # sentences
        sents = sentences("First.  Second, still?  Third and Final!  Well, not really")
        assert(len(sents) == 4)
