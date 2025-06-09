###Project Title:

**Scalable Matching of Copyright Registration Images Using AI and OCR**

---

### Objective

This project demonstrates a **scalable, AI-assisted method** to retrieve and match copyright registration images based on metadata from a spreadsheet. The system uses **optical character recognition (OCR)** and **fuzzy matching** to link scanned images (e.g., `.webp` files) to corresponding registration entries.

---

### 📂 Folder Structure

```
copyright-image-marker/
├── data/
│   ├── images/                 ← input image files (.webp)
│   └── copyright_records.csv   ← input CSV with metadata
├── output/
│   ├── matched_results.csv     ← top 3 high-score matches
│   ├── all_matches.csv         ← full list of OCR/fuzzy results
│   └── matched_images/         ← copied image files for submission
├── src/
│   ├── preprocess.py
│   ├── ocr_extractor.py
│   ├── matcher.py
│   └── main.py
├── requirements.txt
└── README.md                   ← this file
```

---

### Method Summary

1. **Preprocessing**:

   * Extracted and cleaned fields like `Registration Number`, `Title`, and `Claimant` from the CSV.

2. **OCR Extraction**:

   * Used `pytesseract` to extract text from `.webp` images.

3. **AI-based Matching**:

   * Compared OCR text to CSV rows using:

     * Normalized registration numbers
     * Fuzzy matching on title and claimant

4. **Filtering and Output**:

   * Saved all results to `all_matches.csv`
   * Extracted top 3 matches to `matched_results.csv`
   * Copied matched image files to `output/matched_images/`

---

### Technologies Used

* Python 3
* `pytesseract` for OCR
* `Pillow` for image handling
* `RapidFuzz` for fuzzy string matching
* `pandas` for data processing

---

###  Note on Matching

> While the system successfully extracted and scored image text, the images and CSV used in this demo came from different sources.
> As a result, **no true registration number matches** were found.
> However, the pipeline works correctly and is easily re-runnable on matched datasets.

---

### How to Run

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Place your `.webp` images in `data/images/`
   Place your metadata spreadsheet in `data/copyright_records.csv`

3. Run the pipeline:

   ```bash
   python src/main.py
   ```

---

### Sample Output

Found in `output/matched_results.csv` and `output/matched_images/`
These demonstrate successful image text extraction and ranked match confidence.

---

### 📬 Contact

Developed by: *\[Your Name]*
For: *\[Assignment or Institution Name]*
Date: *June 2025*

---

