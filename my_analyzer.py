import csv
total_revenue = 0
client_totals = {}
with open('sales.csv', encoding='cp1251') as f:
    reader = csv.DictReader(f)
    for row in reader:
        client = row['client']
        revenue = int(row['qty']) * float(row['price'])
        client_totals[client] = client_totals.get(client, 0) + revenue
        total_revenue += revenue

for client, total in client_totals.items():
    if total > 30000:
        print(f'Сумма по [VIP] клиенту {client} составила {total:.2f} рублей.')
    else:
        print(f'Сумма по клиенту {client} составила {total:.2f} рублей.')           
print(f'Итого сумма составила {total_revenue:.2f} рублей.')  

with open('report.csv', mode='w', encoding='cp1251', newline='') as f:
    writer = csv.writer(f, delimiter=';')
    writer.writerow(['Клиент', 'Выручка', 'Статус'])
    for client, total in client_totals.items():
        status = 'Обычный'
        if total > 30000:
            status = 'VIP'
        writer.writerow([client, round(total, 2), status])        
      

