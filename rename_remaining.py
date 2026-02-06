#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import shutil

# Define base path
base_path = r"c:\Users\phill\code\Atom01_hardware\atom01_mechnaic"

# Define all file renames across different directories
renames = {
    r"01_SW_Project\16x40十字轴承.SLDPRT": r"01_SW_Project\16x40_Cross_Bearing.SLDPRT",
    r"01_SW_Project\20cm脚.pdf": r"01_SW_Project\20cm_Foot.pdf",
    r"01_SW_Project\20cm脚.STEP": r"01_SW_Project\20cm_Foot.STEP",
    r"01_SW_Project\GB╱T 9163-2001[向心关节轴承（G系列）8].sldprt": r"01_SW_Project\GB_T_9163-2001[Radial_Spherical_Plain_Bearing_G_Series_8].sldprt",
    r"01_SW_Project\~$软胶 大腿根 左.SLDPRT": r"01_SW_Project\~$Soft_Rubber_Thigh_Root_Left.SLDPRT",
    r"01_SW_Project\手部（球型）.stp": r"01_SW_Project\Hand_Spherical.stp",
    r"01_SW_Project\比例尺1：2外围图.DWG": r"01_SW_Project\Scale_1-2_Perimeter_Drawing.DWG",
    r"01_SW_Project\肘部标定件，数量2.STEP": r"01_SW_Project\Elbow_Calibration_Part_Qty2.STEP",
    r"01_SW_Project\镜向GB╱T 9163-2001[向心关节轴承（G系列）8].SLDPRT": r"01_SW_Project\Mirrored_GB_T_9163-2001[Radial_Spherical_Plain_Bearing_G_Series_8].SLDPRT",
    
    # 02_Manufacturing directory
    r"02_Manufacturing\3D_Printing\脚踝标定，数量2.STEP": r"02_Manufacturing\3D_Printing\Ankle_Calibration_Qty2.STEP",
}

print("Starting file renaming...")
renamed = 0
errors = 0

for old_path, new_path in renames.items():
    old_full = os.path.join(base_path, old_path)
    new_full = os.path.join(base_path, new_path)
    
    if os.path.exists(old_full):
        try:
            os.rename(old_full, new_full)
            print(f"✓ Renamed: {old_path} -> {os.path.basename(new_path)}")
            renamed += 1
        except Exception as e:
            print(f"✗ Error renaming {old_path}: {e}")
            errors += 1
    else:
        print(f"⚠ Not found: {old_path}")

print(f"\n{'='*50}")
print(f"Summary:")
print(f"  Successfully renamed: {renamed}")
print(f"  Errors: {errors}")
print(f"{'='*50}")
