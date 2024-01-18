import datetime, os, time
from sqlalchemy import Column, Integer, String, Float, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///cafeteria.db")
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


class FoodMenu(Base):
    __tablename__ = "food_menu"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Float)
    category = Column(String)

    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category


# Base.metadata.create_all(engine) # cia DB sukurimui


def add_dish():
    os.system("cls")
    print("\nAdding new dish")
    name = str(input("\nEnter name: "))
    price = str(input("Enter price: "))
    category = str(input("Enter category: "))

    new_dish = FoodMenu(name, price, category)
    session.add(new_dish)
    session.commit()
    print(f"\Dish {name} {price} to category {category} has been added")
    time.sleep(1.5)


def get_food_menu():
    categories = session.query(FoodMenu.category).distinct().all()

    while True:
        os.system("cls")
        counter = 1
        print("\n--Categories--\n")
        for x in categories:
            print(f"{counter}. {x[0].capitalize()}")
            counter += 1

        try:
            selection = int(input("\nSelect category: ")) - 1
            selected_item = categories[selection]
        except Exception:
            print(
                "\nPlease enter number from list provided without any symbols and spaces."
            )
            time.sleep(1.5)
            continue

        os.system("cls")
        print(f"\n--{selected_item[0].capitalize()}--\n")
        food_list = session.query(FoodMenu).filter_by(category=selected_item[0]).all()
        counter = 1
        print("       |DISH|                     |PRICE|")
        for x in food_list:
            # print(f"{counter}. {x.name} {x.price}")
            print(f"{counter}. {x.name:<32}{x.price:>3} €")
            counter += 1
        input()
        break
