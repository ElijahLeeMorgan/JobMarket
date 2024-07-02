import requests
from bs4 import BeautifulSoup
import json

# Session Initialization
session = requests.Session()
session.headers.update({'User-Agent': 'Mozilla/5.0'})


def fetch_details(url, limit=None):
    print(f"Sending request to URL: {url}")
    response = session.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    jobs_data = []
    job_list = soup.find_all('article', {'data-cy': 'serp-item'})
    print(f"Found {len(job_list)} job listings on this page.")

    for job in job_list:
        if limit and len(jobs_data) >= limit:
            break  # Stop if the limit is reached

        title_link = job.find('a', {'data-cy': 'job-link'})
        job_title = title_link['title'] if title_link and 'title' in title_link.attrs else 'Title not available'

        company_name = job.find('strong').get_text(strip=True) if job.find('strong') else 'Company not specified'

        # Initialize default values if not found
        contract_type = 'Contract type not available'
        workload = 'Workload not available'
        salary = 'Salary not specified'

        # Extract contract type, workload, and salary
        for p in job.find_all('p', class_='jZCxUn'):
            if '%' in p.text:
                workload = p.text.strip()
            elif 'CHF' in p.text or 'EUR' in p.text:
                salary = p.text.strip()
            else:
                contract_type = p.text.strip()

        job_info = {
            'title': job_title,
            'company': company_name,
            'contract_type': contract_type,
            'workload': workload,
            'salary': salary
        }

        if title_link:
            job_detail_url = 'https://www.jobs.ch' + title_link['href']
            job_response = session.get(job_detail_url)
            job_soup = BeautifulSoup(job_response.text, 'html.parser')

            # Extract job description
            description = job_soup.find('div', {'data-cy': 'vacancy-description'})
            job_info['description'] = description.text.strip() if description else 'Description not available'

        jobs_data.append(job_info)

    # Handle pages
    if not limit or len(jobs_data) < limit:
        next_page_link = soup.find('a', {'data-cy': 'paginator-next'})
        if next_page_link:
            next_page_url = 'https://www.jobs.ch' + next_page_link['href']
            print(f"Scraping next page: {next_page_url}")
            more_data = fetch_details(next_page_url, limit - len(jobs_data) if limit else None)
            jobs_data.extend(more_data)

    return jobs_data


# Starting URL for scraping
base_url = "https://www.jobs.ch/de/stellenangebote/?location=zürich&term="


''' uncomment to test on a few jobs
# Run the script with a limit for initial testing
test_job_details = fetch_details(base_url, limit=5)

# Save the results to a JSON file
with open('data/test_jobs_data.json', 'w', encoding='utf-8') as json_file:
    json.dump(test_job_details, json_file, ensure_ascii=False, indent=4)
print("Test scraping completed for 5 jobs.")
'''

# Uncomment the following lines to run the scaping without limits
all_job_details = fetch_details(base_url)
with open('data/all_jobs_data.json', 'w', encoding='utf-8') as json_file:
    json.dump(all_job_details, json_file, ensure_ascii=False, indent=4)
print("Full scraping completed.")
