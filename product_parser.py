listings = [
    "Apple iPhone 13 (128GB) - $999",
    "Samsung Galaxy S22 Ultra, 256GB - Starting at $1188",
    "Google Pixel 6 Pro - 512GB @ $890"
]


def extract_prices(listings):
    product_list = {}

    for listing in listings:
        # Find the position of the $ sign
        price_index = listing.find("$")

        if price_index != -1:
            # Extract everything after the $ sign
            price_str = listing[price_index + 1:]
            
            # Split the string and take the first word, which should be the price
            price_parts = price_str.split()
            if len(price_parts) > 0:
                price_number = price_parts[0]

                # Check if the price is a valid number (contains only digits or a dot)
                valid = True
                for char in price_number:
                    if not (char.isdigit() or char == '.'):
                        valid = False

                if valid:
                    price = float(price_number)
                    print(f"Listing: {listing}")
                    print(f"Extracted Price: ${price:.2f}")
                    product_list[listing] = {price}
                else:
                    print(f"Invalid price format in listing: {listing}")
            else:
                print(f"No price value found after $ in listing: {listing}")
        else:
            print(f"No price found in listing: {listing}")
    return product_list
