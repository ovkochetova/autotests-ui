from playwright.async_api import expect

from elements.base_element import BaseElement


class Input(BaseElement):
    def get_locator(self, nth: int = 0, **kwargs): # переопределяем локатор, добаляя ему input
        return super().get_locator(**kwargs).locator('input')

    def  fill(self, value: str, nth: int = 0,**kwargs):
        locator = self.get_locator(nth=nth, **kwargs)
        locator.fill(value)

    def check_have_value(self, value: str, nth: int = 0, **kwargs):
        locator = self.get_locator(nth=nth, **kwargs)
        expect(locator).to_have_value(value)