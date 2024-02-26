import pytest
from budget import Category, create_spend_chart


def test_category():
  food = Category("Food")
  food.deposit(1000, "initial deposit")
  food.withdraw(10.15, "groceries")
  assert food.get_balance() == 989.85
  assert food.check_funds(100) == True
  assert food.check_funds(10000) == False


def test_create_spend_chart():
  food = Category("Food")
  clothing = Category("Clothing")
  auto = Category("Auto")
  food.deposit(1000, "initial deposit")
  clothing.deposit(1000, "initial deposit")
  auto.deposit(1000, "initial deposit")
  food.withdraw(10.15, "groceries")
  clothing.withdraw(25.55, "jacket")
  auto.withdraw(100, "gas")
  auto.withdraw(200, "repair")
  assert create_spend_chart([food, clothing, auto]) == (
      "Percentage spent by category\n100|          \n 90|          \n 80|          \n 70|    o     \n 60|    o     \n 50|    o     \n 40|    o     \n 30|    o     \n 20|    o     \n 10|    o  o  \n  0| o  o  o  \n    ----------\n     F  C  A  "
  )


if __name__ == "__main__":
  pytest.main()
