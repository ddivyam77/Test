def main():
    print("Amount Due: 50")
    amount_due = 50
    accepted_coins = [5, 10, 25]

    while amount_due > 0:
        coin = int(input("Insert Coin: ").strip())

        if coin in accepted_coins:  
            amount_due -= coin
            if amount_due > 0:
                print(f"Amount Due: {amount_due}")
            else:
                print(f"Change Owed: {abs(amount_due)}")
        else:
            print(f"Amount Due: {amount_due}")

main()
