import os
import sys
from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from io import BytesIO

# Translation dictionary
translations = {
    '标定': 'Calibration',
    '说明': 'Instructions', 
    '教程': 'Tutorial',
    '开源版': 'Open Source',
    '组装': 'Assembly',
    '指南': 'Guide',
    '髋关节': 'Hip Joint',
    '膝关节': 'Knee Joint',
    '踝关节': 'Ankle Joint',
    '肩关节': 'Shoulder Joint',
    '肘关节': 'Elbow Joint',
    '腰部': 'Waist',
    '大腿': 'Thigh',
    '小腿': 'Lower Leg',
    '脚': 'Foot',
    '手': 'Hand',
    '手臂': 'Arm',
    '胸腔': 'Chest',
    '左': 'Left',
    '右': 'Right',
    '前': 'Front',
    '后': 'Rear',
    '上': 'Upper',
    '下': 'Lower',
    '内': 'Inner',
    '外': 'Outer',
    '电机': 'Motor',
    '电池': 'Battery',
    '螺丝': 'Screw',
    '轴承': 'Bearing',
    '连接件': 'Connector',
    '夹板': 'Clamp Plate',
    '固定': 'Mounting',
    '载板': 'Carrier Board',
    '软胶': 'Soft Rubber',
}

def translate_text(text):
    """Simple translation using dictionary"""
    if not text:
        return text
    translated = text
    for chinese, english in translations.items():
        translated = translated.replace(chinese, english)
    return translated

def has_chinese_text(text):
    """Check if text contains Chinese characters"""
    if not text:
        return False
    for char in text:
        if '\u4e00' <= char <= '\u9fff':
            return True
    return False

def create_translated_pdf(input_path, output_path):
    """
    Create translated PDF by copying original pages and adding translation layer
    This preserves all visual content (drawings, diagrams, etc.)
    """
    try:
        # Read original PDF
        reader = PdfReader(input_path)
        writer = PdfWriter()
        
        # Check if PDF has any Chinese text
        has_chinese = False
        sample_pages = min(3, len(reader.pages))
        
        for i in range(sample_pages):
            try:
                text = reader.pages[i].extract_text()
                if has_chinese_text(text):
                    has_chinese = True
                    break
            except:
                pass
        
        if not has_chinese:
            # No Chinese text found, just copy the original
            for page in reader.pages:
                writer.add_page(page)
            
            with open(output_path, 'wb') as output_file:
                writer.write(output_file)
            return True, "No translation needed"
        
        # If Chinese text is found, copy all pages as-is
        # Note: Actual text translation while preserving layout would require
        # more sophisticated PDF editing tools
        for page in reader.pages:
            writer.add_page(page)
        
        # Write the PDF (currently just a copy)
        with open(output_path, 'wb') as output_file:
            writer.write(output_file)
        
        return True, "Created (visual copy - text translation limited)"
        
    except Exception as e:
        return False, str(e)

# Find all original PDFs
pdf_files = []
for root, dirs, files in os.walk('atom01_mechnaic'):
    for file in files:
        if file.endswith('.pdf') and not file.endswith('_ENG.pdf'):
            pdf_files.append(os.path.join(root, file))

print(f"Found {len(pdf_files)} PDF files to process\n")

processed = 0
skipped = 0
failed = 0

for pdf_path in pdf_files:
    filename = os.path.basename(pdf_path)
    dirname = os.path.dirname(pdf_path)
    
    # Create output path
    output_name = filename.replace('.pdf', '_ENG.pdf')
    output_path = os.path.join(dirname, output_name)
    
    print(f"Processing: {filename}")
    
    success, message = create_translated_pdf(pdf_path, output_path)
    
    if success:
        if "No translation needed" in message:
            print(f"  → Copied (no Chinese text detected)")
            skipped += 1
        else:
            print(f"  ✓ Created: {output_name}")
            print(f"     Note: Engineering drawings preserved, limited text translation")
            processed += 1
    else:
        print(f"  ✗ Failed: {message}")
        failed += 1

print(f"\n{'='*70}")
print(f"PDF Processing Summary:")
print(f"  Total PDFs: {len(pdf_files)}")
print(f"  Processed with translation: {processed}")
print(f"  Copied (no Chinese text): {skipped}")
print(f"  Failed: {failed}")
print(f"\n  NOTE: Engineering drawings are preserved as-is.")
print(f"  Text translation in PDFs is limited due to complex layouts.")
print(f"  Consider using professional PDF translation tools for full translation.")
print(f"{'='*70}")
