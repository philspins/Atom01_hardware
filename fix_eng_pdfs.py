import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch

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
        c = canvas.Canvas(output_path, pagesize=letter)
        width, height = letter
        
        margin_left = 0.75 * inch
        margin_right = 0.75 * inch
        margin_top = 0.75 * inch
        margin_bottom = 0.75 * inch
        
        max_width = width - margin_left - margin_right
        font_name = "Helvetica"
        font_size = 10
        line_height = font_size + 2
        
        lines = wrap_text(text_content, max_width, c, font_name, font_size)
        y_position = height - margin_top
        
        for line in lines:
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

# First, remove all incorrectly named PDFs
print("Removing incorrectly named PDFs...")
for root, dirs, files in os.walk('atom01_mechnaic'):
    for file in files:
        if file.endswith('_ENG.pdf'):
            filepath = os.path.join(root, file)
            try:
                os.remove(filepath)
                print(f"  Removed: {filepath}")
            except Exception as e:
                print(f"  Error removing {filepath}: {e}")

print("\nCreating correctly named PDFs...\n")

# Map text files to their original PDF locations
translated_dir = 'translated_pdfs'

# Mapping of text file patterns to original PDF paths
mappings = []

# Find all original PDFs to create the mapping
for root, dirs, files in os.walk('atom01_mechnaic'):
    for file in files:
        if file.endswith('.pdf') and not file.endswith('_ENG.pdf'):
            original_pdf_path = os.path.join(root, file)
            rel_path = os.path.relpath(original_pdf_path, 'atom01_mechnaic')
            
            # Create the text filename
            text_name = rel_path.replace('.pdf', '_translated.txt').replace('\\', '_').replace('/', '_')
            text_path = os.path.join(translated_dir, text_name)
            
            if os.path.exists(text_path):
                # Output path: same folder as original, name_ENG.pdf
                output_name = file.replace('.pdf', '_ENG.pdf')
                output_path = os.path.join(root, output_name)
                
                mappings.append((text_path, output_path, file))

print(f"Found {len(mappings)} PDFs to create\n")

processed = 0
failed = 0

for text_path, output_path, original_name in mappings:
    print(f"Processing: {original_name}")
    
    # Read translated text
    try:
        with open(text_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"  ✗ Error reading text file: {e}")
        failed += 1
        continue
    
    # Create PDF
    if create_pdf_from_text(content, output_path):
        output_name = os.path.basename(output_path)
        print(f"  ✓ Created: {output_name}")
        processed += 1
    else:
        failed += 1

print(f"\n{'='*60}")
print(f"PDF Creation Summary:")
print(f"  Total PDFs to create: {len(mappings)}")
print(f"  Successfully created: {processed}")
print(f"  Failed: {failed}")
print(f"{'='*60}")
