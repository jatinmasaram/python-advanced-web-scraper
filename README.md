Advanced Python Web Scraper
Project Overview
This is a robust and modular web scraper built in Python to extract data from a multi-page website. The project is designed to demonstrate professional software development practices, including modular code organization, robust error handling, and responsible scraping.

The scraper targets the Quotes to Scrape website, navigating through all available pages to collect a comprehensive dataset of quotes.

Key Features
Modular Design: The project's code is separated into distinct files (scrape_logic.py, data_processor.py, and main.py) based on functionality. This approach makes the code clean, maintainable, and scalable.

Pagination: The scraper automatically navigates through all pages of the target website to ensure all available data is collected.

Robust Error Handling: The script is equipped to handle common issues like network errors (e.g., 404 Not Found) and missing HTML elements, ensuring the program does not crash and provides clear feedback.

Responsible Scraping: A randomized delay is incorporated between each request to prevent overloading the target server, demonstrating an understanding of ethical web scraping practices.

Data Export: The collected data is neatly formatted and exported to a .csv file for easy analysis and use.

Technologies Used
Python 3.x

requests: For making HTTP requests to the web server.

Beautiful Soup 4 (bs4): For parsing and navigating the HTML content.

Project Structure
.
├── scrape_logic.py         # Contains core scraping logic for a single page.
├── data_processor.py       # Handles saving the scraped data to a CSV file.
├── main.py                 # The main script that orchestrates the entire process.
├── requirements.txt        # Lists the necessary Python libraries.
└── README.md               # The project's README file.
How to Run
Clone the repository:

Bash

git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
Install the dependencies:

Bash

pip install -r requirements.txt
Run the main script:

Bash

python main.py
After the script completes, a new file named all_quotes_modular.csv will be created in the project directory, containing the scraped data.
