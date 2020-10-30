# David Gonzalez
# 1630338

class FoodItem:
    def __init__(self, name="None", fat=0.0, carbs=0.0, protein=0.0):
        self.name = name
        self.fat = fat
        self.carbs = carbs
        self.protein = protein

    def get_calories(self, num_servings):
        cal = ((self.fat * 9) + (self.carbs * 4) + (self.protein * 4)) * num_servings
        return cal

    def print_info(self):
        print('Nutritional information per serving of {}:'.format(self.name))
        print('   Fat: {:.2f} g'.format(self.fat))
        print('   Carbohydrates: {:.2f} g'.format(self.carbs))
        print('   Protein: {:.2f} g'.format(self.protein))


if __name__ == '__main__':
    item1 = FoodItem()
    item_n = input()
    amount_f = float(input())
    amount_c = float(input())
    amount_p = float(input())

    item2 = FoodItem(item_n, amount_f, amount_c, amount_p)
    num_servings = float(input())

    item1.print_info()
    print("Number of calories for {:.2f} serving(s): {:.2f}".format(num_servings, item1.get_calories(num_servings)))
    print()
    item2.print_info()
    print("Number of calories for {:.2f} serving(s): {:.2f}".format(num_servings, item2.get_calories(num_servings)))
