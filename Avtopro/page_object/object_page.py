import re
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


from properties.prop_driver import Driver
from base_function import helper



class PageObjectAvtopro(Driver):

    url = 'https://avto.pro/'

    header = ['Производитель', 'Код', 'Описание', 'Цена,ГРН']

    def __init__(self):
        super().__init__()

    def open_site(self):
        return self.driver.get(self.url)

    def get_search_query(self):
        return self.driver.find_element_by_id('ap-search-query')

    def get_choice_num(self, brand_exist):
        brand_exist = brand_exist
        brand_no_sym = helper.delete_all_spec_symbol(brand_exist)

        list_brand = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[2]/span/span")))

        for brand in list_brand:
            brand_avtopro = brand.text
            brand_avtopro_no_sym = helper.delete_all_spec_symbol(brand_avtopro)
            if re.search(brand_no_sym[0], brand_avtopro_no_sym[0], re.I):
                brand.click()
                break

    def get_table(self):
        return self.wait.until(EC.presence_of_all_elements_located((By.XPATH, "//tbody/tr")))

    def record_to_file_csv(self, table):
        lst = []
        keys = ['Производитель', 'Код', 'Описание', 'Цена,ГРН']
        dct_key = dict.fromkeys(keys)

        for tr in table:
            dct_value = [td.text for idx, td in enumerate(tr.find_elements_by_xpath('td'), start=1) if idx in (1, 2, 3, 5)]
            dct = dict(zip(dct_key, dct_value))
            lst.append(dct)
        return lst


