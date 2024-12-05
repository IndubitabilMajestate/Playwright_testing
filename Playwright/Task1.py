from random import random
from Utils import Utils
from playwright.sync_api import sync_playwright

def Task1():
    with sync_playwright() as playwright:
        full_name = f"Name{round(100 * random())} Surname{round(100 * random())}"
        email = f"{full_name.replace(' ','_')}@example.com"
        current_address = f"Street{round(10 * random())} no.{round(100 * random())}"
        permanent_address = f"Street{round(10 * random())} no.{round(100 * random())}"
        data = {"Full Name": full_name, "Email": email, "Current Address": current_address,
                "Permanent Address": permanent_address}

        chromium = playwright.chromium  # or "firefox" or "webkit".
        browser = chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://demoqa.com")
        page.locator("xpath=.//h5[contains(text(), 'Elements')]").click()
        page.locator("xpath=.//ul//li//span[contains(text(), 'Text Box')]").click()

        locator = Utils(page, data)
        locator.fillInputLocator()
        locator.clickButton(".//button[@id='submit']")
        if locator.validateResponse():
            print("Test passed!")
        else:
            print("Test failed!")
        print(locator.page.locator('xpath=.//div[@id="output"]').locator('xpath=.//p').count())
        pass

if __name__ == '__main__':
    Task1()

    # parinte = page.locator("xpath=.//form")
    #
    # form_fields = parinte.locator("xpath=(//input | //textarea | //button | //select)")
    # for locator_field in form_fields:
    #     print(locator_field)
    #
    # parinte.locator("xpath=.//div[contains(@id, 'wrapper') and  .//label[contains(text(), 'Full Name')]]//input").fill(
    #     full_name)
    # print(parinte)
    # parinte.locator("xpath=.//div[contains(@id, 'wrapper') and  .//label[contains(text(), 'Email')]]//input").fill(
    #     email)
    # parinte.locator("xpath=.//div[contains(@id, 'wrapper') and  .//label[contains(text(), 'Current Address')]]//textarea").fill(
    #     current_address)
    # parinte.locator("xpath=.//div[contains(@id, 'wrapper') and  .//label[contains(text(), 'Permanent Address')]]//textarea").fill(
    #     permanent_address)
    #
    # parinte.locator("xpath=.//div[contains(@id, )")

#   <unde il caut><pe cine caut>[<ce propietati are>]

# <unde il caut> = .  /  //  ./   .//

# <pe cine caut> = *  sau tagul elm

# (optional)
# [<ce propietati are>]
#    a) atribute -> @nume_atr    ( ex: @class='clasa-cautata' )
#    b) functii  -> functie()       contains(), text(),  name()
#    c) elemente -> XPath        .//div[.h3]
#
#    Sintaxa:
#    - contains( <pe prop caut> , <ce sa contina> )   ex: contains(@class, 'tip-clasa')
#    - name ( name()='nume-cautat')                   ex: ".//*[name()='svg']"
#    - text ( text()='text-cautat')                   ex: ".//*[text()='label']"


