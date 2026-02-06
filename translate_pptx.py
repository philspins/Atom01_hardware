import os
import shutil
from zipfile import ZipFile
import xml.etree.ElementTree as ET

# Translation dictionary for calibration instructions
translations = {
    '标定说明': 'Calibration_Instructions',
    '标定': 'Calibration',
    '说明': 'Instructions',
    # Add more translations as needed based on content
}

def rename_pptx_files():
    """Rename .pptx files from Chinese to English"""
    pptx_files = []
    
    # Find all .pptx files
    for root, dirs, files in os.walk('atom01_mechnaic'):
        for file in files:
            if file.endswith('.pptx') and not file.startswith('~$'):
                pptx_files.append(os.path.join(root, file))
    
    renamed_count = 0
    for filepath in pptx_files:
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
    
    return renamed_count

# Rename files
count = rename_pptx_files()
print(f"\n✓ Renamed {count} PowerPoint files")
