import logging
import string
import nltk
import os
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

nltk_data_path = os.path.join(os.path.dirname(__file__), "nltk_data")
# nltk.download('punkt', download_dir=nltk_data_path)
# nltk.download('stopwords', download_dir=nltk_data_path)
# nltk.download('punkt_tab', download_dir=nltk_data_path)    
# nltk.download('wordnet', download_dir=nltk_data_path)    
# nltk.download('omw-1.4', download_dir=nltk_data_path) 
# nltk.download('averaged_perceptron_tagger_eng', download_dir=nltk_data_path)
nltk.data.path.append(nltk_data_path)


logger = logging.getLogger(__name__)

class TextCleaningProcessing:

    @staticmethod
    def to_lowercase(text:str):
        """Convert text to lowercase."""
        return text.lower()
    
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
        return " ".join([word for word in tokens if word not in stop_words])
    
    @staticmethod
    def Lemmatization(text:str):
        """ Perform lemmatization on the text."""
        lemmatizer = WordNetLemmatizer()
        tokens = word_tokenize(text)
        return " ".join([lemmatizer.lemmatize(word) for word in tokens])

    @staticmethod
    def full_processing(text:str):
        """ Perform full text processing."""
        text = TextCleaningProcessing.to_lowercase(text)
        text = TextCleaningProcessing.removing_punctuation_marks(text)
        text = TextCleaningProcessing.removing_unnecessary_whitespace(text)
        text = TextCleaningProcessing.removing_stop_words(text)
        text = TextCleaningProcessing.Lemmatization(text)
        return text




