import unittest
import lib

class TestLib(unittest.TestCase):

    def test_get_rozdzialy_skip_header(self):
        pytania = """# Pytania
        ## Rozdział 1. aaa
aaa
bbb
## Rozdział 2. bbb 
ccc
## Rozdział 3. ccc
xxx"""
        rozdzialy = lib.get_rozdzialy(pytania)

        self.assertEqual(len(rozdzialy), 3)

    def test_get_rozdzialy(self):
        pytania = """
        
## Rozdział 1. aaa
aaa
bbb
## Rozdział 2. bbb 
ccc
## Rozdział 3. ccc
xxx
"""

        rozdzialy = lib.get_rozdzialy(pytania)
        self.assertEqual(len(rozdzialy), 3)

    def test_get_rozdzialy_empty(self):
        pytania = ""
        rozdzialy = lib.get_rozdzialy(pytania)
        self.assertEqual(len(rozdzialy), 0)

    def test_get_rozdzialy_without_leading_space(self):
        pytania = """## Rozdział 1. aaa
aaa
bbb
## Rozdział 2. bbb 
ccc
"""
        rozdzialy = lib.get_rozdzialy(pytania)
        self.assertEqual(len(rozdzialy), 2)

    def test_get_title(self):
        rozdzial = "## Rozdział 1. aaa"
        title = lib.get_title(rozdzial)
        self.assertEqual(title, "aaa")

    def test_get_sections(self):
        rozdzial = """

        ## Rozdział 1. aaa
        """

        sec = """1. aaa
        a) aaa
        b) bbb
        c) ccc
        """

        n = 100

        rozdzial += n*sec

        sections = lib.get_sections(rozdzial)
        self.assertEqual(len(sections), n)

    def test_get_answers(self):
        pytania = """1. Jaka jest najstarsza dostępna wersja systemu operacyjnego Windows Server w chmurze Azure?
   a) Windows Server 2003
   b) Windows Server 2008 R2 SP1
   c) Windows Server 2012 R2"""

        answers = lib.get_answers(pytania)
        self.assertEqual(len(answers), 3)