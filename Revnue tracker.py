import csv
from datetime import datetime, timedelta

# Configuration
start_date = datetime(2025, 6, 1)
days = 30
streams = ['Retail', 'Wholesale', 'Online']
output_file = 'June_2025_Revenue_Tracker.csv'

# Prepare header
header = ['Date'] + streams + ['Total Revenue']

# Generate rows
rows = []
for i in range(days):
    date = (start_date + timedelta(days=i)).strftime('%Y-%m-%d')
    row_num = i + 2  # Excel rows start at 1, with header on row 1
    formula = f'=SUM(B{row_num}:D{row_num})'
    row = [date] + [''] * len(streams) + [formula]
    rows.append(row)

# Write to CSV
with open(output_file, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(header)
    writer.writerows(rows)

print(f'Revenue tracker saved as {output_file}')
