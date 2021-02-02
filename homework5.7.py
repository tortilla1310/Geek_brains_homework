import json

firm_dict = {}
profit_dict = {}
profit_average = 0
total_profit = 0
i = 0

with open('test-4.txt', 'r') as my_file:
    for line in my_file:
        line_split = line.split(' ')
        company_name = line_split[0]
        profit = int(line_split[2]) - int(line_split[3])

        i += 1
        total_profit += profit
        firm_dict[company_name] = profit

if i > 0:
    profit_average = total_profit / i

    profit_dict["average_profit"] = profit_average

    for key, value in firm_dict.items():
        print(f"Company : {key} profit: {value}")

    for key, value in profit_dict.items():
        print(f"{key} : {value}")

    result_list = [firm_dict, profit_dict]

    with open('output.txt', 'w') as outfile:
        json.dump(result_list, outfile)

