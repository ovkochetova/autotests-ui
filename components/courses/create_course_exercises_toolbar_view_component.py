from playwright.sync_api import expect

from components.base_component import BaseComponent


class CreateCourseExercisesToolbarViewComponent(BaseComponent):
    def __init__(self, page):
        super().__init__(page)

        self.title = page.get_by_test_id('create-course-exercises-box-toolbar-title-text')
        self.button = page.get_by_test_id('create-course-exercises-box-toolbar-create-exercise-button')

    def check_visible(self):
        expect(self.title).to_be_visible()
        expect(self.button).to_be_visible()

    def click_create_exercise_button(self):
        self.button.click()