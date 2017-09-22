# -*- coding: latin-1 -*-
from __future__ import unicode_literals

from os import path
import time
from unittest import TestCase

from core_aiml.kernel import Kernel


class TestKernel(TestCase):
    def setUp(self):

        self.k = Kernel()
        self.k.learn(path.join("aiml", "self-test.aiml"))

    def test_sanity(self):
        self.assertEquals(self.k.respond('test bot'), "My name is Nameless")
        self.k.set_predicate('gender', 'male')
        self.assertEquals(self.k.respond('test condition name value'), 'You are handsome')
        self.k.set_predicate('gender', 'female')
        self.assertEquals(self.k.respond('test condition name value'), '')
        self.assertEquals(self.k.respond('test condition name'), 'You are beautiful')
        self.k.set_predicate('gender', 'robot')
        self.assertEquals(self.k.respond('test condition name'), 'You are genderless')
        self.assertEquals(self.k.respond('test condition'), 'You are genderless')
        self.k.set_predicate('gender', 'male')
        self.assertEquals(self.k.respond('test condition'), 'You are handsome')
        self.assertEquals(self.k.respond('test formal'), "Formal Test Passed")
        self.assertEquals(self.k.respond('test gender'), "He'd told her he heard that her hernia is history")
        self.assertEquals(self.k.respond('test get and set'), "I like cheese. My favorite food is cheese")
        self.assertEquals(self.k.respond('test gossip'), "Gossip is not yet implemented")
        self.assertEquals(self.k.respond('test id'), "Your id is _global")
        self.assertEquals(self.k.respond('test input'), 'You just said: test input')
        self.assertEquals(self.k.respond('test javascript'), "Javascript is not yet implemented")
        self.assertIn(self.k.respond('test random'), ["response #1", "response #2", "response #3"])
        self.assertEquals(self.k.respond('test random empty'), "Nothing here!")
        self.assertEquals(self.k.respond('test sentence'), "My first letter should be capitalized.")
        self.assertEquals(self.k.respond("test size"), "I've learned %d categories" % self.k.num_categories())
        self.assertEquals(self.k.respond("test system"), "The system says hello!")
        self.assertEquals(self.k.respond("test that"), "I just said: The system says hello!")
        self.assertEquals(self.k.respond("test that"), "I have already answered this question")

    def test_person(self):
        self.assertEquals(self.k.respond('test person'), 'He is a cool guy.')
        self.assertEquals(self.k.respond('test person2'), 'You are a cool guy.')
        self.assertEquals(self.k.respond('test person2 I Love Lucy'), 'You Love Lucy')

    def test_srai(self):
        self.assertEquals(self.k.respond("test sr test srai"), "srai results: srai test passed")
        self.assertEquals(self.k.respond("test nested sr test srai"), "srai results: srai test passed")
        self.assertEquals(self.k.respond("test srai"), "srai test passed")
        self.assertEquals(self.k.respond("test srai infinite"), "")

    def test_date(self):
        # the date test will occasionally fail if the original and "test"
        # times cross a second boundary.  There's no good way to avoid
        # this problem and still do a meaningful test, so we simply
        # provide a friendly message to be printed if the test fails.
        date_warning = """
        NOTE: the <date> test will occasionally report failure even if it
        succeeds.  So long as the response looks like a date/time string,
        there's nothing to worry about.
        """
        response = self.k.respond('test date')
        print(response)
        self.assertEquals(response, "The date is %s" % time.asctime())

    def test_star(self):
        self.assertEquals(self.k.respond('You should test star begin'), 'Begin star matched: You should')
        self.assertEquals(self.k.respond('test star creamy goodness middle'), 'Middle star matched: creamy goodness')
        self.assertEquals(self.k.respond('test star end the credits roll'), 'End star matched: the credits roll')
        self.assertEquals(self.k.respond('test star having multiple stars in a pattern makes me extremely happy'),
                                         'Multiple stars matched: having, stars in a pattern, extremely happy')
        self.assertEquals(self.k.respond("test thatstar"), "I say beans")
        self.assertEquals(self.k.respond("test thatstar"), "I just said \"beans\"")
        self.assertEquals(self.k.respond("test thatstar multiple"), 'I say beans and franks for everybody')
        self.assertEquals(self.k.respond("test thatstar multiple"), 'Yes, beans and franks for all!')
        self.assertEquals(self.k.respond("test think"), "")

    def test_topic(self):
        self.k.set_predicate("topic", "fruit")
        self.assertEquals(self.k.respond("test topic"), "We were discussing apples and oranges")
        self.k.set_predicate("topic", "Soylent Green")
        self.assertEquals(self.k.respond('test topicstar'), "Solyent Green is made of people!")
        self.k.set_predicate("topic", "Soylent Ham and Cheese")
        self.assertEquals(self.k.respond('test topicstar multiple'), "Both Soylents Ham and Cheese are made of people!")

    def test_unicode(self):
        self.assertEquals(self.k.respond(u"ÔÇÉÏºÃ"), u"Hey, you speak Chinese! ÔÇÉÏºÃ")

    def test_word_case(self):
        self.assertEquals(self.k.respond('test uppercase'), "The Last Word Should Be UPPERCASE")
        self.assertEquals(self.k.respond('test lowercase'), "The Last Word Should Be lowercase")

    def test_version(self):
        self.assertEquals(self.k.respond('test version'), "PyAIML is version %s" % self.k.version())

    def test_whitespace_perserveation(self):
        self.assertEquals(self.k.respond('test whitespace'), "Extra   Spaces\n   Rule!   (but not in here!)    But   Here   They   Do!")
