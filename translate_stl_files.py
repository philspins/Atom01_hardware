import os

# Translation dictionary for soft rubber parts
translations = {
    '软胶': 'Soft_Rubber',
    '下身': 'Lower_Body',
    '腰部下': 'Waist_Lower',
    '腰部上': 'Waist_Upper',
    '脚背': 'Foot_Top',
    '脚底': 'Foot_Sole',
    '小腿膝盖': 'Lower_Leg_Knee',
    '小腿外': 'Lower_Leg_Outer',
    '小腿后': 'Lower_Leg_Rear',
    '小腿前': 'Lower_Leg_Front',
    '小腿内': 'Lower_Leg_Inner',
    '大腿根': 'Thigh_Root',
    '大腿外': 'Thigh_Outer',
    '大腿后': 'Thigh_Rear',
    '大腿前': 'Thigh_Front',
    '大腿内': 'Thigh_Inner',
    '左': 'Left',
    '右': 'Right',
    ' ': '_',  # Replace spaces with underscores
}

# Find all .stl files
stl_files = []
for root, dirs, files in os.walk('atom01_mechnaic'):
    for file in files:
        if file.endswith('.stl'):
            stl_files.append(os.path.join(root, file))

# Rename files
renamed_count = 0
for filepath in stl_files:
    dirname = os.path.dirname(filepath)
    basename = os.path.basename(filepath)
    
    # Translate filename
    new_basename = basename
    for chinese, english in translations.items():
        new_basename = new_basename.replace(chinese, english)
    
    # Clean up any double underscores
    while '__' in new_basename:
        new_basename = new_basename.replace('__', '_')
    
    if new_basename != basename:
        new_filepath = os.path.join(dirname, new_basename)
        try:
            os.rename(filepath, new_filepath)
            print(f"✓ Renamed: {basename}")
            print(f"       → {new_basename}")
            renamed_count += 1
        except Exception as e:
            print(f"✗ Error renaming {basename}: {e}")

print(f"\n✓ Renamed {renamed_count} .stl files")
print(f"  Total .stl files processed: {len(stl_files)}")
