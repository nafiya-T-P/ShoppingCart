
products = [
    {"ID": 1, "Name": "Milk", "Price": 30, "Available Stock": 30},
    {"ID": 2, "Name": "Bread", "Price": 50, "Available Stock": 20},
    {"ID": 3, "Name": "Chocolate", "Price": 20, "Available Stock": 50},
    {"ID": 4, "Name": "Drink", "Price": 10, "Available Stock": 100},
    {"ID": 5, "Name": "Tea Powder", "Price": 35, "Available Stock": 38}
]

cart = []
order_history = []
order_id = 1001

coupons = {
    "SAVE10": 10,
    "SAVE20": 20,
    "WELCOME": 5
}

applied_coupon = None


while True:

    print("\n========== SUPERMARKET SHOPPING CART ==========")
    print("1. Display Products")
    print("2. Add Products to Cart")
    print("3. Remove Products from Cart")
    print("4. Update Product Quantity")
    print("5. View Shopping Cart")
    print("6. Calculate Total Amount")
    print("7. Apply Coupon Code")
    print("8. Search Products")
    print("9. Checkout")
    print("10. Order History")
    print("11. Exit")

    menu_choice = int(input("\nEnter Your Choice: "))


    # 1. DISPLAY PRODUCTS

    if menu_choice == 1:

        print("\nSUPERMARKET LIST")
        print(f"{'ID':<15}{'Name':<15}{'Price':<15}{'Available Stock':<15}")

        for product in products:
            print(f"{product['ID']:<15}{product['Name']:<15}{product['Price']:<15}{product['Available Stock']:<15}")


    # 2. ADD PRODUCTS TO CART

    elif menu_choice == 2:

        print("\nSUPERMARKET LIST")
        print(f"{'ID':<15}{'Name':<15}{'Price':<15}{'Available Stock':<15}")

        for product in products:
            print(f"{product['ID']:<15}{product['Name']:<15}{product['Price']:<15}{product['Available Stock']:<15}")

        while True:

            product_id = int(input("\nEnter Product ID (0 to exit): "))

            if product_id == 0:
                break

            found_product = False

            for product in products:

                if product["ID"] == product_id:
                    found_product = True

                    quantity = int(input("Enter Quantity: "))

                    if quantity <= 0:
                        print("Invalid Quantity")

                    elif quantity > product["Available Stock"]:
                        print("Insufficient Stock")

                    else:
                        found = False

                        for item in cart:
                            if item["ID"] == product_id:
                                item["Quantity"] += quantity
                                found = True
                                break

                        if not found:
                            cart.append({
                                "ID": product["ID"],
                                "Name": product["Name"],
                                "Price": product["Price"],
                                "Quantity": quantity
                            })

                        product["Available Stock"] -= quantity

                        print(product["Name"], "Added Successfully")

                    break

            if not found_product:
                print("Invalid Product ID")


    # 3. REMOVE PRODUCTS FROM CART

    elif menu_choice == 3:

        if len(cart) == 0:
            print("Your Cart is Empty")

        else:

            while True:

                remove_id = int(input("\nEnter Product ID to Remove (0 to exit): "))

                if remove_id == 0:
                    break

                found = False

                for item in cart:

                    if item["ID"] == remove_id:
                        found = True

                        remove_quantity = int(input("Enter Quantity to Remove: "))

                        if remove_quantity <= 0:
                            print("Invalid Quantity")

                        elif remove_quantity > item["Quantity"]:
                            print("Quantity Exceeds Cart Quantity")

                        else:
                            item["Quantity"] -= remove_quantity

                            for product in products:
                                if product["ID"] == remove_id:
                                    product["Available Stock"] += remove_quantity
                                    break

                            print(item["Name"], remove_quantity, "Removed Successfully")

                            if item["Quantity"] == 0:
                                cart.remove(item)

                        break

                if not found:
                    print("Product Not Found in Cart")


    # 4. UPDATE PRODUCT QUANTITY

    elif menu_choice == 4:

        if len(cart) == 0:
            print("Your Cart is Empty")

        else:

            while True:

                update_id = int(input("\nEnter Product ID to Update (0 to exit): "))

                if update_id == 0:
                    break

                found = False

                for item in cart:

                    if item["ID"] == update_id:
                        found = True

                        print("1. Increase Quantity")
                        print("2. Decrease Quantity")

                        choice = int(input("Enter Your Choice: "))
                        quantity = int(input("Enter Quantity: "))

                        if quantity <= 0:
                            print("Invalid Quantity")

                        elif choice == 1:

                            for product in products:
                                if product["ID"] == update_id:

                                    if quantity > product["Available Stock"]:
                                        print("Insufficient Stock")

                                    else:
                                        item["Quantity"] += quantity
                                        product["Available Stock"] -= quantity
                                        print("Quantity Increased Successfully")

                                    break

                        elif choice == 2:

                            if quantity > item["Quantity"]:
                                print("Quantity Exceeds Cart Quantity")

                            else:
                                item["Quantity"] -= quantity

                                for product in products:
                                    if product["ID"] == update_id:
                                        product["Available Stock"] += quantity
                                        break

                                print("Quantity Decreased Successfully")

                                if item["Quantity"] == 0:
                                    cart.remove(item)

                        else:
                            print("Invalid Choice")

                        break

                if not found:
                    print("Product Not Found in Cart")


    # 5. VIEW SHOPPING CART

    elif menu_choice == 5:

        print("\nYOUR SHOPPING CART")

        if len(cart) == 0:
            print("Your Cart is Empty")

        else:
            print(f"{'Name':<15}{'Price':<10}{'Quantity':<12}{'Subtotal':<12}")

            grand_total = 0

            for item in cart:
                subtotal = item["Price"] * item["Quantity"]
                grand_total += subtotal

                print(f"{item['Name']:<15}{item['Price']:<10}{item['Quantity']:<12}{subtotal:<12}")

            print("-----------------------------------------")
            print("Grand Total:", grand_total)


    # 6. CALCULATE TOTAL AMOUNT

    elif menu_choice == 6:

        if len(cart) == 0:
            print("Your Cart is Empty")

        else:

            grand_total = 0

            for item in cart:
                subtotal = item["Price"] * item["Quantity"]
                grand_total += subtotal

            print("\nTOTAL AMOUNT:", grand_total)

            discount = 0

            if grand_total > 5000:
                discount = grand_total * 10 / 100
                print("Discount (10%):", discount)

            else:
                print("No Discount Applied")

            coupon_discount = 0

            if applied_coupon is not None:
                coupon_discount = grand_total * coupons[applied_coupon] / 100
                print("Coupon Discount:", coupon_discount)

            final_amount = grand_total - discount - coupon_discount

            print("Final Payable Amount:", final_amount)


    # 7. APPLY COUPON CODE

    elif menu_choice == 7:

        if len(cart) == 0:
            print("Add Products to Your Cart First")

        else:

            coupon_code = input("Enter Coupon Code: ").upper()

            if coupon_code in coupons:
                applied_coupon = coupon_code

                print("Valid Coupon Code!")
                print("Coupon Applied Successfully")
                print("Coupon Discount:", coupons[coupon_code], "%")

            else:
                applied_coupon = None
                print("Invalid Coupon Code")


    # 8. SEARCH PRODUCTS

    elif menu_choice == 8:

        search_name = input("\nEnter Product Name to Search: ").lower()

        found = False

        for product in products:

            if search_name in product["Name"].lower():
                found = True

                print("\nPRODUCT FOUND")
                print(f"{'ID':<10}{'Name':<15}{'Price':<10}{'Available Stock':<15}")

                print(f"{product['ID']:<10}{product['Name']:<15}{product['Price']:<10}{product['Available Stock']:<15}")

        if not found:
            print("Product Not Found")


    # 9. CHECKOUT

    elif menu_choice == 9:

        print("\n========== CHECKOUT ==========")

        if len(cart) == 0:
            print("Your Cart is Empty")

        else:

            print("\nFINAL ORDER SUMMARY")
            print(f"{'Name':<15}{'Price':<10}{'Quantity':<12}{'Subtotal':<12}")

            grand_total = 0

            for item in cart:
                subtotal = item["Price"] * item["Quantity"]
                grand_total += subtotal

                print(f"{item['Name']:<15}{item['Price']:<10}{item['Quantity']:<12}{subtotal:<12}")

            print("-----------------------------------------")
            print("Total Amount:", grand_total)

            discount = 0

            if grand_total > 5000:
                discount = grand_total * 10 / 100
                print("Regular Discount:", discount)

            coupon_discount = 0

            if applied_coupon is not None:
                coupon_discount = grand_total * coupons[applied_coupon] / 100
                print("Coupon Applied:", applied_coupon)
                print("Coupon Discount:", coupon_discount)

            final_amount = grand_total - discount - coupon_discount

            print("-----------------------------------------")
            print("Final Payable Amount:", final_amount)

            confirm = input("\nConfirm Order? (yes/no): ").lower()

            if confirm == "yes":

                order = {
                    "Order ID": order_id,
                    "Products": [item.copy() for item in cart],
                    "Total Amount": final_amount
                }

                order_history.append(order)

                print("\nORDER PLACED SUCCESSFULLY!")
                print("Order ID:", order_id)
                print("Final Amount:", final_amount)
                print("Thank You for Shopping with Us!")

                order_id += 1
                cart.clear()
                applied_coupon = None

            else:
                print("\nOrder Cancelled")
                print("Your Cart is Unchanged")


    # 10. ORDER HISTORY

    elif menu_choice == 10:

        print("\n========== ORDER HISTORY ==========")

        if len(order_history) == 0:
            print("No Previous Orders Found")

        else:

            for order in order_history:

                print("\nOrder ID:", order["Order ID"])

                print(f"{'Name':<15}{'Price':<10}{'Quantity':<12}{'Subtotal':<12}")

                for item in order["Products"]:
                    subtotal = item["Price"] * item["Quantity"]

                    print(f"{item['Name']:<15}{item['Price']:<10}{item['Quantity']:<12}{subtotal:<12}")

                print("Total Amount:", order["Total Amount"])
                print("-----------------------------------------")


    # 11. EXIT

    elif menu_choice == 11:

        print("\nThank You for Shopping with Us!")
        print("Visit Again!")
        break


    # INVALID CHOICE

    else:
        print("Invalid Choice. Please Select Between 1 and 11.")
