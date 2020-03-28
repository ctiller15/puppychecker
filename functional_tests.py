from selenium import webdriver
import unittest

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
        self.assertIn('Puppychecker', self.browser.title)
        
        self.fail('Finish the test!')

        # She sees a prompt to input an image.

        # She submits an image, and it redirects to a page with her result.

        # It tells her her image is a puppy.

if __name__ == '__main__':
    unittest.main(warnings='ignore')
