import spacy
from biobert_embedding.embedding import BiobertEmbedding
from collections import Counter

# Load the SciSpacy 'en_ner_bc5cdr_md' model for disease and drug entities
def extract_entities_bc5cdr(file_path):
    nlp = spacy.load("en_ner_bc5cdr_md")
    diseases = []
    drugs = []

    # Read the text file
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()

    # Process the text to extract entities
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ == "DISEASE":
            diseases.append(ent.text)
        elif ent.label_ == "CHEMICAL":
            drugs.append(ent.text)

    return diseases, drugs

# Extract entities using BioBERT (assuming custom model for NER)
def extract_entities_biobert(file_path):
    biobert = BiobertEmbedding()
    diseases = []
    drugs = []

    # Read the text file
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()

    # Split the text into sentences (assuming BioBERT can handle per-sentence embeddings)
    sentences = text.split('.')
    for sentence in sentences:
        tokens = sentence.split()  # Tokenize by space
        embeddings = biobert.word_vector(tokens)

        # Assume custom NER model has been applied and we get BIO labels
        for token, embedding in zip(tokens, embeddings):
            label = embedding.label  # Replace this with your NER model prediction for the token
            if label == "DISEASE":
                diseases.append(token)
            elif label == "DRUG":
                drugs.append(token)

    return diseases, drugs

# Compare the results
def compare_entities(diseases_bc5cdr, drugs_bc5cdr, diseases_biobert, drugs_biobert):
    # Total entities detected
    print(f"Total diseases detected by en_ner_bc5cdr_md: {len(diseases_bc5cdr)}")
    print(f"Total drugs detected by en_ner_bc5cdr_md: {len(drugs_bc5cdr)}")

    print(f"Total diseases detected by BioBERT: {len(diseases_biobert)}")
    print(f"Total drugs detected by BioBERT: {len(drugs_biobert)}")

    # Convert lists to sets for easier comparison
    diseases_bc5cdr_set = set(diseases_bc5cdr)
    drugs_bc5cdr_set = set(drugs_bc5cdr)
    diseases_biobert_set = set(diseases_biobert)
    drugs_biobert_set = set(drugs_biobert)

    # Intersection and differences
    common_diseases = diseases_bc5cdr_set.intersection(diseases_biobert_set)
    common_drugs = drugs_bc5cdr_set.intersection(drugs_biobert_set)

    print(f"Common diseases detected by both models: {len(common_diseases)}")
    print(f"Common drugs detected by both models: {len(common_drugs)}")

    # Differences
    diff_diseases_bc5cdr = diseases_bc5cdr_set.difference(diseases_biobert_set)
    diff_drugs_bc5cdr = drugs_bc5cdr_set.difference(drugs_biobert_set)
    diff_diseases_biobert = diseases_biobert_set.difference(diseases_bc5cdr_set)
    diff_drugs_biobert = drugs_biobert_set.difference(drugs_bc5cdr_set)

    print(f"Diseases only detected by en_ner_bc5cdr_md: {len(diff_diseases_bc5cdr)}")
    print(f"Drugs only detected by en_ner_bc5cdr_md: {len(diff_drugs_bc5cdr)}")

    print(f"Diseases only detected by BioBERT: {len(diff_diseases_biobert)}")
    print(f"Drugs only detected by BioBERT: {len(diff_drugs_biobert)}")

    # Common word frequency
    diseases_common_counter = Counter(common_diseases)
    drugs_common_counter = Counter(common_drugs)
    
    print("\nMost common diseases:")
    for disease, count in diseases_common_counter.most_common(10):
        print(f"{disease}: {count}")

    print("\nMost common drugs:")
    for drug, count in drugs_common_counter.most_common(10):
        print(f"{drug}: {count}")

# Main function to extract and compare entities
def main(file_path):
    # Extract using en_ner_bc5cdr_md
    diseases_bc5cdr, drugs_bc5cdr = extract_entities_bc5cdr(file_path)

    # Extract using BioBERT
    diseases_biobert, drugs_biobert = extract_entities_biobert(file_path)

    # Compare entities
    compare_entities(diseases_bc5cdr, drugs_bc5cdr, diseases_biobert, drugs_biobert)

# Example usage:
# main('merged_data.txt')
