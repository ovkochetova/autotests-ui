from playwright.async_api import expect

from elements.base_element import BaseElement


class Textarea(BaseElement):
    def get_locator(self, **kwargs): # переопределяем локатор, добаляя ему input
        return super().get_locator(**kwargs).locator('textarea').first

    def fill(self, value, **kwargs):
        locator = self.get_locator(**kwargs)
        locator.fill(value)

    def check_have_value(self, value, **kwargs):
        locator = self.get_locator(**kwargs)
        expect(locator).to_have_value(value)
