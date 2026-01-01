name: Daily Conflict Scraper

on:
  schedule:
    - cron: '0 8 * * *' # Runs every day at 8:00 AM UTC
  workflow_dispatch:      # Allows you to click a button to run it manually

jobs:
  scrape-and-report:
    runs-on: ubuntu-latest
    permissions:          # Gives the bot permission to save files
      contents: write
    
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.9'

      - name: Install libraries
        run: pip install requests beautifulsoup4 pandas

      - name: Run Scraper
        run: python nigeria_news_bot.py 
        # Ensure your python script saves data to 'data.csv'

      - name: Commit and Push Data
        run: |
          git config --global user.name 'NewsBot'
          git config --global user.email 'bot@noreply.github.com'
          git add data.csv
          git commit -m "Daily news update" || exit 0
          git push
