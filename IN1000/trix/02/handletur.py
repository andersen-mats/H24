# product: price
AVAILABLE_PRODUCTS = {
    "brod": 20,
    "melk": 15,
    "ost": 40,
    "yoghurt": 12,
    "kaffe": 35,
}


def calculate(wares):
    sum = 0
    count = 0

    for product in AVAILABLE_PRODUCTS:
         sum += wares[product] * AVAILABLE_PRODUCTS[product]

    return sum


def main():
    # product: amount
    wares_customer = {}

    print("Velkommen til IFI-butikken!")

    for product in AVAILABLE_PRODUCTS:
        try:
            ware_amount = int(input(f"Hvor mange {product} vil du ha?\n> ").strip())
            if ware_amount >= 0:
                wares_customer[product] = ware_amount
            else:
                raise ValueError
        except:
            print("Ikke gyldig antall")
            return 1
        
    sum_customer = calculate(wares_customer)
    print(f"Du skal betale: {sum_customer} kr")
    return 0


if __name__ == "__main__":
    main()
