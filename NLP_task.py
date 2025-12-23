import spacy
from spacy.tokenizer import Tokenizer

nlp = spacy.load("en_core_web_sm")
tokenizer = Tokenizer(nlp.vocab)

def get_segment(some_text):
    sentence = []
    doc = nlp(some_text)
    for sent in doc.sents:
        sentence.append(sent.text)
    return sentence

def get_tokens(some_text):
    doc = tokenizer(some_text)
    return [token for token in doc]

def remove_stop_words(some_tokens):
    filtered_sentence =[]
    for word in some_tokens:
        if not word.is_stop:
            filtered_sentence.append(word.text)
    return filtered_sentence

def stemm_lemmatization(some_text):
    list_lemma = []
    for token in nlp(some_text):
        list_lemma.append(token.lemma_)
    return list_lemma

def part_of(doc):
    word_tags = {}
    for word in nlp(doc):
        word_tags[word.text] = word.pos_
    return word_tags

text = '''Natural Language Processing (NLP) is a part of AI (artificial intelligence) that deals with understanding and processing of human language.
In real time, majority of data exists in the unstructured form such us text, videos, images.
Mass of data in unstructured category, will be in textual form.
To process this textual data's with machine learning algorithms, NLP comes in to play.
NLP use cases are Language translation, Speech recognition, Hiring and Recruitment, Chat Bot, Sentimental analysis and so on.'''


sentences = get_segment(text)
print("*** Sentences: ***")
for s in sentences:
    print(s)

tokens = get_tokens(text)
print("\n*** Tokens: ***")
print(tokens)

text_minus_stop = remove_stop_words(tokens)
print("\n*** Tokens after removing stop words: ***")
for word in text_minus_stop:
    print(word)


text_after_lemma = stemm_lemmatization(text)
print("\n*** Tokens after lemmatization: ***")
for word in text_after_lemma:
    print(word)

part_speech = part_of(text)
print('\n*** Parts of Speech ***')
print(part_speech)