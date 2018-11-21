from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import unittest
import re

driver = webdriver.Firefox()


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
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Enter Assignment Data', header_text)        


        # The Faculty member is invited to enter assignment data straight away
        inputboxAID = self.browser.find_element_by_id('id_new_assignment')  
        self.assertEqual(
            inputboxAID.get_attribute('placeholder'),
            'Enter AssignmentID'
        )    
        inputboxAName = self.browser.find_element_by_id('Name_new_assignment')  
        self.assertEqual(
            inputboxAName.get_attribute('placeholder'),
            'Enter AssignmentName' 
        )    
        inputboxPEO = self.browser.find_element_by_id('PEO_new_assignment')  
        self.assertEqual(
            inputboxPEO.get_attribute('placeholder'),
            'Enter PEO'     
        )
        inputboxSO = self.browser.find_element_by_id('SO_new_assignment')  
        self.assertEqual(
            inputboxSO.get_attribute('placeholder'),
            'Enter SO' 
        )
        inputboxClassID = self.browser.find_element_by_id('ClassID_new_assignment')  
        self.assertEqual(
            inputboxClassID.get_attribute('placeholder'),
            'Enter ClassID' 
        ) 
        inputboxScore = self.browser.find_element_by_id('Score_new_assignment')  
        self.assertEqual(
            inputboxScore.get_attribute('placeholder'),
            'Enter Score' 
        )
        inputboxTerm = self.browser.find_element_by_id('Term_new_assignment')  
        self.assertEqual(
            inputboxTerm.get_attribute('placeholder'),
            'Enter Term' 
        ) 
        inputboxYear = self.browser.find_element_by_id('Year_new_assignment')  
        self.assertEqual(
            inputboxYear.get_attribute('placeholder'),
            'Enter Year' 
        )    
       
        #The faculty member enters the assignment data into test boxes for AssignmentID, AssignmentName, 
        # PEO, SO, ClassID, Score. Term, Year
        inputboxAID.send_keys('999')
        inputboxAName.send_keys('Assignment999')
        inputboxPEO.send_keys('PEO1')
        inputboxSO.send_keys('SO1')
        inputboxClassID.send_keys('CS5513')
        inputboxScore.send_keys('75')
        inputboxTerm.send_keys('1')
        inputboxYear.send_keys('2018')

        # When the Faculty member hits enter, the page updates, and adds the new data to the sampledb DB
        inputboxAID.send_keys(Keys.ENTER)
        time.sleep(1)
        inputboxAName.send_keys(Keys.ENTER)
        time.sleep(1)
        inputboxPEO.send_keys(Keys.ENTER)
        time.sleep(1)
        inputboxSO.send_keys(Keys.ENTER)
        time.sleep(1)
        inputboxClassID.send_keys(Keys.ENTER)
        time.sleep(1)
        inputboxScore.send_keys(Keys.ENTER)
        time.sleep(1)
        inputboxTerm.send_keys(Keys.ENTER)
        time.sleep(1)
        inputboxYear.send_keys(Keys.ENTER)
        time.sleep(1)

    
        driver = webdriver.Firefox()
        python_button = driver.find_elements_by_xpath("//input[@name='scriptbutton' and @value='Visualize Assignment Data']")
        python_button.click()

        table = self.browser.find_element_by_id('id_list_table')
        self.fail('Finish the test!')

if __name__ == '__main__':  
    unittest.main(warnings='ignore')   
     



