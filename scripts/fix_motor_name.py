import csv

# Read the CSV file
csv_path = r'atom01_mechnaic\03_URDF\urdf\Atom01_urdf.csv'

with open(csv_path, 'r', encoding='utf-8') as file:
    content = file.read()

# Replace the motor name
old_name = 'DM 4340 rau 3505 Motor 3D'
new_name = 'DM-J4340-2EC_Motor_3D'

content = content.replace(old_name, new_name)

# Write back
with open(csv_path, 'w', encoding='utf-8', newline='') as file:
    file.write(content)

print(f"✓ Replaced all instances of '{old_name}' with '{new_name}'")
