sale_list = [50, 75, 150, 125, 100]
week_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
max_sale = max(sale_list)
max_index = sale_list.index(max_sale)
max_day = week_list[max_index]

#output
print('Max Sale:', max_sale)
print('Day:', max_day)

