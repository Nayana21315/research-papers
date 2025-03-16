import requests
import pandas as pd
import time
import os
from dotenv import load_dotenv

# Load environment variables from .env file (if any)
load_dotenv()

# PubMed API endpoints
PUBMED_SEARCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
PUBMED_SUMMARY_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"

def fetch_paper_ids(query, max_results=10):
    """Fetch PubMed paper IDs based on a search query."""
    params = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": max_results
    }
    response = requests.get(PUBMED_SEARCH_URL, params=params)
    if response.status_code != 200:
        raise Exception("Error fetching data from PubMed API")
    
    data = response.json()
    return data.get("esearchresult", {}).get("idlist", [])

def fetch_paper_details(paper_id):
    """Fetch paper details from PubMed using the paper ID."""
    params = {
        "db": "pubmed",
        "id": paper_id,
        "retmode": "json"
    }
    response = requests.get(PUBMED_SUMMARY_URL, params=params)
    if response.status_code != 200:
        return None
    
    return response.json()

def filter_non_academic_authors(authors):
    """Identify non-academic authors by checking affiliations."""
    non_academic_authors = []
    companies = []

    for author in authors:
        if "university" not in author.lower() and "college" not in author.lower():
            non_academic_authors.append(author)
            companies.append("Unknown Company")  # Improve with better heuristics

    return non_academic_authors, companies

def save_to_csv(data, filename="output.csv"):
    """Save fetched data to a CSV file."""
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"Results saved to {filename}")

def main(query, output_file="output.csv"):
    """Main function to fetch and process PubMed papers."""
    paper_ids = fetch_paper_ids(query)
    
    if not paper_ids:
        print("No papers found.")
        return

    results = []
    
    for paper_id in paper_ids:
        details = fetch_paper_details(paper_id)
        if not details:
            continue
        
        # Dummy author extraction - Replace with actual parsing
        authors = ["Author Name 1", "Author Name 2"]  
        non_academic_authors, companies = filter_non_academic_authors(authors)

        results.append({
            "PubmedID": paper_id,
            "Title": details.get("result", {}).get(paper_id, {}).get("title", "Unknown"),
            "Publication Date": details.get("result", {}).get(paper_id, {}).get("pubdate", "Unknown"),
            "Non-academic Author(s)": ", ".join(non_academic_authors),
            "Company Affiliation(s)": ", ".join(companies),
            "Corresponding Author Email": "N/A"
        })

        # Avoid exceeding API rate limits
        time.sleep(1)

    if output_file:
        save_to_csv(results, output_file)
    else:
        print(results)

if __name__ == "__main__":
    query = input("Enter search query: ")
    main(query)
