import logging
import string
import nltk
import os
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk_data_path = os.path.join(os.path.dirname(__file__), "nltk_data")
# nltk.download('punkt', download_dir=nltk_data_path)
# nltk.download('stopwords', download_dir=nltk_data_path)
# nltk.download('punkt_tab', download_dir=nltk_data_path)
nltk.data.path.append(nltk_data_path)


logger = logging.getLogger(__name__)

class TextCleaningProcessing:
    
    class Cleaning:
        
        @staticmethod
        def removing_punctuation_marks(text:str):
            """Remove punctuation marks from the text."""
            translator = str.maketrans('', '', string.punctuation)
            return text.translate(translator)
        
        @staticmethod
        def removing_unnecessary_whitespace(text:str):
            """ Remove unnecessary whitespace (tabs, long spaces, line breaks) from the text."""
            return " ".join(text.split())
        
        @staticmethod
        def removing_stop_words(text:str):
            """ Remove stop words from the text."""
            stop_words = set(stopwords.words('english'))
            tokens = word_tokenize(text.lower())
            return " ".join([w for w in tokens if w not in stop_words])



    class Processing:
        pass
    
    



