import os
import re

def fix_stp_file(filepath):
    """Fix FILE_NAME in .stp file to match the actual filename"""
    # Get the actual filename from the path
    actual_filename = os.path.basename(filepath)
    
    # Read the file
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return False
    
    # Find and replace FILE_NAME line
    # Pattern matches both regular and encoded filenames
    # FILE_NAME(\n/* name */ 'anything' or '\X2\...\X0\',
    pattern = r"(FILE_NAME\s*\(\s*/\*\s*name\s*\*/\s*)'[^']*',"
    replacement = f"\\1'{actual_filename}',"
    
    # Check if replacement is needed
    if re.search(pattern, content):
        new_content = re.sub(pattern, replacement, content)
        
        # Only write if content changed
        if new_content != content:
            try:
                with open(filepath, 'w', encoding='utf-8', newline='') as f:
                    f.write(new_content)
                return True
            except Exception as e:
                print(f"Error writing {filepath}: {e}")
                return False
    return False

# Translation dictionary for filenames
translations = {
    '电池盒粗略尺寸': 'Battery_Box_Rough_Dimensions',
}

# Find all .stp files
stp_files = []
for root, dirs, files in os.walk('atom01_mechnaic'):
    for file in files:
        if file.endswith('.stp'):
            stp_files.append(os.path.join(root, file))

# Rename Chinese files first
renamed_count = 0
for filepath in stp_files:
    dirname = os.path.dirname(filepath)
    basename = os.path.basename(filepath)
    
    # Translate filename
    new_basename = basename
    for chinese, english in translations.items():
        new_basename = new_basename.replace(chinese, english)
    
    if new_basename != basename:
        new_filepath = os.path.join(dirname, new_basename)
        os.rename(filepath, new_filepath)
        print(f"✓ Renamed: {basename} → {new_basename}")
        renamed_count += 1
        # Update the list with new path
        stp_files[stp_files.index(filepath)] = new_filepath

# Fix FILE_NAME in each file
fixed_count = 0
for filepath in stp_files:
    if fix_stp_file(filepath):
        fixed_count += 1
        print(f"✓ Fixed FILE_NAME: {os.path.basename(filepath)}")

print(f"\n✓ Renamed {renamed_count} .stp files")
print(f"✓ Fixed FILE_NAME in {fixed_count} .stp files")
print(f"  Total .stp files processed: {len(stp_files)}")
