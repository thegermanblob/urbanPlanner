from typing import List

class Data():
    """Defines the data that will be added to the model
    """
    
    def __init__(self):
        self.population_by_municipality:str = file_to_string("/appsrc/data/annual_estimates_of_the_resident_population_puerto_rico_2020_2023.csv")
        self.income_tax_filings_by_municipality:str = file_to_string("/appsrc/data/number_of_annual_fillings_by_municipality.csv")
        self.sales_tax_data:str = ["https://hacienda.pr.gov/sites/default/files/distribution_of_monthly_sut_collections_rev_unallo._starting_bal_.pdf"]
        pass


def file_to_string(file_path:str) -> str:
    with open(file_path, 'r') as file:
        data = file.read().replace('\\n', '')
        return data