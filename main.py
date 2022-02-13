import matplotlib.pyplot as plt
import math

def open_file(file_name):
    # dictionaries
    dict_word_paragrah = {}


    # vars
    num_paragraph = 0
    num_word_sentence = 0
    num_sentence = 0

    # LISTS
    end_sentence = ['.', '!', '?']
    special_names = ['Mr.', 'Ms.', 'Mrs.']
    list_word_sentence = []
    list_sentence_paragraph = []

    with open(file_name) as file:
        for row in file:

            row = row.split()
            row_len = len(row)

            if row_len >= 1:
                # EACH CHAPTER
                if row[0].lower() == 'chapter':
                    pass

                # CALCULATE NUMBER OF SENTENCES AND SENTENCE LENGTHS
                else:
                    for word in row:
                        word_len = len(word)
                        if word[-1] in end_sentence:
                            # if word_len <= 4 and word in special_names:
                            #         pass
                            # elif word >= 4:
                            num_sentence += 1
                            num_word_sentence += 1
                            list_word_sentence.append(num_word_sentence)
                            num_word_sentence = 0

                        else:
                            num_word_sentence += 1




            # Each paragraph
            else:
                num_paragraph += 1
                list_sentence_paragraph.append(num_sentence)
                list_sentence_paragraph = []
        print(list_word_sentence)






open_file('Jacob Kahn - Great_Expectations.txt')
# open_file('Jacob Kahn - Scarlet_Letter.txt')
