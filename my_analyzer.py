import csv

def analyze_csv(lines):
    total_revenue = 0.0
    client_totals = {}
    
    reader = csv.DictReader(lines)
    for row in reader:
        client = row['client']
        revenue = int(row['qty']) * float(row['price'])
        client_totals[client] = client_totals.get(client, 0.0) + revenue
        total_revenue += revenue

    average_revenue = total_revenue / len(client_totals) if client_totals else 0.0
    
    return {
        'total_revenue': total_revenue,
        'average_revenue': average_revenue,
        'clients': client_totals
    }  

def generate_csv_report(clients_dict):
    lines = ['Клиент;Выручка;Статус']
    for client, total in clients_dict.items():
        status = 'VIP' if total > 30000 else 'Обычный'
        formatted_total = f'{total:.2f}'.replace('.', ',')
        lines.append(f'{client};{formatted_total};{status}')
    return '\n'.join(lines).encode('cp1251')

      

