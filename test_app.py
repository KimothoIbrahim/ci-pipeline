"""test for app.py
"""

import app


class TestTalk:
    def test_talk(self):
        """unit test for talk function
        """
        assert app.talk('Ibrahim') == 'My name is Ibrahim'


    def test_shout(self):
        """Shout your name
        """
        assert app.shout('Ibrahim') == 'I am screaming out my name Ibrahim'
