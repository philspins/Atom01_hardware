import os
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

def wrap_text(text, max_width, canvas_obj, font_name, font_size):
    """Wrap text to fit within max_width"""
    lines = []
    paragraphs = text.split('\n')
    
    for paragraph in paragraphs:
        if not paragraph.strip():
            lines.append('')
            continue
            
        words = paragraph.split()
        current_line = []
        
        for word in words:
            test_line = ' '.join(current_line + [word])
            width = canvas_obj.stringWidth(test_line, font_name, font_size)
            
            if width <= max_width:
                current_line.append(word)
            else:
                if current_line:
                    lines.append(' '.join(current_line))
                current_line = [word]
        
        if current_line:
            lines.append(' '.join(current_line))
    
    return lines

def create_pdf_from_text(text_content, output_path):
    """Create a PDF from text content"""
    try:
        # Create canvas
        c = canvas.Canvas(output_path, pagesize=letter)
        width, height = letter
        
        # Set margins
        margin_left = 0.75 * inch
        margin_right = 0.75 * inch
        margin_top = 0.75 * inch
        margin_bottom = 0.75 * inch
        
        max_width = width - margin_left - margin_right
        
        # Font settings
        font_name = "Helvetica"
        font_size = 10
        line_height = font_size + 2
        
        # Wrap text
        lines = wrap_text(text_content, max_width, c, font_name, font_size)
        
        # Draw text
        y_position = height - margin_top
        
        for line in lines:
            # Check if we need a new page
            if y_position < margin_bottom:
                c.showPage()
                y_position = height - margin_top
            
            c.setFont(font_name, font_size)
            c.drawString(margin_left, y_position, line)
            y_position -= line_height
        
        c.save()
        return True
    except Exception as e:
        print(f"  Error creating PDF: {e}")
        return False

# Find all translated text files
translated_dir = 'translated_pdfs'
text_files = [f for f in os.listdir(translated_dir) if f.endswith('_translated.txt')]

print(f"Found {len(text_files)} translated text files\n")

processed = 0
failed = 0

for text_file in text_files:
    text_path = os.path.join(translated_dir, text_file)
    
    # Parse the filename to get original path
    # Format: folder1_folder2_originalname_translated.txt
    parts = text_file.replace('_translated.txt', '').split('_')
    
    # Reconstruct the path
    if text_file.startswith('00_Docs_'):
        folder = 'atom01_mechnaic/00_Docs'
        original_name = '_'.join(parts[2:]) + '.pdf'
    elif text_file.startswith('01_SW_Project_20cm_Foot_20cm'):
        folder = 'atom01_mechnaic/01_SW_Project/20cm_Foot'
        original_name = '20cm_Foot.pdf'
    elif text_file.startswith('01_SW_Project_'):
        folder = 'atom01_mechnaic/01_SW_Project'
        original_name = '_'.join(parts[2:]) + '.pdf'
    elif text_file.startswith('02_Manufacturing_CNC_Machining_'):
        folder = 'atom01_mechnaic/02_Manufacturing/CNC_Machining'
        original_name = '_'.join(parts[3:]) + '.pdf'
    else:
        print(f"  Warning: Could not parse path for {text_file}")
        failed += 1
        continue
    
    # Create output filename
    base_name = original_name.replace('.pdf', '')
    output_name = f"{base_name}_ENG.pdf"
    output_path = os.path.join(folder, output_name)
    
    print(f"Processing: {original_name}")
    print(f"  Output: {output_path}")
    
    # Read translated text
    try:
        with open(text_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"  ✗ Error reading {text_file}: {e}")
        failed += 1
        continue
    
    # Create PDF
    if create_pdf_from_text(content, output_path):
        print(f"  ✓ Created {output_name}")
        processed += 1
    else:
        failed += 1

print(f"\n{'='*60}")
print(f"PDF Creation Summary:")
print(f"  Total text files: {len(text_files)}")
print(f"  Successfully created: {processed}")
print(f"  Failed: {failed}")
print(f"{'='*60}")
