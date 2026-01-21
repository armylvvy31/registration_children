import deti
import obrabotka
import sys

def load_kids_data(filename):
    try:
        f = open(filename, 'r', encoding='utf-8')
    except FileNotFoundError:
        print("файл не найден!")
        return None
    
    kids_data_list = []
    for line in f:
        record = deti.create_kid_record(line)
        if record:
            kids_data_list.append(record)
    f.close()
    
    return kids_data_list

def main():
    kids_data_list = load_kids_data('baza_detey.txt')
    
    if kids_data_list is None:
        return
    
    if not kids_data_list:
        print("список пуст")
        return
    
    # ОТЧЕТ №1:
    print("ОТЧЕТ 1: Все дети (по количеству 'здоров' и фамилии)")
    sorted_report1 = obrabotka.hoara_sort(kids_data_list, 1)
    for kid in sorted_report1:
        print(f"Здоров: {kid['health_score']} | {kid['surname']} | {kid['name']}")
    
    # ОТЧЕТ №2:
    target_group = "средняя"
    group_kids_list = []
    for kid in kids_data_list:
        if kid['group'] == target_group:
            group_kids_list.append(kid)
    
    print(f"\nОТЧЕТ 2: Группа '{target_group}' (по дате рождения)")
    sorted_report2 = obrabotka.hoara_sort(group_kids_list, 2)
    for kid in sorted_report2:
        print(f"{kid['year']:04d}-{kid['month']:02d}-{kid['day']:02d} | {kid['surname']}")
    
    # ОТЧЕТ №3:
    kids_needing_treatment = []
    for kid in kids_data_list:
        if obrabotka.needs_treatment_check(kid):
            kids_needing_treatment.append(kid)
    
    print("\nОТЧЕТ 3: Нуждаются в лечении (по группам и фамилиям)")
    sorted_report3 = obrabotka.hoara_sort(kids_needing_treatment, 3)
    for kid in sorted_report3:
        print(f"{kid['group']} | {kid['surname']} | Врачи: {kid['health_results']}")

if __name__ == "__main__":
    main()