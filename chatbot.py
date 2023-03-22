import spacy
from spacy import displacy

nlp = spacy.load("en_core_web_sm")


def split_to_sentences(doc):
    sentences = list(doc.sents)
    # for sentence in sentences:
    #     print(sentence.text)
    return sentences


question_keywords = ["what", "why", "who", "where", "how", "when"]

unwanted_words = ['the', '?', '\n', '(', ')', '.', '/']


def tokenize_spacy(sentence):
    # Load the English language model

    # Process the input sentence with spaCy
    doc = nlp(sentence)
    return doc


def create_dictionary_of_words(filename):
    dictionary = set()
    with open(filename, "r") as file1:
        all_lines = file1.readlines()

        for sentence in all_lines:
            tokens = tokenize_spacy(sentence)

            for word in tokens:
                if word.text not in unwanted_words:
                    dictionary.add(word.lemma_)

    with open("dictionary.txt", "w") as dictionary_file:
        dictionary_file.write('\n'.join(dictionary))

    return dictionary


def create_bag_of_words(sentence, dictionary):
    doc = nlp(sentence)
    words = [token.lemma_ for token in doc]
    bow = [0 for i in range(len(dictionary))]
    for word in words:
        # we need to find the index of our word in the dictionary
        index = dictionary.index(word)
        bow[index] += 1
        #if word == words[i]


my_text = "What is your name?"
dictionary = create_dictionary_of_words("all_words_example.txt")

bow = create_bag_of_words(my_text, dictionary)



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
