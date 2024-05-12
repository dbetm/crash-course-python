class Temperature:
    """Represent a temperature value extracted from the timeanddate.com/weather webpage."""
    base_url = "https://www.timeanddate.com/weather/{country}/{city}"

    def __init__(self, country: str, city: str):
        self.country = self.____preprocess_param_string(country)
        self.city = self.__preprocess_param_string(city)
    
    def __preprocess_param_string(self, string: str) -> str:
        """Remove leading and trailing spaces, replaces intermediate spaces with 
        dashes and lowercase the string."""
        string = string.strip()
        string = string.replace(" ", "-")

        return string.lower()

    def get(self):
        url = self.base_url.format(country=self.country, city=self.city)



from selectorlib import Extractor

extractor = Extractor.from_yaml_file("")
extractor.extract(response.text)