thonimport json
from extractors.yc_parser import parse_yc_data
from outputs.exporters import export_to_json, export_to_csv

def main():
    # Example URL for scraping
    yc_url = "https://www.ycombinator.com/companies"
    
    # Fetch data from the URL
    company_data = parse_yc_data(yc_url)
    
    # Export the scraped data in JSON format
    export_to_json(company_data, 'output.json')
    # Optionally, export data in CSV format
    export_to_csv(company_data, 'output.csv')

if __name__ == "__main__":
    main()