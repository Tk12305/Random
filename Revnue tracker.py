import csv
import random
from datetime import datetime, timedelta

# Configuration
start_date = datetime(2025, 6, 1)
days = 30
streams = ['Retail', 'Wholesale', 'Online']
output_file = 'June_2025_Revenue_Tracker.csv'

# Revenue range per stream (adjust as needed)
revenue_ranges = {
    'Retail': (200, 800),
    'Wholesale': (500, 1500),
    'Online': (100, 600)
}

# Prepare header
header = ['Date'] + streams + ['Total Revenue']

# Generate rows with random values
rows = []
for i in range(days):
    date = (start_date + timedelta(days=i)).strftime('%Y-%m-%d')
    row_num = i + 2  # Excel row number (header is row 1)
    
    # Generate random revenue per stream
    stream_values = [
        random.randint(*revenue_ranges[stream])
        for stream in streams
    ]
    
    # Excel formula for total sum
    formula = f'=SUM(B{row_num}:D{row_num})'
    
    row = [date] + stream_values + [formula]
    rows.append(row)

# Write to CSV
with open(output_file, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(header)
    writer.writerows(rows)

print(f'Revenue tracker with random data saved as {output_file}')
