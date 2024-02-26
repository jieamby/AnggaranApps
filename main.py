from budget import Category, create_spend_chart


def main():
  food = Category("Food")
  clothing = Category("Clothing")
  auto = Category("Auto")
  food.deposit(1000, "initial deposit")
  clothing.deposit(1000, "initial deposit")
  food.withdraw(10.15, "groceries")
  clothing.withdraw(25.55, "jacket")
  auto.withdraw(100, "gas")
  auto.withdraw(200, "repair")
  print(food)
  print(clothing)
  print(auto)
  print(create_spend_chart([food, clothing, auto]))


if __name__ == "__main__":
  main()
