import unittest
from crawlerhelpers import get_domain


class TestCrawlerHelpers(unittest.TestCase):
    """Just for Example"""

    def test_get_domain(self):
        self.assertEqual(get_domain("http://domain.com/blog/page.html"), 'domain.com')


if __name__ == '__main__':
    unittest.main()
