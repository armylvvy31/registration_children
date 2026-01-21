# Метод Хоара
def hoara_sort(data_list, sort_mode):
    if len(data_list) <= 1:
        return data_list
    
    pivot = data_list[len(data_list) // 2]
    left = []
    middle = []
    right = []
    
    for item in data_list:
        should_go_left = False
        
        if sort_mode == 1: # Сортировка для отчета 1 (здоровье убыв. + фамилия возр.)
            if item['health_score'] > pivot['health_score']:
                should_go_left = True
            elif item['health_score'] == pivot['health_score'] and item['surname'] < pivot['surname']:
                should_go_left = True
                
        elif sort_mode == 2: # Сортировка по дате рождения (год, потом месяц, потом день)
            if item['year'] < pivot['year']:
                should_go_left = True
            elif item['year'] == pivot['year'] and item['month'] < pivot['month']:
                should_go_left = True
            elif item['year'] == pivot['year'] and item['month'] == pivot['month'] and item['day'] < pivot['day']:
                should_go_left = True
                
        elif sort_mode == 3: # Сортировка по группе и фамилии
            if item['group'] < pivot['group']:
                should_go_left = True
            elif item['group'] == pivot['group'] and item['surname'] < pivot['surname']:
                should_go_left = True

        if should_go_left:
            left.append(item)
        elif item == pivot:
            middle.append(item)
        else:
            right.append(item)
            
    return hoara_sort(left, sort_mode) + middle + hoara_sort(right, sort_mode)

def needs_treatment_check(kid_record):
    for result in kid_record['health_results']:
        if result == "нуждается":
            return True
    return False
