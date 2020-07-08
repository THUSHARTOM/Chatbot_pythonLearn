import re
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import WordNetLemmatizer
from part_of_speech import get_part_of_speech

lemmatizer = WordNetLemmatizer()

oprah_wiki = '<p>Working in local media, she was both the youngest news anchor and the first black female news anchor at Nashville\'s WLAC-TV. </p>'

oprah_wiki_clean = re.sub(r'<.?p>?' , "", oprah_wiki)
oprah_wiki_clean_period = re.sub(r'\.', "", oprah_wiki_clean)

oprah_lower = oprah_wiki_clean_period.lower()
tokenize_oprah = word_tokenize(oprah_lower)

lemmatized_pos = [lemmatizer.lemmatize(token, get_part_of_speech(token)) for token in tokenize_oprah]

print(lemmatized_pos)