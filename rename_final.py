#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

base_path = r"c:\Users\phill\code\Atom01_hardware\atom01_mechnaic"

# Final batch of renames
renames = {
    r"02_Manufacturing\3D_Printing\膝盖标定，数量2.STEP": r"02_Manufacturing\3D_Printing\Knee_Calibration_Qty2.STEP",
    r"02_Manufacturing\3D_Printing\肩部固定件，数量2.STEP": r"02_Manufacturing\3D_Printing\Shoulder_Mounting_Part_Qty2.STEP",
    r"02_Manufacturing\CNC_Machining\IMU载板.STEP": r"02_Manufacturing\CNC_Machining\IMU_Carrier_Board.STEP",
    r"02_Manufacturing\CNC_Machining\IMU载板.pdf": r"02_Manufacturing\CNC_Machining\IMU_Carrier_Board.pdf",
    r"01_SW_Project\01_Calibration_Parts\肩部固定件，数量2.STEP": r"01_SW_Project\01_Calibration_Parts\Shoulder_Mounting_Part_Qty2.STEP",
    r"01_SW_Project\01_Calibration_Parts\膝盖标定，数量2.STEP": r"01_SW_Project\01_Calibration_Parts\Knee_Calibration_Qty2.STEP",
    r"01_SW_Project\Shell_Modified_Parts_1\外壳修改部件\腰部下册.stp": r"01_SW_Project\Shell_Modified_Parts_1\Shell_Modified_Parts\Waist_Lower_Part.stp",
    r"01_SW_Project\Shell_Modified_Parts_1\外壳修改部件\胸腔腹部.stp": r"01_SW_Project\Shell_Modified_Parts_1\Shell_Modified_Parts\Chest_Abdomen.stp",
    r"01_SW_Project\Shell_Modified_Parts_1\外壳修改部件\胸腔胸部.stp": r"01_SW_Project\Shell_Modified_Parts_1\Shell_Modified_Parts\Chest_Thorax.stp",
    r"01_SW_Project\Shell_Modified_Parts_1\外壳修改部件\胸腔肩部.stp": r"01_SW_Project\Shell_Modified_Parts_1\Shell_Modified_Parts\Chest_Shoulder.stp",
    r"01_SW_Project\Shell_Modified_Parts_1\外壳修改部件\胸腔后背下部.stp": r"01_SW_Project\Shell_Modified_Parts_1\Shell_Modified_Parts\Chest_Back_Lower.stp",
    r"01_SW_Project\Shell_Modified_Parts_1\外壳修改部件\大腿根部结构开孔.stp": r"01_SW_Project\Shell_Modified_Parts_1\Shell_Modified_Parts\Thigh_Root_Structure_Hole.stp",
    r"01_SW_Project\Rubber_Foot_Sole\橡胶脚底.SLDPRT": r"01_SW_Project\Rubber_Foot_Sole\Rubber_Foot_Sole.SLDPRT",
    r"01_SW_Project\Rubber_Foot_Sole\橡胶脚底.STEP": r"01_SW_Project\Rubber_Foot_Sole\Rubber_Foot_Sole.STEP",
}

print("Renaming final batch of Chinese files...")
renamed = 0
errors = 0

for old_path, new_path in renames.items():
    old_full = os.path.join(base_path, old_path)
    new_full = os.path.join(base_path, new_path)
    
    if os.path.exists(old_full):
        try:
            os.makedirs(os.path.dirname(new_full), exist_ok=True)
            os.rename(old_full, new_full)
            print(f"✓ {os.path.basename(new_path)}")
            renamed += 1
        except Exception as e:
            print(f"✗ Error: {e}")
            errors += 1
    else:
        print(f"⚠ Not found: {os.path.basename(old_path)}")

# Try to remove old Chinese directory if empty
try:
    old_dir = os.path.join(base_path, r"01_SW_Project\Shell_Modified_Parts_1\外壳修改部件")
    if os.path.exists(old_dir) and not os.listdir(old_dir):
        os.rmdir(old_dir)
        print("✓ Removed empty Chinese directory")
except:
    pass

print(f"\nRenamed: {renamed}, Errors: {errors}")
