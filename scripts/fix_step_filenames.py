import os
import re

def fix_step_file(filepath):
    """Fix FILE_NAME in STEP file to match the actual filename"""
    # Get the actual filename from the path
    actual_filename = os.path.basename(filepath)
    
    # Read the file
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # Find and replace FILE_NAME line
    # Pattern: FILE_NAME ('anything.STEP',
    pattern = r"FILE_NAME \('[^']*\.STEP',"
    replacement = f"FILE_NAME ('{actual_filename}',"
    
    # Check if replacement is needed
    if re.search(pattern, content):
        new_content = re.sub(pattern, replacement, content)
        
        # Only write if content changed
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8', newline='') as f:
                f.write(new_content)
            return True
    return False

# Find all .STEP files
step_files = []
for root, dirs, files in os.walk('atom01_mechnaic'):
    for file in files:
        if file.endswith('.STEP'):
            step_files.append(os.path.join(root, file))

# Fix each file
fixed_count = 0
for filepath in step_files:
    if fix_step_file(filepath):
        fixed_count += 1
        print(f"✓ Fixed: {filepath}")

print(f"\n✓ Fixed {fixed_count} STEP files")
print(f"  Total STEP files processed: {len(step_files)}")
