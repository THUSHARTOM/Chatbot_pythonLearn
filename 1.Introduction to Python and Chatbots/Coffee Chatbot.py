# Define your functions

def coffee_bot():
    print("Welcome to the cafe!")
    a = get_size()
    b = get_drink_type()
    print("Alright, thats a " + a + " " + b + "!")
    name = input("can I get your name please?")
    print("Thanks, " + name + "! YOur drink will be ready shortly.")


def get_size():
    res = input('What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n> ')

    if res == "a":
        return "small"
    elif res == "b":
        return "medium"
    elif res == "c":
        return "large"
    else:
        print(
            " I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response.")
        return get_size()


def get_drink_type():
    res = input("What type of drink would you like? \n[a]Brewed Coffee \n[b]Mocha \n[c]Latte")
    if res == "a":
        return "brewed Coffee"
    elif res == "b":
        return "mocha"
    elif res == "c":
        return order_latte()
    else:
        print(
            " I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response.")
        return get_drink_type()


def order_latte():
    res = input("And what kind of milk for your latte? \n[a]2% milk  \n[b]non-fat milk \n[c]soy milk")
    if res == "a":
        return "latte"
    elif res == "b":
        return "non-fat latte"
    elif res == "c":
        return "soy latte"
    else:
        print(
            " I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response.")
        return order_latte()


# Call coffee_bot()!
coffee_bot()

