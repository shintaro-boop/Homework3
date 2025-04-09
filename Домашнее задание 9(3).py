
with open('task_3.txt', 'r') as file_in, open('task_4.txt', 'w') as file_out:
    for line in file_in:
        line = line.strip()
        if not line.isspace() and line:
            file_out.write(line + '\n')
with open('task_4.txt', 'r', encoding='utf-8') as isxod :
    numbers = [int(line.strip()) for line in isxod]
    sorted_numbers = sorted(numbers, reverse=True)
    result = sum(sorted_numbers[:3])
    print(f"Сумма трёх наибольших чисел: {result}")