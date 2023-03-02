import spacy


def tokenize_spacy(sentence):
    # Load the English language model
    nlp = spacy.load("en_core_web_sm")

    # Process the input sentence with spaCy
    doc = nlp(sentence)

    # Extract the tokens from the processed document
    tokens = [f"{token.text} {token.pos_}" for token in doc]

    # Print the output tokens
    print(tokens)

    return tokens


# Example input sentence
sentence = "The quick brown fox jumps over the lazy dog."
tokenize_spacy(sentence)