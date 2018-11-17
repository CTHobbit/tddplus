from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_add_assignmentdata_and_view_it_later(self):
        # Faculty Member goes to the page to enter assignment data
        self.browser.get('http://localhost:8000')

        # He/She  notices the page title and header mention entering assignment data. 
        self.assertIn('Enter Assignment Data', self.browser.title)
        self.fail('Finish the test!')


        # The Faculty member is invited to enter assignment data straight away

if __name__ == '__main__':  
    unittest.main(warnings='ignore')        



