import json
import unittest

import facebook_page_scraper


class Test_json(unittest.TestCase):

    def is_name_empty(self,dictionary):
        for key in dictionary:
            if dictionary[key]['name'] == "":
                return True
        return False

        
    def test_scraper_for_json(self): 
        nyc_sublet_group = facebook_page_scraper.Facebook_scraper("1225966920763001",10,"firefox")
        json_data = nyc_sublet_group.scrap_to_json()
        data_dictionary = json.loads(json_data)
        
        self.assertEqual(len(data_dictionary),10)
        self.assertFalse(self.is_name_empty(data_dictionary),"Getting empty strings on name attribute")
        
             

class Test_csv_output(unittest.TestCase):
    
    def test_csv_group(self):
        nyc_sublet_group = facebook_page_scraper.Facebook_scraper("1225966920763001",10,"firefox", isGroup=True)
        was_saved = nyc_sublet_group.scrap_to_csv("nyc","/Users/godye/github/SubletSage/backend")
        self.assertEqual(was_saved,True)

    def test_csv_page(self):
        meta_page = facebook_page_scraper.Facebook_scraper("Meta",10,"firefox")
        was_saved = meta_page.scrap_to_csv("meta_test","/Users/godye/github/SubletSage/backend")
        self.assertEqual(was_saved,True)



if __name__ == "__main__":
    unittest.main()