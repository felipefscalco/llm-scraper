import os
import asyncio
import json
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from typing import List
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode, LLMConfig
from crawl4ai.extraction_strategy import LLMExtractionStrategy

load_dotenv()

BASE_URL = "https://www.seek.com.au/job/83035215"

class Advertise(BaseModel):
    job_url: str
    job_title: str
    company: str
    location: str
    industry: str
    work_type: str
    salary: str
    posted_date: str
    description: str
    quick_apply_url: str
    view_all_jobs_url: str

async def main():
    # 1. Define the LLM extraction strategy
    llm_strategy = LLMExtractionStrategy(
        llm_config = LLMConfig(provider="gemini/gemini-2.0-flash-lite-preview-02-05", api_token=os.getenv('GEMINI_API_KEY')),
        schema=Advertise.model_json_schema(),
        extraction_type="schema",
        instruction="Extract all the job information, job url, job title, company name, location, industry, work type, salary, posted date, description, quick apply url and view all jobs url. ",
        chunk_token_threshold=1000,
        overlap_rate=0.0,
        apply_chunking=True,
        input_format="markdown",   # or "html", "fit_markdown"
        extra_args={"temperature": 0.0, "max_tokens": 800}
    )

    # 2. Build the crawler config
    crawl_config = CrawlerRunConfig(
        extraction_strategy=llm_strategy,
        cache_mode=CacheMode.BYPASS
    )

    # 3. Create a browser config if needed
    browser_cfg = BrowserConfig(headless=True)

    async with AsyncWebCrawler(config=browser_cfg) as crawler:
        # 4. Let's say we want to crawl a single page
        result = await crawler.arun(
            url=BASE_URL,
            config=crawl_config
        )

        if result.success:
            # 5. The extracted content is presumably JSON
            data = json.loads(result.extracted_content)
            print("Extracted items:", data)

            # 6. Show usage stats
            llm_strategy.show_usage()  # prints token usage
        else:
            print("Error:", result.error_message)

if __name__ == "__main__":
    asyncio.run(main())