import spacy
from spacy import displacy


def split_to_sentences(doc):
    sentences = list(doc.sents)
    # for sentence in sentences:
    #     print(sentence.text)
    return sentences


question_keywords = ["what", "why", "who", "where", "how", "when"]


def is_a_question(sentence):
    if sentence.text[-1] == "?":
        return True
    else:
        return False


def tokenize_spacy(sentence):
    pass
    # Load the English language model
    nlp = spacy.load("en_core_web_sm")

    # Process the input sentence with spaCy
    doc = nlp(sentence)

    sentences = split_to_sentences(doc)
    for sentence in sentences:
        print(sentence.text, "is a question?", is_a_question(sentence))

    # Extract the tokens from the processed document
    tokens = [f"TEXT: {token.text} PART-OF-SPEECH: {token.pos_} LEMMA: {token.lemma_} DEPENDENCY: {token.dep_}" for token in doc]

    for entity in doc.ents:
        print(entity.text, entity.label_)

    # Print the output tokens
    print('\n'.join(tokens))

    displacy.serve(doc, style="dep", port=3000)

    return tokens


# # Example input sentence
sentence = "The quick brown foxes jumped over the lazy dogs."
# sentence = "The cat is sitting with the bats on the striped mat under many badly flying gooses."
# sentence = "I live in New York City, and I am working for Google."
sentence = "Hi, can you help me with my math homework? " \
           "What is the result of 2 plus 2"
tokenize_spacy(sentence)