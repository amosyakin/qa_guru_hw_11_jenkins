from selene import browser, by, command, have

from qa_gure_5_hw_selene import resources


class RegistrationPage:
    def __init__(self):
        self.first_name = browser.element('#firstName')
        self.last_name = browser.element('#lastName')
        self.user_email = browser.element('#userEmail')
        self.user_number = browser.element('#userNumber')
        self.subjects_input = browser.element('#subjectsInput')
        self.up_picture = browser.element('#uploadPicture')
        self.current_address = browser.element('#currentAddress')
        self.state = browser.element('#state')
        self.city = browser.element('#city')
        self.submit = browser.element('#submit')
        self.close_large_modal = browser.element('#closeLargeModal')

    def open(self):
        browser.open('/automation-practice-form')
        return self

    def fill_first_name(self, value):
        self.first_name.type(value)

    def fill_last_name(self, value):
        self.last_name.type(value)

    def fill_user_email(self, value):
        self.user_email.type(value)

    def fill_user_gender(self, value):
        self.click_element_by_text(value)

    def fill_user_number(self, value):
        self.user_number.type(value)

    def fill_date_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').perform(command.js.scroll_into_view)
        browser.element('#dateOfBirthInput').perform(command.js.click)
        browser.element('.react-datepicker__month-select').click().element(by.text(month)).click()
        browser.element('.react-datepicker__year-select').click().element(by.text(year)).click()
        browser.element('.react-datepicker__week').element(by.text(day)).click()

    def input_subjects(self, value):
        short_value = value[:2]
        self.subjects_input.type(short_value)
        self.click_element_by_text(value)

    def click_element_by_text(self, value):
        browser.element(by.text(value)).perform(command.js.click)

    def select_hobbies(self, value):
        self.click_element_by_text(value)

    def upload_picture(self, value):
        self.up_picture.set_value(resources.path(value))

    def fill_address(self, value):
        self.current_address.type(value)

    def select_state(self, value):
        browser.element('#state').perform(command.js.scroll_into_view)
        self.state.click().element(by.text(value)).click()

    def select_city(self, value):
        self.city.click().element(by.text(value)).click()

    def click_submit_button(self):
        self.submit.click()

    def should_registrated_user_with(
            self, full_name, email, gender, phone_number, date_of_birth,
            subjects, hobbies, picture, address, state_and_city):
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                full_name,
                email,
                gender,
                phone_number,
                date_of_birth,
                subjects, hobbies,
                picture,
                address,
                state_and_city))

    def should_finish_form_title(self, value):
        browser.element('.modal-title').should(have.text(value))

    def should_finish_form_button(self, value):
        self.close_large_modal.should(have.text(value))