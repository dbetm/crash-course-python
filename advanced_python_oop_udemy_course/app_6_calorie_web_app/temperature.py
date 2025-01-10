import requests
from selectorlib import Extractor


class Temperature:
    """Represent a temperature value extracted from the timeanddate.com/weather webpage."""
    base_url = "https://www.timeanddate.com/weather/{country}/{city}"

    def __init__(self, country: str, city: str):
        self.country = self.__preprocess_param_string(country)
        self.city = self.__preprocess_param_string(city)
    
    def __preprocess_param_string(self, string: str) -> str:
        """Remove leading and trailing spaces, replaces intermediate spaces with 
        dashes and lowercase the string."""
        string = string.strip()
        string = string.replace(" ", "-")

        return string.lower()
    
    def __fahrenheit_to_celsius(self, temp_f: float) -> float:
        return (temp_f - 32) * 1.8

    def get(self):
        """Get the current temperature scraping a website using the given city and country.
        The temperature is returned in Celsius degrees."""
        url = self.base_url.format(country=self.country, city=self.city)

        print(f"{url=}")

        response = requests.get(url)

        print(response)
        extractor = Extractor.from_yaml_file("temperature.yaml")

        raw_temperature : str = extractor.extract(response.text)["temperature"]

        print(f"{raw_temperature=}")
        temp_f = float(raw_temperature.replace("\xa0°F", "").strip())

        return self.__fahrenheit_to_celsius(temp_f)