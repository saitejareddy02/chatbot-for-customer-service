import random

products = {
    "product1": {
        "price": 100,
        "rating": 4.5,
        "description": "This is product 1. It's a great product.",
    },
    "product2": {
        "price": 120,
        "rating": 4.2,
        "description": "Product 2 is another good option.",
    },
    "product3": {
        "price": 90,
        "rating": 4.8,
        "description": "Product 3 is the cheapest and highly rated.",
    },
}

def compare_products(product_names):
    comparison_results = {}
    for product_name in product_names:
        product = products.get(product_name)
        if product:
            comparison_results[product_name] = product
        else:
            comparison_results[product_name] = "Product not found."

    return comparison_results

while True:
    user_input = input("You: ")
    user_input = user_input.lower()

    if user_input == "exit":
        print("Chatbot: Goodbye!")
        break

    elif "compare" in user_input:
        product_names = user_input.split("compare")[1].strip().split(" and ")
        comparison_results = compare_products(product_names)
        print("Chatbot: Comparison Results:")
        for product_name, data in comparison_results.items():
            if data == "Product not found.":
                print(f"{product_name}: {data}")
            else:
                print(
                    f"{product_name}: Price - ${data['price']}, Rating - {data['rating']}, Description - {data['description']}"
                )

    else:
        print("Chatbot: I don't understand. You can ask me to compare products.")
