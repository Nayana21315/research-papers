import argparse

def main():
    parser = argparse.ArgumentParser(description="Fetch research papers from PubMed.")
    parser.add_argument("query", help="Search query for PubMed.")
    parser.add_argument("-f", "--file", help="Save results to a CSV file.")
    
    args = parser.parse_args()
    print(f"Fetching papers for query: {args.query}")

if __name__ == "__main__":
    main()
