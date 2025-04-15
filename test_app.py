"""test for app.py
"""

import app


class TestTalk:
    def test_talk(self):
        """unit test for talk function
        """
        assert app.talk('Ibrahim') == 'My name is Ibrahim'
