import os
import pandas as pd
from preprocess import preprocess_csv
from ocr_extractor import extract_ocr_text
from matcher import match_images_to_metadata
import shutil

# Paths
CSV_PATH = 'data/copyright_records.csv'
IMAGE_DIR = 'data/images'
OUTPUT_DIR = 'output'
OUTPUT_CSV_ALL = os.path.join(OUTPUT_DIR, 'all_matches.csv')
OUTPUT_CSV_FILTERED = os.path.join(OUTPUT_DIR, 'matched_results.csv')
OUTPUT_IMAGE_DIR = os.path.join(OUTPUT_DIR, 'matched_images')

def main():
    print("🔄 Loading and preprocessing CSV...")
    df = preprocess_csv(CSV_PATH)

    print("👁 Extracting OCR text from images...")
    ocr_results = extract_ocr_text(IMAGE_DIR)

    print("🤖 Matching OCR to metadata...")
    matches = match_images_to_metadata(ocr_results, df)
    print(f"📊 Found {len(matches)} total match candidates.")

    # Save all matches
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    df_all = pd.DataFrame(matches)
    df_all.to_csv(OUTPUT_CSV_ALL, index=False)
    print(f"✅ Saved all matches to: {OUTPUT_CSV_ALL}")

    # Select top 3 matches for sample output
    df_filtered = df_all.sort_values(by='match_score', ascending=False).head(3)
    df_filtered.to_csv(OUTPUT_CSV_FILTERED, index=False)
    print(f"✅ Saved top 3 matches to: {OUTPUT_CSV_FILTERED}")

    # Copy matched image files
    os.makedirs(OUTPUT_IMAGE_DIR, exist_ok=True)
    copied = 0
    for _, row in df_filtered.iterrows():
        image_name = row['image_file'].strip()
        src_path = os.path.join(IMAGE_DIR, image_name)
        dst_path = os.path.join(OUTPUT_IMAGE_DIR, image_name)
        if os.path.exists(src_path):
            shutil.copy(src_path, dst_path)
            copied += 1
        else:
            print(f"⚠️ Image not found: {src_path}")

    print(f"🖼 Copied {copied} matched images to: {OUTPUT_IMAGE_DIR}")
    print("🎉 Done!")

if __name__ == "__main__":
    main()
