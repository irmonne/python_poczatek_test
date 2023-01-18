class TaxCalculator:

    FRUIT_VEGETABLES_TAX_RATE = 0.05
    FOOD_TAX_RATE = 0.08
    OTHERS_TAX_RATE = 0.20

    @staticmethod
    def calculate_tax(category_name, amount, price):
        if category_name == "fruit & vegetables":
            tax_rate = TaxCalculator.FRUIT_VEGETABLES_TAX_RATE
        elif category_name == "food":
            tax_rate = TaxCalculator.FOOD_TAX_RATE
        else:
            tax_rate = TaxCalculator.OTHERS_TAX_RATE

        return tax_rate * amount * price


def run_taxcalculator(product, amount):
    print(TaxCalculator.calculate_tax(product.category_name, amount, product.price))
