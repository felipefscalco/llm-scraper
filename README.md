# llm-scraper

This project was created to test the scraping of the Seek website. The main objectives of this project were:

1. **Job List Extraction**: Extract all job titles, unique page links, and the link to the next page from the Seek job listings.
2. **Job Details Extraction**: For every single job page, extract detailed job information, including:
   - Job URL
   - Job Title
   - Company Name
   - Location
   - Industry
   - Work Type
   - Salary
   - Posted Date
   - Description
   - Quick Apply URL
   - View All Jobs URL

## Tools and Libraries Used

This project utilized the `crawl4ai` library to perform web scraping and data extraction. Different LLM providers were tested for the extraction process, including:
- **Gemini**
- **DeepSeek**
- **ChatGPT**

## How It Works

- The project uses `crawl4ai`'s `AsyncWebCrawler` and `LLMExtractionStrategy` to define schemas and extraction strategies for scraping job listings and job details.
- Environment variables are used to securely store API keys for the LLM providers.
- The extracted data is processed and saved in JSON format for further analysis.

## Files in the Project

- **`scrape_job_list.py`**: Extracts job titles, unique page links, and next page links from the Seek job listings.
- **`scrape_job_page.py`**: Extracts detailed job information from individual job pages.
- **`read_next_page.py`**: Demonstrates navigation to the next page of job listings.
- **`litellm-test.py`**: Tests the integration with the `litellm` library.
- **`initial_test.py`**: A basic test script for scraping a single job page.

## Requirements

- Python 3.8+
- API keys for the LLM providers (Gemini, DeepSeek, ChatGPT)

## Setup

1. Clone the repository.
2. Create a `.env` file based on `.env.example` and add your API keys.
3. Execute the single files like `python3 scrape_job_list.py` to run the scraping process.
4. The extracted data will be in the output in JSON format.