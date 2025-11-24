import csv

# Path to LIAR dataset (TSV)
liar_path = "train.tsv"  # Change if your file is named differently
claims_path = "data/claims.csv"

# Read existing claims
with open(claims_path, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    existing_claims = {(row["text"], row["label"]) for row in reader}

# Read LIAR and append new claims
with open(liar_path, "r", encoding="utf-8") as infile, \
     open(claims_path, "a", newline='', encoding="utf-8") as outfile:
    reader = csv.DictReader(infile, delimiter='\t')
    writer = csv.writer(outfile)
    for row in reader:
        text = row["statement"]
        label = row["label"].capitalize()
        if label == "True":
            label = "Real"
        elif label == "False":
            label = "Fake"
        # Avoid duplicates
        if (text, label) not in existing_claims:
            writer.writerow([text, "", label])
            existing_claims.add((text, label))

print(f"Appended LIAR dataset claims to {claims_path}")