def main():
    pay_coke()

def pay_coke():
    due = 50
    while due > 0:
        print("Amount Due:", due)
        paidMoney = int(input("Insert Coin: "))
        if check_money(paidMoney):
            due -= paidMoney
            if due < 0:
                print("Change Owed:", abs(due))
                break
            elif due == 0:
                print("Change Owed: 0")
                break

def check_money(payedCoin):
    validCoins = [5, 10, 25]
    for coin in validCoins:
        if coin == payedCoin:
            return True

main()