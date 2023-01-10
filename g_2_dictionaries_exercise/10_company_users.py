companies = {}
while True:
    command = input()
    if command == "End":
        break
    company_name, employee_id = command.split(" -> ")

    if company_name not in companies.keys():
        companies[company_name] = []
    if employee_id not in companies[company_name]:
        companies[company_name].append(employee_id)

for company_name, employee_id in companies.items():
    print(company_name)
    for id in employee_id:
        print(f"-- {id}")

# companies = sorted(companies.items(), key=lambda x: (x[0], x[1]))
# for company_name, employee_id in companies:
#     print(company_name)
#     for id in employee_id:
#         print(f"-- {id}")
