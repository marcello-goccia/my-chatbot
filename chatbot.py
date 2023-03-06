import spacy


def tokenize_spacy(sentence):
    pass
    # Load the English language model
    nlp = spacy.load("en_core_web_sm")

    # Process the input sentence with spaCy
    doc = nlp(sentence)
    # this comment just added now!!

    # Extract the tokens from the processed document
    tokens = [f"{token.text} {token.pos_}" for token in doc]

    # Print the output tokens
    print(tokens)

    return tokens
#
#
# # Example input sentence
sentence = "The quick brown foxes jumped over the lazy dogs."
tokenize_spacy(sentence)