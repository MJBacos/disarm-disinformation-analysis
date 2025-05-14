# Thailand State-Sponsored Disinformation Analysis via DISARM Framework

## 📂 Project Overview
This project focuses on processing and preparing public datasets of **state-sponsored disinformation campaigns** originating from **Thailand**. The data is structured to be compatible with the [DISARM Framework](https://disarm.foundation/) for behavior analysis and visualization.

The repository includes:
- Raw **Parquet** files
- **Scripts** for converting Parquet to CSV and CSV to DISARM-compatible JSON
- Final **JSON files** ready to load into the DISARM Navigator

---

## 🔗 Dataset Source
- Downloaded from [Zenodo: State-Sponsored Disinformation Campaigns](https://zenodo.org/records/14189193)
- Provided in **Parquet (.parquet)** format


## 🔄 Workflow
1. **Download raw Parquet files** from Zenodo.
2. **Use provided scripts** to:
   - Convert Parquet ➔ CSV
   - Convert CSV ➔ DISARM-compatible JSON
3. **Load JSON layers** into DISARM Navigator to map disinformation behaviors.


---

## 🧵 Why Parquet ➔ CSV ➔ JSON?
- **Parquet is optimized for analytics**, not for structured metadata use.
- **CSV enables easier inspection** and cleaning before metadata mapping.
- **JSON** aligns the data with the required DISARM Navigator format.

In short:
> **Parquet ➔ CSV ➔ JSON ensures accuracy, quality control, and usability for DISARM analysis.**


---

## 📁 Repo Structure
```bash
thailand-disarm-analysis/
├── original_parquets/      # Raw Parquet files
├── disarms_jsons/          # Converted JSON files
├── scripts/
│   ├── parquet_to_csv.py       # Script: Parquet to CSV conversion
│   └── csv_to_disarm_json.py   # Script: CSV to DISARM JSON conversion
├── LICENSE
└── README.md
└── analysis.md

---

## 💡 How to Use This Repo
1. **Clone the repository**
2. **(Optional)** Use scripts to rerun conversions if working with new data.
3. **Load JSON files** in [DISARM Navigator](https://disarm.foundation/navigator) to visualize the campaigns.

---

## 🌍 About DISARM Framework
The **DISARM Framework** offers an open method for describing and analyzing information operations. It enables standardized sharing and detection of disinformation tactics.

Learn more at [DISARM Foundation](https://disarm.foundation)
