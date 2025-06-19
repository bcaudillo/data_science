def print_product_info():
    products = [
        {"image": "product3.jpg", "description": "Stay cozy with our premium fleece hoodie."},
        {"image": "product4.png", "description": "Upgrade your workspace with this sleek LED desk lamp."},
        {"image": "product5.webp", "description": "Freshly roasted coffee beans — now in eco-friendly packaging!"}
    ]

    for product in products:
        print(f"Image: {product['image']}")
        print(f"Description: {product['description']}")
        print()

def print_post_by_platform():
    platforms = ["TikTok", "Pinterest", "LinkedIn"]
    products = [
        {"image": "product3.jpg", "description": "Stay cozy with our premium fleece hoodie."},
        {"image": "product4.png", "description": "Upgrade your workspace with this sleek LED desk lamp."},
        {"image": "product5.webp", "description": "Freshly roasted coffee beans — now in eco-friendly packaging!"}
    ]

    for product, platform in zip(products, platforms):
        print(f"Sharing on {platform}:")
        print(f"Image: {product['image']}")
        print(f"Description: {product['description']}")
        print()

print_product_info()
print_post_by_platform()
