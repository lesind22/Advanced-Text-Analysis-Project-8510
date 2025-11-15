#!/usr/bin/env python3
"""
Batch Named Entity Recognition (NER) Analysis using spaCy
Analyzes all .txt files in a folder to extract people (PERSON entities).
"""

import spacy
import pandas as pd
import argparse
import sys
from pathlib import Path

def load_spacy_model(model_name="en_core_web_sm"):
    try:
        nlp = spacy.load(model_name)
        print(f"✓ Loaded spaCy model: {model_name}")
        return nlp
    except OSError:
        print(f"❌ Error: spaCy model '{model_name}' not found.")
        print(f"Please install it with: python -m spacy download {model_name}")
        sys.exit(1)

def extract_person_entities(text, nlp):
    doc = nlp(text)
    entities = []
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            entities.append({
                'text': ent.text,
                'label': ent.label_,
                'filename': None  
            })
    return entities

def save_entities_to_csv(entities, output_file):
    if not entities:
        print("❌ No PERSON entities found to save.")
        return
    results_dir = Path("results")
    results_dir.mkdir(exist_ok=True)
    output_path = results_dir / output_file
    df = pd.DataFrame(entities)
    df = df[["filename", "label", "text"]]
    df.to_csv(output_path, index=False)
    print(f"💾 Saved {len(entities)} PERSON entities to: {output_path}")

def process_folder(folder_path, nlp, max_chars=None):
    entities_all = []
    folder = Path(folder_path)
    for file_path in sorted(folder.glob("*.txt")):
        print(f"\n📖 Reading file: {file_path.name}")
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                text = f.read()
        except UnicodeDecodeError:
            with open(file_path, 'r', encoding='latin-1') as f:
                text = f.read()
        if max_chars and len(text) > max_chars:
            text = text[:max_chars]
            print(f"⚠️  Limited processing of {file_path.name} to first {max_chars} characters")
        entities = extract_person_entities(text, nlp)
        for ent in entities:
            ent['filename'] = file_path.name
        entities_all.extend(entities)
        print(f"🔍 Found {len(entities)} PERSON entities in {file_path.name}")
    return entities_all

def main():
    parser = argparse.ArgumentParser(description='Batch NER Analysis using spaCy for PERSON entities only')
    parser.add_argument('input_folder', help='Path to the folder containing .txt files')
    parser.add_argument('--model', default='en_core_web_sm', 
        help='spaCy model to use (default: en_core_web_sm)')
    parser.add_argument('--output', default='people_only_results', 
        help='Base name for output file (default: people_only_results.csv)')
    parser.add_argument('--max-chars', type=int, default=None,
        help='Maximum characters per file to process (optional)')
    args = parser.parse_args()

    folder_path = Path(args.input_folder)
    if not folder_path.exists() or not folder_path.is_dir():
        print(f"❌ Error: Input folder '{args.input_folder}' not found or is not a directory.")
        sys.exit(1)

    nlp = load_spacy_model(args.model)
    entities = process_folder(folder_path, nlp, max_chars=args.max_chars)

    if not entities:
        print("❌ No PERSON entities found in any file.")
        return

    print(f"\n📊 Found {len(entities)} PERSON entities across all files.")
    save_entities_to_csv(entities, f"{args.output}.csv")
    print(f"\n✅ Batch extraction complete! Results saved to: results/{args.output}.csv")

if __name__ == "__main__":
    main()