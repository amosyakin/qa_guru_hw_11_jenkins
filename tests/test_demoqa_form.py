import allure
from allure_commons.types import Severity

from qa_gure_5_hw_selene.model.pages.registration_page import RegistrationPage


@allure.tag("WEB")
@allure.severity(Severity.NORMAL)
@allure.feature("Форма регистрации")
@allure.title("Заполнение и проверка формы регистрации")
@allure.link("https://demoqa.com/automation-practice-form", name="DEMOQA")
def test_submit_form(setup_browser):
    with allure.step("Открыть форму регистрации"):
        registration_page = RegistrationPage()
        registration_page.open()

    with allure.step("Заполнить форму регистрации данными и отправить"):
        registration_page.fill_first_name('Ivan')
        registration_page.fill_last_name('Ivanov')
        registration_page.fill_user_email('ivanivanov@mail.com')
        registration_page.fill_user_gender('Male')
        registration_page.fill_user_number('9876543210')
        registration_page.fill_date_of_birth('2000', 'January', '1')
        registration_page.input_subjects('English')
        registration_page.select_hobbies('Music')
        registration_page.upload_picture('picture.jpg')
        registration_page.fill_address('Red Square, 1')
        registration_page.select_state('Haryana')
        registration_page.select_city('Karnal')
        registration_page.click_submit_button()

    with allure.step("Проверка результрующей таблицы"):
        registration_page.should_finish_form_title('Thanks for submitting the form')
        registration_page.should_registrated_user_with(
            'Ivan Ivanov',
            'ivanivanov@mail.com',
            'Male',
            '9876543210',
            '01 January,2000',
            'English',
            'Music',
            'picture.jpg',
            'Red Square, 1',
            'Haryana Karnal'
        )
        registration_page.should_finish_form_button('Close')
