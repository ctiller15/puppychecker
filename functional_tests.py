from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest
import os

class LandingPageTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_submit_a_photo_and_get_a_classification(self):
        # Janet has found this new website. 
        # You put in a picture of a dog and it tells you if it's a puppy or not!
        # She checks out its homepage.
        self.browser.get('http://localhost:8000')

        # She notices the main page tells here where she is.
        self.assertIn('Pupchecker', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('pup', header_text)

        # She sees a prompt to input an image.
        file_input = self.browser.find_element_by_css_selector('input[type="file"]#id_input_photo')
        self.assertEqual(file_input.get_attribute('placeholder'),
                'submit a pup pic'
                )

        curdir = os.getcwd()

        print(curdir)

        # She submits an image, and it redirects to a page with her result.
        file_input.send_keys(curdir + '/pupcheck/test/images/puppy_image.jpg')
        time.sleep(1)

        picture = self.browser.find_element_by_id('id_input_photo')
        self.assertEqual(picture, file_input)

        # It tells her her image is a puppy.
        result = self.browser.find_element_by_id('id_photo_result')
        self.assertIn('puppy', result.browser.text)

        # There is still a second input field inviting the user to keep trying out images to see if it is or is not a puppy.
        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main(warnings='ignore')
