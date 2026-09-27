# 🍔 FOOD ORDERING SYSTEM

## 📖 1. Introduction

The Food Ordering System is a beginner-friendly Python console application designed to make the food ordering process simple and easy. The customer can log in, enter personal details, view the food menu, select food items, add them to a shopping cart, remove items, calculate the bill, choose a payment method, place an order, and provide a rating.

This project is developed using basic Python programming concepts such as variables, functions, lists, dictionaries, loops, conditional statements, input validation, and arithmetic operations.

## 🎯 2. Objectives

The main objectives of the Food Ordering System are:

* 🍕 To create a simple food ordering application using Python.
* 🛒 To allow customers to select food items and quantities.
* 📦 To provide a shopping cart for managing selected items.
* 💰 To automatically calculate the total bill.
* 🏷️ To apply discounts, GST, and delivery charges.
* 💳 To provide different payment options.
* 🆔 To generate an order ID after placing an order.
* ⭐ To collect customer feedback through a rating system.

## 💻 3. Technologies Used

* 🐍 **Programming Language:** Python 3.x
* 🖥️ **Development Environment:** VS Code / Python IDLE
* 📱 **Application Type:** Console-based application
* 📚 **External Libraries:** No external libraries are required.

## 🍕 4. Food Menu

The system provides the following food items:

1. 🍕 Margherita Pizza – ₹180
2. 🍔 Cheese Burger – ₹140
3. 🍝 White Sauce Pasta – ₹160
4. 🌯 Veg Wrap – ₹100
5. 🍟 Peri Peri Fries – ₹90
6. 🥤 Fresh Lime Soda – ₹60

## ⚙️ 5. Features of the System

### 🔐 5.1 Login System

The customer must enter a valid username and password to access the food ordering system.

### 👤 5.2 Customer Details

The system collects the customer's name, phone number, and delivery address. The phone number must contain exactly 10 digits, and the address cannot be empty.

### 📋 5.3 Food Menu

The menu displays available food items along with their prices.

### 🍽️ 5.4 Food Selection

The customer can select a food item and enter the required quantity. The program checks whether the selected food number and quantity are valid.

### 🛒 5.5 Shopping Cart

Selected food items are stored in a shopping cart. Customers can order multiple items, view their cart, and remove an item before completing the order.

### 🏷️ 5.6 Discount

A 10% discount is applied when the subtotal is ₹500 or more.

### 🧾 5.7 GST

A 5% GST is calculated on the amount after applying the discount.

### 🚚 5.8 Delivery Charge

If the subtotal is ₹500 or more, delivery is free. For orders below ₹500, a delivery charge of ₹40 is added.

### 💳 5.9 Payment Method

The customer can choose:

1. 💵 Cash
2. 📱 UPI
3. 💳 Card

### ✅ 5.10 Order Confirmation

After selecting the payment method, the system generates a unique order ID and displays the order confirmation.

### ⭐ 5.11 Customer Rating

After placing the order, the customer can provide a rating between 1 and 5.

## 💰 6. Billing Process

The billing process is performed in the following order:

**Food Price × Quantity → Subtotal → Discount → Amount After Discount → GST → Delivery Charge → Final Amount**

### 🧮 Example

If the subtotal is ₹500:

* Subtotal = ₹500
* Discount = 10% of ₹500 = ₹50
* Amount After Discount = ₹450
* GST = 5% of ₹450 = ₹22.50
* Delivery Charge = ₹0
* **Final Amount = ₹472.50**

## 🔧 7. Functions Used

