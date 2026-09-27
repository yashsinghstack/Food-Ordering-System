def login():
    correct_username = "fooduser"
    correct_password = "food123"

    while True:
        print("\n========== FOOD ORDERING SYSTEM ==========")
        username = input("Enter username: ")
        password = input("Enter password: ")

        if username == correct_username and password == correct_password:
            print("\n✅ Login successful!")
            return True
        else:
            print("\n❌ Invalid username or password.")
            print("Please try again.")


def customer_details():
    print("\n========== CUSTOMER DETAILS ==========")

    name = input("Enter your name: ").strip()

    while True:
        phone = input("Enter 10-digit phone number: ").strip()

        if phone.isdigit() and len(phone) == 10:
            break
        else:
            print("❌ Phone number must contain exactly 10 digits.")

    while True:
        address = input("Enter delivery address: ").strip()

        if address:
            break
        else:
            print("❌ Address cannot be empty.")

    print("\n✅ Customer details saved!")

    return name, phone, address


def display_menu():
    menu = {
        1: ("Margherita Pizza", 180),
        2: ("Cheese Burger", 140),
        3: ("White Sauce Pasta", 160),
        4: ("Veg Wrap", 100),
        5: ("Peri Peri Fries", 90),
        6: ("Fresh Lime Soda", 60)
    }

    print("\n========== FOOD MENU ==========")

    for number, (food, price) in menu.items():
        print(f"{number}. {food:<20} ₹{price}")

    return menu


def select_food(menu):
    while True:
        try:
            choice = int(input("\nEnter food number: "))

            if choice in menu:
                food, price = menu[choice]

                while True:
                    try:
                        quantity = int(input("Enter quantity: "))

                        if quantity > 0:
                            print(f"\n✅ Added {quantity} × {food}")
                            return food, price, quantity
                        else:
                            print("❌ Quantity must be greater than 0.")

                    except ValueError:
                        print("❌ Please enter a valid quantity.")

            else:
                print("❌ Invalid food choice.")

        except ValueError:
            print("❌ Please enter a valid number.")


def display_cart(cart):
    print("\n========== YOUR CART ==========")

    if not cart:
        print("🛒 Your cart is empty.")
        return

    total = 0

    for number, item in enumerate(cart, start=1):
        food = item["food"]
        price = item["price"]
        quantity = item["quantity"]

        subtotal = price * quantity
        total += subtotal

        print(
            f"{number}. {food:<20} "
            f"₹{price} × {quantity} = ₹{subtotal}"
        )

    print("--------------------------------")
    print(f"Cart Total: ₹{total}")


def shopping_cart(menu):
    cart = []

    while True:
        food, price, quantity = select_food(menu)

        cart.append({
            "food": food,
            "price": price,
            "quantity": quantity
        })

        print(f"\n✅ {quantity} × {food} added to cart!")

        while True:
            more = input(
                "\nDo you want to order another item? (yes/no): "
            ).lower()

            if more == "yes":
                break

            elif more == "no":
                display_cart(cart)
                return cart

            else:
                print("❌ Please enter yes or no.")


def remove_from_cart(cart):
    if not cart:
        print("\n🛒 Your cart is empty.")
        return

    display_cart(cart)

    print("\n========== REMOVE ITEM ==========")
    print("0. Finish")

    while True:
        try:
            choice = int(input("Enter item number to remove: "))

            if choice == 0:
                return

            if 1 <= choice <= len(cart):
                removed_item = cart.pop(choice - 1)

                print(
                    f"\n❌ Removed {removed_item['quantity']} × "
                    f"{removed_item['food']} from cart."
                )

                # Remove only ONE selected cart item, then continue
                # with the billing/payment steps.
                return

            else:
                print("❌ Invalid item number.")

        except ValueError:
            print("❌ Please enter a valid number.")

def calculate_subtotal(cart):
    subtotal = 0

    for item in cart:
        subtotal += item["price"] * item["quantity"]

    return subtotal


def apply_discount(subtotal):
    if subtotal >= 500:
        discount = subtotal * 0.10
    else:
        discount = 0

    final_amount = subtotal - discount

    return discount, final_amount


def calculate_gst(amount):
    gst = amount * 0.05
    return gst


def calculate_delivery(subtotal):
    if subtotal >= 500:
        delivery_charge = 0
    else:
        delivery_charge = 40

    return delivery_charge


def select_payment():
    print("\n========== PAYMENT METHOD ==========")
    print("1. Cash")
    print("2. UPI")
    print("3. Card")

    while True:
        try:
            choice = int(input("Choose payment method: "))

            if choice == 1:
                return "Cash"

            elif choice == 2:
                return "UPI"

            elif choice == 3:
                return "Card"

            else:
                print("❌ Please choose 1, 2, or 3.")

        except ValueError:
            print("❌ Please enter a valid number.")


def generate_order_id():
    import random

    number = random.randint(100000, 999999)
    order_id = f"FD{number}"

    return order_id


def place_order(name, total_amount, payment_method):
    order_id = generate_order_id()

    print("\n========== ORDER CONFIRMATION ==========")
    print(f"Customer Name  : {name}")
    print(f"Order ID       : {order_id}")
    print(f"Total Amount   : ₹{total_amount:.2f}")
    print(f"Payment Method : {payment_method}")
    print("Order Status   : Confirmed")
    print("----------------------------------------")
    print("✅ Your order has been placed successfully!")

    return order_id


def give_rating():
    print("\n========== RATE YOUR ORDER ==========")

    while True:
        try:
            rating = int(input("Give your rating (1-5): "))

            if 1 <= rating <= 5:
                print(f"\n⭐ Thank you! You gave {rating}/5.")
                return rating

            else:
                print("❌ Rating must be between 1 and 5.")

        except ValueError:
            print("❌ Please enter a valid number.")


# ================= MAIN PROGRAM =================

if login():

    name, phone, address = customer_details()

    menu = display_menu()

    cart = shopping_cart(menu)

    display_cart(cart)

    remove_from_cart(cart)

    display_cart(cart)

    subtotal = calculate_subtotal(cart)

    discount, final_amount = apply_discount(subtotal)

    gst = calculate_gst(final_amount)

    delivery_charge = calculate_delivery(subtotal)

    total_amount = final_amount + gst + delivery_charge

    payment_method = select_payment()

    print("\n========== FINAL BILL ==========")
    print(f"Subtotal        : ₹{subtotal:.2f}")
    print(f"Discount        : ₹{discount:.2f}")
    print(f"After Discount  : ₹{final_amount:.2f}")
    print(f"GST (5%)        : ₹{gst:.2f}")
    print(f"Delivery Charge : ₹{delivery_charge:.2f}")
    print("--------------------------------")
    print(f"Total Amount    : ₹{total_amount:.2f}")
    print(f"Payment Method  : {payment_method}")

    order_id = place_order(
        name,
        total_amount,
        payment_method
    )

    rating = give_rating()

    