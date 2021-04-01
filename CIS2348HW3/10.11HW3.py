#Ali Rajgarah 1586471

class FoodItem:

### defining default values ###

    def __init__(self, name=None, fat=0.0, carbs=0.0, protein=0.0):
        self.name = name
        self.fat = fat
        self.carbs = carbs
        self.protein = protein

###

    def get_calories(self, num_servings):
        calories = ((self.fat * 9) + (self.carbs * 4) + (self.protein * 4)) * num_servings;
        return calories

    def print_info(self):
        print('Nutritional information per serving of {}:'.format(self.name))
        print('   Fat: {:.2f} g'.format(self.fat))
        print('   Carbohydrates: {:.2f} g'.format(self.carbs))
        print('   Protein: {:.2f} g'.format(self.protein))


### getting input for name, amount of fat, amount of carbs, amount of protein ###

if __name__ == "__main__":
    first_meal = FoodItem()
    item_name = input()
    amount_fat = float(input())
    amount_carbs = float(input())
    amount_protein = float(input())
    second_meal = FoodItem(item_name, amount_fat, amount_carbs, amount_protein)
    num_servings = float(input())

### print the input in the specified format ###

    first_meal.print_info()
    print('Number of calories for {:.2f} serving(s): {:.2f}'.format(num_servings,
                                                                    first_meal.get_calories(num_servings)))

    print()

    second_meal.print_info()
    print('Number of calories for {:.2f} serving(s): {:.2f}'.format(num_servings,
                                                                    second_meal.get_calories(num_servings)))