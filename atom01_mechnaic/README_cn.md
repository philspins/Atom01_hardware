# ROBOTO

[English](./README.md) | **[🇨🇳 中文](./README_cn.md)**

![Hardware](https://img.shields.io/badge/Hardware-v1.0-blue)
![Docs](https://img.shields.io/badge/Guide-Beginner_Friendly-green)
![License](https://img.shields.io/badge/License-MIT-orange)

> **Project Introduction (项目简介):** This is an open-source bipedal robot project. This project is dedicated to lowering the assembly threshold by providing a comprehensive step-by-step assembly tutorial from mechanical structure to circuit connections.

---

## 📚 Core Documentation Navigation (核心文档导航)

We have prepared detailed PDF manuals for beginners. Please **read them in the following order**:

我们为初学者准备了详细的 PDF 手册，请**务必按照以下顺序阅读**：

| Order<br>顺序 | Document Name<br>文档名称 | Content Description<br>内容说明 | Location<br>存放位置 |
| :---: | :--- | :--- | :--- |
| 1️⃣ | **[Assembly Work Instructions<br>装配作业指导书](00_Docs/)** | Detailed robot manufacturing process<br>详细机器人的制造流程 | `00_Docs/` |
| 2️⃣ | **[Mechanical Assembly Guide<br>机械装配指导书](00_Docs/Assembly_Guide_v1.14.pdf)** | Detailed assembly steps for mechanical structure<br>机械结构的详细组装步骤 | `00_Docs/` |


---

## 🛠️ Assembly Roadmap (装配路线图)


### Phase 1: Preparation (第一阶段：准备工作)
- [ ] **Tool Preparation (工具准备):** 
- [ ] **Material Inventory (物料清点):** 
- [ ] **PCB Fabrication (PCB 打样):** 

### Phase 2: Mechanical Assembly (第二阶段：机械组装)
> See `Assembly_Guide_v1.14.pdf` for details (详见 `Assembly_Guide_v1.14.pdf`)
- [ ] **Leg Assembly (腿部总成):**
- [ ] **Arm Assembly (手臂总成):** 
- [ ] **Torso Integration (躯干集成):** 

### Phase 3: Electronics & Wiring (第三阶段：电子与接线)
> ⚠️ **Critical Warning (高能预警): Always check positive and negative terminals before powering on! (上电前务必测量正负极！)**
- [ ] **Power Board Installation (电源板安装):** 
- [ ] **Wire Routing (走线布局):** 
- [ ] **Communication Connections (通讯连接):** 


## 📂 Project File Structure (项目文件架构)

This repository adopts a modular structure with files organized as follows:

本仓库采用模块化结构，文件组织如下：
```text
├── 00_docs/                         # [Documentation/文档] Core manuals/核心说明书
│   ├── BOM_Mechanical.xlsx          # Procurement list/采购清单
│   ├── Assembly_Guide_v1.14.pdf     # Assembly tutorial/组装教程
│   └── Standard Operating Procedure.pdf # SOP standard operating procedures/SOP 标准作业书
│
├── 01_SW_Project/                   # [Source Files/源文件] Mechanical design project/机械设计工程
│   
├── 02_Manufacturing/                # [Manufacturing/制造] Production and fabrication files/生产加工文件
│   
└── 03_URDF/                         # [Simulation/仿真] Robot description files/机器人描述文件
    