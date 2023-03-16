import spacy
from spacy import displacy

dictionary = set()


def split_to_sentences(doc):
    sentences = list(doc.sents)
    # for sentence in sentences:
    #     print(sentence.text)
    return sentences


question_keywords = ["what", "why", "who", "where", "how", "when"]

unwanted_words = ['the', '?', '\n', '(', ')', '.', '/']

def create_dictionary_of_words(filename):
    with open(filename, "r") as file1:
        all_lines = file1.readlines()

        for sentence in all_lines:
            tokens = tokenize_spacy(sentence)

            for word in tokens:
                if word.text not in unwanted_words:
                    dictionary.add(word.lemma_)

    with open("dictionary.txt", "w") as dictionary_file:
        dictionary_file.write('\n'.join(dictionary))



def tokenize_spacy(sentence):

    # Load the English language model
    nlp = spacy.load("en_core_web_sm")

    # Process the input sentence with spaCy
    doc = nlp(sentence)

    # sentences = split_to_sentences(doc)
    # for sentence in sentences:
    #     print(sentence.text, "is a question?", is_a_question(sentence))

    # Extract the tokens from the processed document
    # tokens = [f"TEXT: {token.text} PART-OF-SPEECH: {token.pos_} LEMMA: {token.lemma_} DEPENDENCY: {token.dep_}" for token in doc]

    tokens = [token for token in doc]  # list comprehension
    # for entity in doc.ents:
    #     print(entity.text, entity.label_)

    # # Print the output tokens
    # print('\n'.join(tokens))
    #
    # displacy.serve(doc, style="dep", port=3000)

    return tokens


create_dictionary_of_words("all_words_example.txt")

my_text = "What is your name?"

def create_bag_of_words(sentence):
    pass



# def is_a_question(sentence):
#     if sentence.text[-1] == "?":
#         return True
#     else:
#         return False




# # # Example input sentence
# sentence = "The quick brown foxes jumped over the lazy dogs."
# # sentence = "The cat is sitting with the bats on the striped mat under many badly flying gooses."
# # sentence = "I live in New York City, and I am working for Google."
# sentence = "Hi, can you help me with my math homework? " \
#            "What is the result of 2 plus 2"
# tokenize_spacy(sentence)
