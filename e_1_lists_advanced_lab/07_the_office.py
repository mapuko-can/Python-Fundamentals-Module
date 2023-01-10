employees = input().split()
factor = int(input())

employees = list(map(lambda employee: int(employee) * factor, employees))
filtered = list(filter(lambda employee: employee >= (sum(employees) / len(employees)), employees))

if len(filtered) >= len(employees) / 2:
    print(f"Score: {len(filtered)}/{len(employees)}. Employees are happy!")
else:
    print(f"Score: {len(filtered)}/{len(employees)}. Employees are not happy!")