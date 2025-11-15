# Black History Month and Text Use of JET Magazine

This directory contains Scripts for performing NER (Named Entity Recognition) using spaCy with historical magazine text.  
 
The magazine and month are consecutive, so there's an opportunity to see any changes over time. In this instance, I am choosing February as the month and the years 1993 to 2004. I'm using Jet magazine for this analysis. I will be focusing on person names, locations, and dates. The goal is to track the frequency and context of these entities from 1993 to 2004. 


# Files
 - batch_ner_people.py (Extracts people; PERSON)
 - batch_ner_locations_dates.py (Extracts location; GPE or LOC)
 - pdfs_to_txt.py (Convert JET PDFs to txt files)
 - requirements.txt (Dependencies to run Scripts)
 - setup.py (setup script for Installation)
 - results (folder containing CSV files)

# Note:
If the reset script is run, you will have to reinstall these dependencies:

		pip install spacy
_________________________________________________________________________

		pip install pandas
_________________________________________________________________________

		pip install pdfminer.six


# How to Run Scripts: 

Open your VSCode Terminal 

Run the PDFs to TXT script (before NER), which will generate the .txt files seen in the repository and save them to a folder. 


# Create your virtual environment:

		python -m venv venv 
		source ner_env/bin/activate

# Install Requirements:

		pip install -r requirements(2).txt 


# Download spaCy English Model:

		python -m spacy download en_core_web_sm


# spaCy Models Used in Project and How to Install:

	- python -m spacy download en_core_web_sm 
	- python -m spacy download en_core_web_lg 


# Usage:

 # Basic Usage (Model Used for Project):

 # Activate your virtual environment 
		source ner_env/bin/activate 

 # Extract Locations and Dates 
		python batch_ner_locations_dates.py "JET txt files" --model en_core_web_sm

 # Extract People
		python batch_ner_people.py "JET txt files" --model en_core_web_lg


# Output


