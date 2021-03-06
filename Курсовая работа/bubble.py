def bubble(arr):
    count_compare = 0 # Счетчик количества сравнений
    count_move = 0    # Счетчик количества перемещений
    n = len(arr)      # Количество элементов массива
    min_index = 0     # Минимальный индекс элемента, для которого выполнялась перестановка
    max_index = n     # Максимальный индекс элемента, для которого выполнялась перестановка

    for i in range(n): 
        count_move_step = 0 # Количество перемещений на текущем шаге
        min_index_step = 0  # Минимальный индекс перемещенного элемента на текущем шаге
        max_index_step = n  # Максимальный индекс перемещенного элемента на текущем шаге

        for j in range(1, n):
            # Если индекс стал меньше минимального индекса перемещений с предыдущего шага,
            # тогда перейдем к следующему шагу
            if n-j-1 < min_index:
                break 
            
            count_compare += 1 # Считаем количество сравнений
            if arr[n-j-1] > arr[n-j]: # Arr[n-2] > Arr[n-1] ... Arr[0] > Arr[1]
                arr[n-j], arr[n-j-1] = arr[n-j-1], arr[n-j] # Меняем местами
                count_move += 1 # Считаем количество перемещений
                count_move_step += 1 # Считаем количество перемещений на текущем шаге
                min_index_step = n-j-1 # Запоминаем минимальный индекс перемещенного элемента на текущем шаге 
                
        # Сохраняем минимальный индекс перемещенного элемента на текущем шаге
        min_index = min_index_step

        for j in range(1, n):
            # Если индекс стал больше максимального индекса перемещений с предыдущего шага,
            # тогда перейдем к следующему шагу
            if j+1 >= max_index:
                break 
            
            count_compare += 1 # Считаем количество сравнений
            if arr[j] > arr[j+1]: # Arr[0] > Arr[1] ... Arr[n-3] > Arr[n-2]
                arr[j], arr[j+1] = arr[j+1], arr[j] # Меняем местами
                count_move += 1 # Считаем количество перемещений
                count_move_step += 1 # Считаем количество перемещений на текущем шаге
                max_index_step = j+1 # Запоминаем максимальный индекс перемещенного элемента на текущем шаге 
                
        # Сохраняем максимальный индекс перемещенного элемента на текущем шаге
        max_index = max_index_step
        
        # Если на текущем шаге не было перемещений заканчиваем сортировку
        if count_move_step == 0:
            break
        
    return [count_compare, count_move]
import random
arry = [random.randint(0, 20) for i in range(20)]
print(arry)
bubble(arry)
print(arry)