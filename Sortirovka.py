class InsertionSort:
  def sort_list(self, input_list):
      if not isinstance(input_list, list):
          raise ValueError("Аргумент не список!")
      
      # Создаем копию списка
      list_to_sort = input_list.copy()
      
      for i in range(1, len(list_to_sort)):
          key = list_to_sort[i]
          j = i - 1
          while j >= 0 and key < list_to_sort[j]:
              list_to_sort[j + 1] = list_to_sort[j]
              j -= 1
          list_to_sort[j + 1] = key
      
      return list_to_sort
      
# Функция для проверки результата сортировки
def check_sort(input_list, sorted_list):
    if not isinstance(input_list, list) or not isinstance(sorted_list, list):
       raise ValueError("Оба аргумента должны быть списками!")
    
    return input_list == sorted_list
    
    
# Создаем экземпляр класса InsertionSort
sorter = InsertionSort()

# Сортируем список
sorted_list = sorter.sort_list([5, 3, 1, 4, 2])
print(sorted_list) # Вывод: [1, 2, 3, 4, 5]

# Проверяем результат
print(check_sort(sorted_list, [1, 2, 3, 4, 5])) # Вывод: True
