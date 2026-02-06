import os
import fitz  # PyMuPDF

# Comprehensive translation dictionary
translations = {
    # Title block and document control
    '更改文件号': 'Change File No.',
    '主管设计': 'Design Supervisor',
    '设计': 'Design',
    '审核': 'Review',
    '校核': 'Check',
    '批准': 'Approval',
    '制图': 'Drawing',
    '描图': 'Drafting',
    '描校': 'Draft Check',
    '工艺': 'Process',
    '日期': 'Date',
    '年 月 日': 'Y M D',
    '年': 'Year',
    '月': 'Month',
    '日': 'Day',
    '签字': 'Signature',
    '签名': 'Signature',
    '共': 'Total',
    '张': 'Sheet',
    '件': 'Pcs',
    '第': 'No.',
    '页': 'Page',
    '图号': 'Drawing No.',
    '文件号': 'File No.',
    '版本': 'Version',
    '比例': 'Scale',
    '重量': 'Weight',
    '数量': 'Quantity',
    '图样标记': 'Drawing Mark',
    '阶段标记': 'Stage Mark',
    '阶 段 标 记': 'Stage Mark',
    '标记': 'Mark',
    '分区': 'Zone',
    '处数': 'Number',
    '代号': 'Code',
    '名称': 'Name',
    '材料': 'Material',
    '备注': 'Note',
    '替代': 'Replacement',
    
    # Materials
    '6061铝合金': '6061 Aluminum Alloy',
    '铝合金': 'Aluminum Alloy',
    '不锈钢': 'Stainless Steel',
    '碳钢': 'Carbon Steel',
    '塑料': 'Plastic',
    '橡胶': 'Rubber',
    '铜': 'Copper',
    '钢': 'Steel',
    '铝': 'Aluminum',
    
    # Assembly and parts
    '标定': 'Calibration',
    '说明': 'Instructions', 
    '教程': 'Tutorial',
    '开源版': 'Open Source',
    '组装': 'Assembly',
    '指南': 'Guide',
    '标准': 'Standard',
    '操作': 'Operation',
    '程序': 'Procedure',
    '总装': 'Main Assembly',
    '部件': 'Component',
    '零件': 'Part',
    '装配': 'Assembly',
    '子装配': 'Sub-assembly',
    
    # Robot body parts
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
    '关节': 'Joint',
    '连杆': 'Link',
    
    # Directions and positions
    '左': 'Left',
    '右': 'Right',
    '前': 'Front',
    '后': 'Rear',
    '上': 'Upper',
    '下': 'Lower',
    '内': 'Inner',
    '外': 'Outer',
    '侧': 'Side',
    '中': 'Middle',
    '底': 'Bottom',
    '顶': 'Top',
    
    # Components
    '电机': 'Motor',
    '电池': 'Battery',
    '螺丝': 'Screw',
    '螺钉': 'Screw',
    '螺母': 'Nut',
    '垫圈': 'Washer',
    '轴承': 'Bearing',
    '连接件': 'Connector',
    '夹板': 'Clamp Plate',
    '固定': 'Mounting',
    '载板': 'Carrier Board',
    '软胶': 'Soft Rubber',
    '支架': 'Bracket',
    '盖板': 'Cover Plate',
    '底板': 'Base Plate',
    '法兰': 'Flange',
    '轴': 'Shaft',
    '销': 'Pin',
    '限位': 'Limit',
    '锁紧': 'Lock',
    '输出': 'Output',
    '万向': 'Universal',
    '扩孔': 'Enlarged Hole',
    
    # Technical terms
    '尺寸': 'Dimension',
    '公差': 'Tolerance',
    '粗糙度': 'Roughness',
    '表面处理': 'Surface Treatment',
    '热处理': 'Heat Treatment',
    '硬度': 'Hardness',
    '强度': 'Strength',
    '精度': 'Precision',
    '加工': 'Machining',
    '工艺': 'Process',
    '检验': 'Inspection',
    '测试': 'Test',
    '完全贯穿': 'Through Hole',
    '贯穿': 'Through',
    
    # Drawing and view terms
    '图纸': 'Drawing',
    '工程图视图': 'View',
    '工程图': 'Engineering Drawing',
    '视图': 'View',
    '剖视图': 'Section View',
    '详图': 'Detail',
    '局部视图': 'Partial View',
    '俯视图': 'Top View',
    '正视图': 'Front View',
    '侧视图': 'Side View',
    
    # Instructions
    '注意': 'Note',
    '警告': 'Warning',
    '步骤': 'Step',
    '说明书': 'Manual',
    '教程': 'Tutorial',
    '指导': 'Guide',
    '要求': 'Requirement',
    '规格': 'Specification',
    '参数': 'Parameter',
    
    # Units and measurements
    '毫米': 'mm',
    '厘米': 'cm',
    '米': 'm',
    '克': 'g',
    '千克': 'kg',
    '度': 'degree',
    '角度': 'Angle',
    
    # Actions
    '安装': 'Install',
    '拆卸': 'Disassemble',
    '调整': 'Adjust',
    '校准': 'Calibrate',
    '测量': 'Measure',
    '检查': 'Check',
    '维护': 'Maintain',
    '修理': 'Repair',
    '更换': 'Replace',
    '清洁': 'Clean',
}

