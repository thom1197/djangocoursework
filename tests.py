from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

#Comments show the User Story
class InputDetailsTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_can_enter_name_and_retrieve_it_later(self):
        #Max Brown is on the Digital CV page of the website
        self.browser.get('http://127.0.0.1:8000/cv')

        #He sees the page header
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Digital CV', header_text, 'Header text incorrect. Contents are:' & header_text)

        #He sees text telling him to enter his name
        name_label = self.browser.find_element_by_id('name_label').text
        self.assertIn('Name:', name_label, 'Name label incorrect. Contents are:' & name_label)

        #Max enters his name into a text box
        name_input = self.browser.find_element_by_id('name_input')
        name_input.send_keys('Max Brown')

        #When Max clicks Save, the page refreshes, and the text-box highlights green to show
        #that his name has been saved to the database and retrieved on refresh
        save_button = self.browser.find_element_by_id('save_button')
        save_button.click()

        time.sleep(1) #Ensures the refreshed page is fully loaded before further assertions are made

        self.assertIn('Max Brown', name_input.value, 'Name input box incorrect. Contents are:' & name_input.value)
        self.assertEqual(
            name_input.get_attribute('background-color'),
            '#75e091'
        )

    if __name__ == '__main__':
        unittest.main(warnings='ignore')