from nltk.sentiment.vader import SentimentIntensityAnalyzer
from Text_cleaned_and_processed.Text_cleaned_and_processed import TextCleaningProcessing
import os


class Analysis:

    @staticmethod
    def latest_timestamp(word:str) -> str:
        """Find the latest timestamp in a given text."""
        return ""

    @staticmethod
    def analyze_sentiment(tweet: str) -> float:
        """Analyze the sentiment of a tweet."""
        return SentimentIntensityAnalyzer().polarity_scores(tweet)["compound"]
    
    @staticmethod
    def sentiment_category(num:float) -> str:
        """Categorize the sentiment score."""
        if num <= 0.5: return "Positive"
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