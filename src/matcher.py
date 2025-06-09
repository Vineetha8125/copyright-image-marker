from rapidfuzz import fuzz

def normalize_reg_num(s):
    if not isinstance(s, str):
        return ""
    return ''.join(filter(str.isdigit, s))

def match_images_to_metadata(ocr_results, metadata_df, threshold=50):
    matched = []

    for result in ocr_results:
        best_match = None
        best_score = 0
        match_type = "none"

        for _, row in metadata_df.iterrows():
            reg_csv = normalize_reg_num(row['Registration Number'])
            reg_text = normalize_reg_num(result['ocr_text'])

            # High-confidence match if registration number matches
            if reg_csv and reg_csv in reg_text:
                avg_score = 100
                current_match_type = "reg_number"
            else:
                score_title = fuzz.partial_ratio(result['ocr_text'], row['Clean Title'])
                score_claimant = fuzz.partial_ratio(result['ocr_text'], row['Clean Claimant'])
                avg_score = (score_title + score_claimant) / 2
                current_match_type = "fuzzy"

            if avg_score > best_score and avg_score >= threshold:
                best_score = avg_score
                best_match = row
                match_type = current_match_type

        if best_match is not None:
            matched.append({
                'image_file': result['image_file'],
                'registration_number': best_match['Registration Number'] if match_type == "reg_number" else "",
                'title': best_match['Title'],
                'match_score': round(best_score, 2),
                'match_type': match_type
            })

    return matched
