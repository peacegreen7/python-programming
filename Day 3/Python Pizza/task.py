def select_pizza_simple():
    print("Welcome to Python Pizza Deliveries!")
    size = input("What size pizza do you want? S, M or L: ")
    pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
    extra_cheese = input("Do you want extra cheese? Y or N: ")
    amount_extra_pepperoni = 0
    if size == 'S':
        price = 15
        if pepperoni == 'Y':
            amount_extra_pepperoni = 2
    elif size == 'M':
        price = 20
        if pepperoni == 'Y':
            amount_extra_pepperoni = 3
    elif size == 'L':
        price = 25
        if pepperoni == 'Y':
            amount_extra_pepperoni = 3
    else:
        print('You input incorrect size. Please input again.')
        exit()

    if extra_cheese == 'Y':
        price = price + amount_extra_pepperoni + 1
    else:
        price = price + amount_extra_pepperoni

    print(f'Your final bill is: ${price}.')


def select_pizza_optimize():

    print('Welcome to Python Pizza Deliveries!')

    size = input("What size pizza do you want? S, M or L: ").upper()
    pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").upper()
    extra_cheese = input("Do you want extra cheese? Y or N: ").upper()

    # Defines size and extra charges using dictionaries
    prices = {'S': 15, 'M': 20, 'L': 25}
    pepperoni_cost = {'S': 2, 'M': 3, 'L': 3}
    cheese_cost = 1

    # Validates size input
    if size not in prices:
        print('You input incorrect size. Please input again.')
        exit()

    # Calculate total price
    if pepperoni == 'Y':
        if extra_cheese == 'Y':
            total = prices[size] + pepperoni_cost[size] + cheese_cost
        else:
            total = prices[size] + pepperoni_cost[size]
    else:
        if extra_cheese == 'Y':
            total = prices[size] + cheese_cost
        else:
            total = prices[size]

    # another way
    total_another = prices[size] + (pepperoni_cost[size] if pepperoni == 'Y' else 0) + (cheese_cost if extra_cheese == 'Y' else 0)
    print(f'Your final bill is: ${total}.')
    print(f'Your final bill is: ${total_another}.')




if __name__ == '__main__':
    # select_pizza_simple()
    print('-------------------------------------')
    select_pizza_optimize()
