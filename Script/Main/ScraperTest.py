from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup

unwanted_inputs: list[str] = [
    "submit", "button", "checkbox", "color", "date", "datetime-local", "file",
    "hidden", "image", "month", "number", "radio", "range", "reset", "tel", "time", "week"
]


class Scraper:
    def __init__(self, url: str, driver: webdriver):
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


if __name__ == "__main__":
    target_url: str = "https://0a1c004804e990b482319dce00550056.web-security-academy.net/"  # "https://0a1c004804e990b482319dce00550056.web-security-academy.net/"

    # Define the url init params
    firefox_options: Options = Options()
    firefox_options.add_argument("--headless")  # Don't launch a visual instance
    my_scraper = Scraper(target_url, webdriver.Firefox(options=firefox_options))

    input_field_names = my_scraper.scrape_input_fields()
    print(f"Input field names: {input_field_names}")