def translate_text(text):
    """Translate text using dictionary"""
    if not text:
        return text
    translated = text
    for chinese, english in translations.items():
        translated = translated.replace(chinese, english)
    return translated

def has_chinese(text):
    """Check if text contains Chinese characters"""
    if not text:
        return False
    return any('\u4e00' <= char <= '\u9fff' for char in text)

def translate_pdf_with_positioning(input_path, output_path):
    """
    Translate PDF by:
    1. Opening the original PDF
    2. For each text block, if it contains Chinese, translate it
    3. Cover the original text with white rectangle
    4. Draw the translated text at the same position
    5. Translate bookmarks/table of contents
    """
    try:
        doc = fitz.open(input_path)
        
        translations_made = 0
        
        for page_num in range(len(doc)):
            page = doc[page_num]
            
            # Get all text instances with their positions
            text_instances = page.get_text("dict")["blocks"]
            
            # Process text blocks in reverse order to avoid position shifts
            for block in text_instances:
                if block["type"] == 0:  # Text block
                    for line in block.get("lines", []):
                        for span in line.get("spans", []):
                            original_text = span["text"]
                            
                            if has_chinese(original_text):
                                translated = translate_text(original_text)
                                
                                if translated != original_text:
                                    # Get text position
                                    bbox = span["bbox"]
                                    font_size = span["size"]
                                    font_name = span["font"]
                                    
                                    # Cover original text with white rectangle
                                    rect = fitz.Rect(bbox)
                                    page.draw_rect(rect, color=(1, 1, 1), fill=(1, 1, 1))
                                    
                                    # Insert translated text at same position
                                    # Use a standard font since we may not have the original
                                    try:
                                        page.insert_text(
                                            (bbox[0], bbox[3]),  # Bottom-left of text
                                            translated,
                                            fontsize=font_size,
                                            color=(0, 0, 0),
                                            fontname="helv"  # Helvetica
                                        )
                                        translations_made += 1
                                    except:
                                        # If insertion fails, try with default parameters
                                        page.insert_text(
                                            (bbox[0], bbox[3]),
                                            translated,
                                            fontsize=font_size * 0.9,  # Slightly smaller
                                            color=(0, 0, 0)
                                        )
                                        translations_made += 1
        
        # Translate bookmarks/outlines (table of contents)
        toc = doc.get_toc()
        if toc:
            translated_toc = []
            for entry in toc:
                level, title, page_num = entry
                if has_chinese(title):
                    translated_title = translate_text(title)
                    translated_toc.append([level, translated_title, page_num])
                    translations_made += 1
                else:
                    translated_toc.append(entry)
            
            # Set the translated table of contents
            doc.set_toc(translated_toc)
        
        # Save the modified PDF
        doc.save(output_path)
        doc.close()
        
        return True, translations_made
        
    except Exception as e:
        return False, str(e)

# Find all PDFs
pdf_files = []
for root, dirs, files in os.walk('atom01_mechnaic'):
    for file in files:
        if file.endswith('.pdf') and not file.endswith('_ENG.pdf'):
            pdf_files.append(os.path.join(root, file))

print(f"Found {len(pdf_files)} PDF files to translate\n")

processed = 0
failed = 0
total_translations = 0

for pdf_path in pdf_files:
    filename = os.path.basename(pdf_path)
    dirname = os.path.dirname(pdf_path)
    
    output_name = filename.replace('.pdf', '_ENG.pdf')
    output_path = os.path.join(dirname, output_name)
    
    print(f"Processing: {filename}")
    
    success, result = translate_pdf_with_positioning(pdf_path, output_path)
    
    if success:
        translations_made = result
        total_translations += translations_made
        print(f"  ✓ Created: {output_name}")
        print(f"     Translated {translations_made} text instances")
        processed += 1
    else:
        print(f"  ✗ Failed: {result}")
        failed += 1

print(f"\n{'='*70}")
print(f"Translation Summary:")
print(f"  Total PDFs: {len(pdf_files)}")
print(f"  Successfully processed: {processed}")
print(f"  Failed: {failed}")
print(f"  Total text translations: {total_translations}")
print(f"\n  Engineering drawings and visuals are preserved.")
print(f"  Chinese text has been replaced with English translations.")
print(f"{'='*70}")
