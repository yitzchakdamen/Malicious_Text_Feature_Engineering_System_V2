from nltk.sentiment.vader import SentimentIntensityAnalyzer
from Text_cleaned_and_processed.Text_cleaned_and_processed import TextCleaningProcessing
import os
from dateutil.parser import parse
from datetime import datetime

class Analysis:

    @staticmethod
    def is_date(string, fuzzy=False):
        """ Return whether the string can be interpreted as a date."""
        try: 
            parse(string, fuzzy=fuzzy)
            return True
        except ValueError:
            return False
    
    @staticmethod
    def latest_timestamp(text:str) -> str:
        """Find the latest timestamp in a given text."""
        dates = [datetime.strptime(word, '%Y-%m-%d') for word in text.split() if Analysis.is_date(word)]
        return max(dates).strftime('%Y-%m-%d') if dates else ""

    @staticmethod
    def analyze_sentiment(tweet: str) -> float:
        """Analyze the sentiment of a tweet."""
        return SentimentIntensityAnalyzer().polarity_scores(tweet)["compound"]
    
    @staticmethod
    def sentiment_category(num:float) -> str:
        """Categorize the sentiment score."""
        if num >= 0.5: return "Positive"
        elif num < 0.5 and num > -0.5: return "Neutral"
        else: return "Negative"

    @staticmethod
    def get_list_of_weapons(file_url: str) -> list[str]:
        """Get a list of weapons from a file."""
        with open(file_url, "r", encoding="utf-8") as f:
            file_content = f.read()
        processed_content = TextCleaningProcessing.full_processing(file_content)
        return processed_content.split("\n")

    @staticmethod
    def weapons_detected(text: str) -> list[str]:
        file_url = os.getenv( "file_url" ,"Enricher_Service/app/weapon_list.txt")
        """Detect weapons mentioned in the text."""
        return [weapon for weapon in Analysis.get_list_of_weapons(file_url) if weapon in text.split(" ")]