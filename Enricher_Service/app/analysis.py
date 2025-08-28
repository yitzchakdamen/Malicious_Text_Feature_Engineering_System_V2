from nltk.sentiment.vader import SentimentIntensityAnalyzer
from Text_cleaned_and_processed.Text_cleaned_and_processed import TextCleaningProcessing
import os
from dateutil.parser import parse
from datetime import datetime
import re
import logging

logger = logging.getLogger(__name__)

class Analysis:

    @staticmethod
    def latest_timestamp(text:str) -> str:
        """Find the latest timestamp in a given text."""
        matches = re.findall(r"\b\d{4}-\d{2}-\d{2}\b", text)
        logger.debug(f"Found timestamps: {matches} for text: {text}")
        if matches: return max([datetime.strptime(m, "%Y-%m-%d") for m in matches]).strftime("%Y-%m-%d")
        else: return ""

    @staticmethod
    def analyze_sentiment(text: str) -> float:
        """Analyze the sentiment of a tweet."""
        logger.debug(f"Analyzing sentiment for tweet: {text}")
        return SentimentIntensityAnalyzer().polarity_scores(text)["compound"]
    
    @staticmethod
    def sentiment_category(num:float) -> str:
        """Categorize the sentiment score."""
        if num >= 0.5: return "Positive"
        elif num <= -0.5: return "Negative"
        else: return "Neutral"


    @staticmethod
    def get_list_of_weapons(file_url: str) -> list[str]:
        """Get a list of weapons from a file."""
        with open(file_url, "r", encoding="utf-8") as f:
            file_content = f.read()
        logger.debug(f"Reading weapons from file: {file_content[:50]}...") 
        processed_content = TextCleaningProcessing.full_processing(file_content)
        return processed_content.split("\n")

    @staticmethod
    def weapons_detected(text: str) -> list[str]:
        """Detect weapons mentioned in the text."""
        file_url = os.getenv( "file_url" ,"Enricher_Service/app/data/weapon_list.txt")
        return [weapon for weapon in Analysis.get_list_of_weapons(file_url) if weapon in text.split()]