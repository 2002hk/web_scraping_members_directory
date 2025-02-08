## Web Scraping extracting members data from https://www.sfma.org.sg/member/members-directory
## Libraries used
- scrapy
- ipython
- virtualenv
## Project Structure
```bash
membersscraper/
│── venv/
│── memberscraper/               # Project module
│   ├── spiders/                # Spider definitions
│   │   ├── __init__.py
│   │   ├── memberspider.py        # Custom spider
│   ├── __init__.py
│   ├── items.py                # Define scraped data structure
│   ├── middlewares.py          # Custom middlewares
│   ├── pipelines.py            # Data processing pipelines
│   ├── settings.py             # Scrapy settings
│── scrapy.cfg                  # Scrapy configuration file
│── requirements.txt            # Dependencies
│── README.md                   # Project documentation
```
```bash
## to create virtual env
python -m venv venv
python venv\Scripts\activate
## to create project
scrapy startproject memberscraper
## go the spider folder
scrapy genspider memberspider '##paste webpage url'
## to activate scrapy shell
scrapy shell
```
- Extracted 442 members data successfully
  
