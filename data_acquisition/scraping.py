import requests
from bs4 import BeautifulSoup
import csv

def scrape_job_details(url):
    print("Sending request to URL:", url)
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for bad requests

    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all job listings
    job_listings = soup.find_all('article', {'data-cy': 'serp-item'})
    print(f"Found {len(job_listings)} job listings.")
    job_details = []

    for job in job_listings[:5]:  # Limit to the first 5 entries
        job_link = job.find('a', {'data-cy': 'job-link'})
        job_title = job_link['title'] if job_link and 'title' in job_link.attrs else 'Title not available'
        #location = job.find_all('p', class_='jZCxUn')[0].get_text(strip=True) if job.find_all('p', class_='jZCxUn') else 'Location not available'
        contract_type = job.find_all('p', class_='jZCxUn')[1].get_text(strip=True) if job.find_all('p', class_='jZCxUn') else 'Contract type not available'
        company_name = job.find('strong').get_text(strip=True) if job.find('strong') else 'Company not specified'

        details = {
            'title': job_title,
            #'location': location,
            'contract_type': contract_type,
            'company': company_name
        }

        job_details.append(details)

    if job_details:
        # Save to CSV file
        keys = job_details[0].keys()
        with open('job_details.csv', 'w', newline='', encoding='utf-8') as output_file:
            dict_writer = csv.DictWriter(output_file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(job_details)
        print("Data written to job_details.csv")
    else:
        print("No job details to write.")

# Example usage:
url = 'https://www.jobs.ch/de/stellenangebote/?region=7&term='  # Adjust the URL as necessary
scrape_job_details(url)