* 🔐 `login()` – Checks the username and password.
* 👤 `customer_details()` – Collects customer information.
* 📋 `display_menu()` – Displays the food menu and prices.
* 🍽️ `select_food()` – Allows the customer to select food and quantity.
* 🛒 `shopping_cart()` – Adds selected items to the cart.
* 📦 `display_cart()` – Displays all items in the cart.
* ❌ `remove_from_cart()` – Removes an item from the cart.
* 🧮 `calculate_subtotal()` – Calculates the total price.
* 🏷️ `apply_discount()` – Calculates the applicable discount.
* 🧾 `calculate_gst()` – Calculates 5% GST.
* 🚚 `calculate_delivery()` – Calculates the delivery charge.
* 💳 `select_payment()` – Allows the customer to select a payment method.
* 🆔 `generate_order_id()` – Generates an order ID.
* ✅ `place_order()` – Displays order confirmation.
* ⭐ `give_rating()` – Takes the customer's rating.

## 🐍 8. Python Concepts Used

The following Python concepts are used:

* 📦 Variables
* 🔤 Strings
* 🔢 Integers
* 📋 Lists
* 📚 Dictionaries
* ⚙️ Functions
* 🔄 Loops
* 🔀 Conditional statements
* 🛡️ `try-except`
* ⌨️ User input
* 🔤 String methods
* ✅ `isdigit()`
* ➕ Arithmetic operations
* 🎲 Random number generation

## 🔄 9. Program Flow

**START**
⬇️
🔐 LOGIN
⬇️
👤 CUSTOMER DETAILS
⬇️
📋 DISPLAY FOOD MENU
⬇️
🍽️ SELECT FOOD
⬇️
🔢 ENTER QUANTITY
⬇️
🛒 ADD TO CART
⬇️
❓ ORDER MORE?
⬇️
🛒 VIEW CART
⬇️
❌ REMOVE ITEM
⬇️
🧮 CALCULATE SUBTOTAL
⬇️
🏷️ APPLY DISCOUNT
⬇️
🧾 CALCULATE GST
⬇️
🚚 CALCULATE DELIVERY CHARGE
⬇️
💳 SELECT PAYMENT METHOD
⬇️
🆔 GENERATE ORDER ID
⬇️
✅ ORDER CONFIRMED
⬇️
⭐ GIVE RATING
⬇️
🏁 END

## 🛡️ 10. Input Validation

The system performs basic input validation to prevent incorrect data.

The program checks:

* 🔐 Username and password
* 📱 Phone number for exactly 10 digits
* 🏠 Empty delivery address
* 🍕 Valid food menu number
* 🔢 Quantity greater than zero
* 💳 Valid payment option
* ⭐ Rating between 1 and 5

If an invalid value is entered, the program displays an error message and asks the customer to enter the value again.

## ✅ 11. Advantages

* 👍 Simple and easy to use.
* 🐍 Beginner-friendly Python project.
* 📚 No external libraries are required.
* 🍕 Supports multiple food items.
* 🛒 Provides shopping cart management.
* 💰 Automatically calculates the bill.
* 🏷️ Includes discount, GST, and delivery charges.
* 💳 Provides multiple payment options.
* ⭐ Includes order confirmation and customer rating.

## ⚠️ 12. Limitations

* 💻 The application works only through the console.
* 💾 Customer information is not permanently stored.
* 🗄️ There is no database connection.
* 💳 Payment is only simulated.
* 🍕 The food menu is fixed in the Python program.
* 📍 There is no real-time order tracking.

## 🚀 13. Future Scope

The project can be improved in the future by adding:

* 🗄️ Database connectivity
* 🖥️ Graphical user interface
* 💳 Online payment integration
* 📜 Customer order history
* 🔎 Food categories and search
* 👨‍💼 Admin management
* 📍 Real-time order tracking
* 🖼️ Food images and descriptions
* 📦 Automatic stock management

## 🎓 14. Conclusion

The Food Ordering System is a simple Python-based application that demonstrates the basic working of a real-world food ordering process. It allows customers to log in, provide their details, select food, manage their shopping cart, calculate the bill, choose a payment method, place an order, and give a rating.

The project provides practical experience with important Python concepts such as functions, loops, conditions, lists, dictionaries, input validation, and calculations. It can also be extended with databases, graphical interfaces, online payments, and other advanced features in the future.
