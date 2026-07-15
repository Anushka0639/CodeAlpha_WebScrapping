import requests
from bs4 import BeautifulSoup
import pandas as pd

# Target Website
url = "https://realpython.github.io/fake-jobs/"

# Send Request
response = requests.get(url)

# Parse HTML
soup = BeautifulSoup(response.content, "html.parser")

# Store Data
job_titles = []
companies = []
locations = []

# Extract Job Information
jobs = soup.find_all("div", class_="card-content")

for job in jobs:
    title = job.find("h2", class_="title").text.strip()
    company = job.find("h3", class_="company").text.strip()
    location = job.find("p", class_="location").text.strip()

    job_titles.append(title)
    companies.append(company)
    locations.append(location)

# Create Dataset
df = pd.DataFrame({
    "Job Title": job_titles,
    "Company": companies,
    "Location": locations
})

# Save Dataset
df.to_csv("job_dataset.csv", index=False)

# Display First 10 Records
print("\nFirst 10 Job Listings:\n")
print(df.head(10))

print("\nDataset successfully saved as 'job_dataset.csv'")