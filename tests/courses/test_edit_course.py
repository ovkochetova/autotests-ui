import pytest

from pages.courses.courses_list_page import CoursesListPage
from pages.courses.create_course_page import CreateCoursePage


@pytest.mark.courses
@pytest.mark.regression
class TestEditCourses:
    def test_edit_course(self, create_course_page: CreateCoursePage, courses_list_page: CoursesListPage):
        create_course_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")
        create_course_page.create_course_form.check_visible(title="", estimated_time="", description="", max_score="0",
                                                            min_score="0")
        create_course_page.create_course_toolbar_view.check_visible(is_create_course_disabled=True)
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=False)
        create_course_page.create_course_exercises_toolbar_view.check_visible()
        create_course_page.check_visible_exercises_empty_view()
        create_course_page.image_upload_widget.upload_preview_image(file='./testdata/files/image.png')
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)
        create_course_page.create_course_form.fill(
            title="Playwright",
            estimated_time="2 weeks",
            description="Playwright",
            max_score="100",
            min_score="10"
        )
        create_course_page.create_course_toolbar_view.check_visible(is_create_course_disabled=False)
        create_course_page.create_course_toolbar_view.click_create_course_button()

        courses_list_page.toolbar_view.check_visible()
        courses_list_page.course_view.check_visible(
            index=0,
            title="Playwright",
            max_score="100",
            min_score="10",
            estimated_time="2 weeks")

        courses_list_page.course_menu_view.menu_button.click()
        courses_list_page.course_menu_view.edit_menu_button.click()
        create_course_page.create_course_form.fill(
            title="Playwright2",
            estimated_time="4 weeks",
            description="Playwright2",
            max_score="200",
            min_score="20"
        )

        create_course_page.create_course_toolbar_view.click_create_course_button()
        courses_list_page.toolbar_view.check_visible()
        courses_list_page.course_view.check_visible(
            index=0,
            title="Playwright2",
            max_score="200",
            min_score="20",
            estimated_time="4 weeks")


