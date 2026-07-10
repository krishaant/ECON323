# ECON323 — Does Student Sentiment Move Professor Pay?

Final project for ECON323, tying together real-world datasets to see whether student sentiment shows up in how UBC professors are paid.

1. **RateMyProfessors reviews** — scraped student reviews for UBC professors (`scrapers/RMPscrapper.py` / `.r`, `RateMyProf_scrapper.ipynb`)
2. **UBC professor salaries** — pulled from UBC's public Statements of Financial Information, FY21–FY24 (`financial_info/`)
3. **Review sentiment** — each review scored positive / negative / neutral with a fine-tuned BERT model (`BERTEMOTIONS.ipynb`)

The scraped reviews and salary data are joined and run through a panel regression to see how professor pay relates to review sentiment over time.

## Layout

- `scrapers/` — RateMyProfessors scrapers (Python and R versions)
- `scraped_professor_urls.txt` — professor profile URLs collected for scraping
- `RateMyProf_scrapper.ipynb` — scraping + cleaning pipeline for reviews
- `Rate_My_Professors_Reviews.csv` — cleaned review dataset
- `BERTEMOTIONS.ipynb` — BERT sentiment scoring of reviews
- `financial_info/` — UBC professor salary data and source financial statements (FY21–FY24), plus the scraper used to pull them

## Note

This started as two separate repos (one for scraping/data, one for the sentiment analysis) — merged here into one project.
