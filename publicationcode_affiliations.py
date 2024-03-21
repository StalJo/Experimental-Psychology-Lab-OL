# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 21:13:44 2024

@author: Stalter
"""

from Bio import Entrez
import collections
import csv
import time

Entrez.email = "ENTER YOUR EMAIL"  

def search_pubmed(search_term):
    handle = Entrez.esearch(db="pubmed", term=search_term, retmax=10000)
    record = Entrez.read(handle)
    handle.close()
    print(f"Found {record['Count']} articles for term '{search_term}'.")
    return record["IdList"]

def get_author_details(pubmed_ids, max_retries=3, retry_delay=5):
    author_details = collections.defaultdict(lambda: {'count': 0, 'affiliations': set()})
    
    for i, pubmed_id in enumerate(pubmed_ids, start=1):
        success = False
        for attempt in range(max_retries):
            try:
                handle = Entrez.efetch(db="pubmed", id=pubmed_id, retmode="xml")
                articles = Entrez.read(handle)
                handle.close()
                for article in articles['PubmedArticle']:
                    article_affiliations = set()
                    if 'MedlineCitation' in article and 'Article' in article['MedlineCitation']:
                        article_data = article['MedlineCitation']['Article']
                        if 'AuthorList' in article_data:
                            for author in article_data['AuthorList']:
                                if 'AffiliationInfo' in author:
                                    for affiliation in author['AffiliationInfo']:
                                        if 'Affiliation' in affiliation:
                                            article_affiliations.add(affiliation['Affiliation'])
                    # Update each author's record with the set of affiliations from this article
                    for author in article_data.get('AuthorList', []):
                        if 'LastName' in author and 'ForeName' in author:
                            author_name = f"{author['ForeName']} {author['LastName']}"
                            author_details[author_name]['count'] += 1
                            author_details[author_name]['affiliations'] |= article_affiliations
                print(f"Processed {i} / {len(pubmed_ids)} articles.")
                success = True
                break
            except Exception as e:
                print(f"Error processing ID {pubmed_id}: {e}. Attempt {attempt + 1} of {max_retries}. Retrying in {retry_delay} seconds...")
                time.sleep(retry_delay)
        
        if not success:
            print(f"Failed to process article {pubmed_id} after {max_retries} attempts.")
    
    return author_details

def save_authors_to_csv(author_details, filename):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Author', 'Publication Count', 'Affiliations'])
        for author, details in author_details.items():
            affiliations = "; ".join(details['affiliations']) if details['affiliations'] else "No Affiliation Data"
            writer.writerow([author, details['count'], affiliations])
    print(f"Saved list of authors to '{filename}'.")

def list_authors_and_affiliations(search_term, filename):
    pubmed_ids = search_pubmed(search_term)
    author_details = get_author_details(pubmed_ids)
    sorted_authors = sorted(author_details.items(), key=lambda x: x[1]['count'], reverse=True)
    print(f"Authors sorted by publication count for '{search_term}':")
    for author, details in sorted_authors:
        print(f"{author}: {details['count']} publications")
    save_authors_to_csv(author_details, filename + '.csv')

# Example usage
search_term = 'ENTER SEARCH TERM'
filename = 'ENTER FILENAME'
list_authors_and_affiliations(search_term, filename)
