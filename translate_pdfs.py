import os
import sys

# Check if required libraries are installed
try:
    import PyPDF2
    print("✓ PyPDF2 is available")
except ImportError:
    print("✗ PyPDF2 not found, attempting to install...")
    os.system(f"{sys.executable} -m pip install PyPDF2 --quiet")

try:
    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import letter, A4
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    print("✓ reportlab is available")
except ImportError:
    print("✗ reportlab not found, attempting to install...")
    os.system(f"{sys.executable} -m pip install reportlab --quiet")

# Re-import after installation
try:
    import PyPDF2
    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import letter, A4
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    print("\n✓ All required libraries are ready")
except ImportError as e:
    print(f"\n✗ Failed to import required libraries: {e}")
    print("Please install manually: pip install PyPDF2 reportlab")
    sys.exit(1)

# Translation dictionary (expanded from previous work)
translations = {
    # Common terms
    '标定': 'Calibration',
    '说明': 'Instructions',
    '教程': 'Tutorial',
    '开源版': 'Open Source Version',
    '组装指南': 'Assembly Guide',
    '标准操作程序': 'Standard Operating Procedure',
    
    # Parts
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
    
    # Directions
    '左': 'Left',
    '右': 'Right',
    '前': 'Front',
    '后': 'Rear/Back',
    '上': 'Upper',
    '下': 'Lower',
    '内': 'Inner',
    '外': 'Outer',
    
    # Components
    '电机': 'Motor',
    '电池': 'Battery',
    '螺丝': 'Screw',
    '轴承': 'Bearing',
    '连接件': 'Connector',
    '夹板': 'Clamp Plate',
    '固定': 'Mounting/Fixed',
    '载板': 'Carrier Board',
    '软胶': 'Soft Rubber',
    
    # Actions
    '安装': 'Install/Assembly',
    '拆卸': 'Disassemble',
    '调试': 'Debug/Adjust',
    '测试': 'Test',
    '注意': 'Note/Attention',
    '警告': 'Warning',
    '步骤': 'Step',
}

def extract_text_from_pdf(pdf_path):
    """Extract text from PDF file"""
    try:
        text = ""
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            for page_num, page in enumerate(pdf_reader.pages):
                try:
                    page_text = page.extract_text()
                    if page_text:
                        text += f"\n--- Page {page_num + 1} ---\n"
                        text += page_text
                except Exception as e:
                    print(f"  Warning: Could not extract page {page_num + 1}: {e}")
        return text
    except Exception as e:
        print(f"  Error reading {pdf_path}: {e}")
        return None

def translate_text(text):
    """Simple translation using dictionary replacement"""
    translated = text
    for chinese, english in translations.items():
        translated = translated.replace(chinese, english)
    return translated

def save_as_text(content, output_path):
    """Save translated content as text file"""
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    except Exception as e:
        print(f"  Error saving {output_path}: {e}")
        return False

# Find all PDF files
pdf_files = []
for root, dirs, files in os.walk('atom01_mechnaic'):
    for file in files:
        if file.endswith('.pdf') and not file.startswith('.'):
            pdf_files.append(os.path.join(root, file))

print(f"\nFound {len(pdf_files)} PDF files to process\n")

# Create output directory
output_dir = 'translated_pdfs'
os.makedirs(output_dir, exist_ok=True)

# Process each PDF
processed = 0
failed = 0

for pdf_path in pdf_files:
    print(f"Processing: {os.path.basename(pdf_path)}")
    
    # Extract text
    text = extract_text_from_pdf(pdf_path)
    
    if text:
        # Translate
        translated_text = translate_text(text)
        
        # Create output filename
        rel_path = os.path.relpath(pdf_path, 'atom01_mechnaic')
        output_name = rel_path.replace('.pdf', '_translated.txt').replace('\\', '_').replace('/', '_')
        output_path = os.path.join(output_dir, output_name)
        
        # Save as text file
        if save_as_text(translated_text, output_path):
            print(f"  ✓ Saved: {output_name}")
            processed += 1
        else:
            failed += 1
    else:
        print(f"  ✗ Failed to extract text")
        failed += 1

print(f"\n{'='*60}")
print(f"Translation Summary:")
print(f"  Total PDFs found: {len(pdf_files)}")
print(f"  Successfully processed: {processed}")
print(f"  Failed: {failed}")
print(f"  Output directory: {output_dir}/")
print(f"{'='*60}")
