import matplotlib.pyplot as plt
import math

def open_file(file_name):
    # vars
    num_paragraph = 0
    num_word_sentence = 0
    num_sentence = 0
    num_word_paragraph = 0
    num_comma_sentence = 0

    # LISTS
    end_sentence = ['.', '!', '?']
    quotations = ['"']

    list_word_sentence = []
    list_sentence_paragraph = []
    list_word_paragraph = []
    list_comma_sentence = []

    with open(file_name) as file:
        for row in file:

            row = row.split()
            row_len = len(row)

            # CHECK IF NEW PARAGRAPH OR NOT
            if row_len >= 1:
                # EACH CHAPTER
                if row[0].lower() == 'chapter':
                    pass
                # CALCULATE NUMBER OF SENTENCES AND SENTENCE LENGTHS
                else:
                    for word in row:
                        num_word_paragraph += 1

                        word_len = len(word)
                        if word[-1] in end_sentence:
                            num_sentence += 1
                            num_word_sentence += 1

                            list_word_sentence.append(num_word_sentence)
                            num_word_sentence = 0

                            list_comma_sentence.append(num_comma_sentence)
                            num_comma_sentence = 0

                        elif word[-1] == ',':
                            num_comma_sentence += 1

                        else:
                            num_word_sentence += 1

            # Each paragraph
            else:
                num_paragraph += 1
                # print(num_sentence)
                list_sentence_paragraph.append(num_sentence)
                list_word_paragraph.append(num_word_paragraph)
                # print(f'{file_name}: {list_sentence_paragraph}')

                num_sentence = 0
                num_word_paragraph = 0

        return(list_sentence_paragraph, list_word_paragraph, list_word_sentence, list_comma_sentence)



def calculate_M_SD(filename, list):
    mean = 0
    standard_dev = 0
    difference_list = []

    mean = sum(list) / len(list)

    for number in list:
        difference_list.append((number - mean) ** 2)

    variance = sum(difference_list) / len(list)
    standard_dev = math.sqrt(variance)

    print(f'{filename} Mean: {mean}, SD: {standard_dev}')
    return(mean, standard_dev)





def main(filename):

    list_sentence_paragraph, list_word_paragraph, list_word_sentence, list_comma_sentence = open_file(filename)

    calculate_M_SD(filename, list_word_sentence)


main('Jacob Kahn - Great_Expectations.txt')
main('Jacob Kahn - Scarlet_Letter.txt')
