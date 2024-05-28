from bs4 import BeautifulSoup

unwanted_inputs: list[str] = [
    "submit", "button", "checkbox", "color", "date", "datetime-local", "file",
    "hidden", "image", "month", "number", "radio", "range", "reset", "tel", "time", "week"
]


class Scraper:
    def __init__(self, url, driver):
        self.url = url
        self.driver = driver

    def scrape_input_fields(self):
        try:
            self.driver.get(self.url)
            page_source = self.driver.page_source
            soup = BeautifulSoup(page_source, "html.parser")
            input_fields = soup.find_all("input", type=lambda t: t not in unwanted_inputs)
            return [field.get("name") for field in input_fields]
        except Exception as e:
            print(f"Abort due to Error: {e}")
        finally:
            self.driver.quit()


"""
from selenium import webdriver  # to create an instance of the driver param
from selenium.webdriver.firefox.options import Options  # to define insert the --headless option  
"""