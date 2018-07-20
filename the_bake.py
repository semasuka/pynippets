"""
Pete likes to bake some cakes. He has some recipes and ingredients. 
Unfortunately he is not good in maths. Can you help him to find out, 
how many cakes he could bake considering his recipes?

Write a function cakes(), which takes the recipe (object) and the 
available ingredients (also an object) and returns the maximum number 
of cakes Pete can bake (integer). For simplicity there are no units 
for the amounts (e.g. 1 lb of flour or 200 g of sugar are simply 1 or 200). 
Ingredients that are not present in the objects, can be considered as 0.

Examples:

# must return 2
cakes({flour: 500, sugar: 200, eggs: 1}, {flour: 1200, sugar: 1200, eggs: 5, milk: 200})
# must return 0
cakes({apples: 3, flour: 300, sugar: 150, milk: 100, oil: 100}, {sugar: 500, flour: 2000, milk: 2000})
"""
import collections
def cakes(recipe, available):
    key_matched = 0
    available_matching = {}
    #checking if we have all the recipe in the available
    for key in available.keys():
        if key in recipe:
            key_matched+=1
    #we have all
    if key_matched == len(recipe):
        #create a new dic without the unneccessary stuff that are required in the recipe
        for key_av,val_av in available.items():
            for key_rec,val_rec in recipe.items():
                if key_av == key_rec:
                    available_matching.update({key_av:val_av})
        #container for sorted available and recipe
        rec_values = []
        av_value = []

        for key,value in sorted(available_matching.items()):
            av_value.append(value)
        for key,value in sorted(recipe.items()):
            rec_values.append(value)
        #add number of possible recipe can come from the quantity available
        recipe_count_list = list(map(lambda x,y:int(x/y), av_value,rec_values))
        #return the minimum recipe int the list
        no_cake = min(recipe_count_list)
        return no_cake
    #we dont have all the recipe required
    else:
        return 0



recipe = {"flour": 500, "sugar": 200, "eggs": 1}
available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
print(cakes(recipe, available))