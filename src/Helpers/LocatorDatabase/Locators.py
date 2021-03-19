import csv, os
from ..UiElement import UiElement


class Locators:

    def __init__(self, page):
        self.page = page

    @staticmethod
    def __locator_file_for_page(page):
        locator_dir = os.path.dirname(os.path.abspath(__file__))
        locator_file = os.path.join(locator_dir, "PageLocators")
        csv_path = os.path.join(locator_file, page+'.csv')
        return csv_path

    @staticmethod
    def __read_locator_data(page):
        file_path = Locators.__locator_file_for_page(page)
        file = open(file_path, 'r')
        data = list(csv.reader(file))
        # filters empty row values from the csv
        locators = [list(filter(lambda x:x, y)) for y in data]
        # filters empty lines from csv file
        locator_list = list(filter(None, locators))
        file.close()
        return locator_list[1:]

    @staticmethod
    def __create_smart_locator(locator_list):
        locator = "|".join(locator_list) if len(locator_list) > 1 else locator_list[0]
        return locator

    def get_locator_for_page_element(self, element):
        locators = Locators.__read_locator_data(self.page)
        element_index = [i[0] for i in locators if locators].index(element)
        locator = locators[element_index]
        return Locators.__create_smart_locator(locator[1:])

    def get_page_element(self, by, element, text_to_replace="NA"):
        if text_to_replace == "NA":
            return UiElement(by, self.get_locator_for_page_element(element))
        else:
            return UiElement(by, self.get_locator_for_page_element(element).replace("REPLACE_TEXT", text_to_replace))

    @staticmethod
    def get_ui_element(by, element):
        return UiElement(by, element)



