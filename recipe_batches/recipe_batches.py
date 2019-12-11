#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  batches = 0
  making = True
  def make_batch():
    for k in recipe.keys():
      nonlocal making
      try:
        ingredients[k] -= recipe[k]
        if ingredients[k] < 0:
          making = False
          return
      except:
        making = False
        return
    nonlocal batches
    batches += 1
  while making:
    make_batch()

  return batches


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))