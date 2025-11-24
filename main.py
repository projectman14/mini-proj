# main.py
import os, pandas as pd
from src.ocr import extract_text
from src.query_builder import build_query
from src.search_fetcher import fetch_top_urls
from src.extractor import extract_title_paragraphs
from src.features import word_similarity_ratio, levenshtein_ratio, ngram_false_count

CLAIMS_CSV = "data/claims.csv"    # create this with columns: id,text,image(optional),label
OUTPUT_CSV = "outputs/features.csv"

def process_claim(claim, image_path=None):
    text = claim
    # Only use OCR if image_path is a valid non-empty string
    if image_path and isinstance(image_path, str) and image_path.strip():
        text = extract_text(image_path)
    query = build_query(text)
    urls = fetch_top_urls(query)
    print(f"\n[CLAIM] {claim}\nNumber of URLs fetched: {len(urls)}")

    feat = {"word_sim":[], "ldr":[], "ngram":[]}  # simple aggregate
    for u in urls:
        title, paras = extract_title_paragraphs(u)
        print(f"\n[CLAIM] {claim}\n[SEARCHING URL] {u}")
        if not title: continue
        feat["word_sim"].append(word_similarity_ratio(query, title))
        feat["ldr"].append(levenshtein_ratio(query, title))
        feat["ngram"].append(ngram_false_count(title))
        for p in paras:
            feat["ldr"].append(levenshtein_ratio(query, p))
            feat["ngram"].append(ngram_false_count(p))
    return {
        "avg_word_sim": sum(feat["word_sim"])/max(1,len(feat["word_sim"])),
        "avg_ldr":      sum(feat["ldr"])/max(1,len(feat["ldr"])),
        "sum_ngram":    sum(feat["ngram"])
    }

# def process_claim(claim, image_path=None):
#     text = claim
#     # Only use OCR if image_path is a valid non-empty string
#     if image_path and isinstance(image_path, str) and image_path.strip():
#         text = extract_text(image_path)
#     query = build_query(text)
#     urls = fetch_top_urls(query)
#     print(f"\n[CLAIM] {claim}\nNumber of URLs fetched: {len(urls)}")

#     feat = {"word_sim":[], "ldr":[], "ngram":[]}  # simple aggregate
#     for u in urls:
#         print(f"\n[CLAIM] {claim}\n[SEARCHING URL] {u}")
#         title, _ = extract_title_paragraphs(u)  # Ignore paragraphs
#         if not title: continue
#         feat["word_sim"].append(word_similarity_ratio(query, title))
#         feat["ldr"].append(levenshtein_ratio(query, title))
#         feat["ngram"].append(ngram_false_count(title))
#         # Do NOT process paragraphs
#     return {
#         "avg_word_sim": sum(feat["word_sim"])/max(1,len(feat["word_sim"])),
#         "avg_ldr":      sum(feat["ldr"])/max(1,len(feat["ldr"])),
#         "sum_ngram":    sum(feat["ngram"])
#     }



def main():
    df = pd.read_csv(CLAIMS_CSV)
    rows = []
    for _, r in df.iterrows():
        features = process_claim(r["text"], r.get("image"))
        features["label"] = r["label"]
        rows.append(features)
    out = pd.DataFrame(rows)
    os.makedirs("outputs", exist_ok=True)
    out.to_csv(OUTPUT_CSV, index=False)
    print(f"Saved features to {OUTPUT_CSV}")

if __name__ == "__main__":
    main()
