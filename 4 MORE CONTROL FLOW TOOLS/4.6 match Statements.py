# Match can be used just like switch statements in other languages

answer = input("Which country do you like the most? Vietnam, Myanmar, Cambodia or Laos? ")

match answer:
    case "Vietnam":
        print("Who wouldn't love a good bun of bánh mì?")
    # Multiple patterns can be provided in a single case
    case "Cambodia" | "Myanmar":
        print("Just don't bring up Thailand.")
    case "Laos":
        print("Certified Lao.")
    # Acts as the default if the variable matches no other cases
    case _:
        print("Pretty sure that", answer, "wasn't in the list.")
