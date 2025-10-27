import sys

def parse_log_line(line: str):
    parts = line.strip().split(' ', 3)
    
    if len(parts) < 4:
        return {}
    
    return {
        'date': parts[0],
        'time': parts[1],
        'level': parts[2],
        'message': parts[3]
    }


def load_logs(file_path: str):
    logs = []
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            logs = [parse_log_line(line) for line in file if line.strip()]
            logs = list(filter(lambda log: log, logs))
    except:
        print("Помилка при читанні файлу")
        sys.exit(1)
    
    return logs


def filter_logs_by_level(logs, level: str):
    return list(filter(lambda log: log.get('level', '').upper() == level.upper(), logs))


def count_logs_by_level(logs):
    counts = {}
    
    for log in logs:
        level = log.get('level', 'UNKNOWN')
        counts[level] = counts.get(level, 0) + 1
    
    return counts


def display_log_counts(counts):
    print("-----------------|----------")
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    
    for level in sorted(counts.keys()):
        print(f"{level:<16} | {counts[level]}")


def display_log_details(logs, level: str):
    print(f"Деталі логів для рівня '{level.upper()}':")
    
    for log in logs:
        print(f"{log['date']} {log['time']} - {log['message']}")


def main():
    if len(sys.argv) < 2:
        print("Використання: python task_3.py /path/to/logfile.log [log_level]")
        sys.exit(1)
    
    file_path = sys.argv[1]
    log_level = sys.argv[2] if len(sys.argv) > 2 else None
    
    logs = load_logs(file_path)
    
    if not logs:
        print("Попередження: Файл не містить коректних записів логів.")
        return
    
    counts = count_logs_by_level(logs)
    
    display_log_counts(counts)
    
    if log_level:
        filtered_logs = filter_logs_by_level(logs, log_level)
        
        if filtered_logs:
            display_log_details(filtered_logs, log_level)
        else:
            print(f"Записів з рівнем '{log_level.upper()}' не знайдено.")


print(main())

