def even_numbers(integer_list: list):
  index = 0 # Initialize index helper
  even_list = [] # Initialize the new list for the even integers
  for item in integer_list:
    if integer_list[index] % 2 == 0:
      even_list = integer_list[index]
    index += 1
  return even_list

if __name__ == "__main__":
  my_list = [1, 2, 3, 4, 5]
  new_list = even_numbers(my_list)
  print("original", my_list)
  print("new", new_list)
