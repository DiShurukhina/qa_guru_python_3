from selene.support.shared import browser
from selene import be, command
import pytest


browser.config.hold_browser_open = True
browser.open('https://demoqa.com/automation-practice-form')
browser.element('[id="firstName"]').should(be.blank).type('Dinara')
browser.element('[id="lastName"]').should(be.blank).type('Shurukhina')
browser.element('[id="userEmail"]').should(be.blank).type('testEmail@gmail.com')
browser.element('[for="gender-radio-2"]').click()
browser.element('[id="userNumber"]').should(be.blank).type('81234567890')
browser.element('[id="dateOfBirthInput"]').click()
browser.element('[class="react-datepicker__month-select"').send_keys('May')
browser.element('[class="react-datepicker__year-select"').send_keys('1986')
browser.element('[class="react-datepicker__day react-datepicker__day--014"').click()
browser.element('[id="subjectsInput"]').should(be.blank).type('math, history, Informatics')
browser.element('[for="hobbies-checkbox-2"]').click()
browser.element('[for="hobbies-checkbox-3"]').click()
browser.element('[id="uploadPicture"]').send_keys('C:/AQA/qa_guru_python_1/photo_2016-08-25_20-45-23.jpg')
browser.element('[id="currentAddress"]').type('Moscow, Tverskaya str, 19, 173')
browser.element('[id="state"]').perform(command.js.scroll_into_view)
browser.element('[id="react-select-3-input"]').send_keys('Haryana').press_enter()
browser.element('[id="react-select-4-input"]').send_keys('Karnal').press_enter()
browser.element('[id="submit"]').press_enter()


def test_registration():
    pass


def test_reg_positive():
    assert 10==10


def test_reg_negative():
    assert "test" != "TEST"
    assert 5 == 5







