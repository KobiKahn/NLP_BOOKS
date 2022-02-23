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
                if num_word_paragraph != 0:
                    num_paragraph += 1
                    # print(num_sentence)
                    list_sentence_paragraph.append(num_sentence)
                    list_word_paragraph.append(num_word_paragraph)
                    # print(f'{file_name}: {list_sentence_paragraph}')

                    num_sentence = 0
                    num_word_paragraph = 0
                else:
                    pass

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
    return(mean, standard_dev, variance)


def graph_gaussian(list1, list2, mean1, mean2, SD1, SD2, variance1, variance2):

    y_list1 = []
    x_list1 = []

    y_list2 = []
    x_list2 = []

    x_start1 = mean1 - 1.5 * SD1
    delta_x1 = (3 * SD1) / 100
    m_s1 = mean1 - SD1
    mps1 = mean1 + SD1

    x_start2 = mean1 - 1.5 * SD2
    delta_x2 = (3 * SD2) / 100
    m_s2 = mean2 - SD2
    mps2 = mean2 + SD2

    # COMPUTE FOR FILE 1
    for i in range(100):
        x = i * delta_x1 + x_start1

        y = (1 / (SD1 * math.sqrt(2 * math.pi))) * math.e ** - (((x - mean1) ** 2) / (2 * variance1))
        y_list1.append(y)
        x_list1.append(x)

        y_left = (1 / (SD1 * math.sqrt(2 * math.pi))) * math.e ** - (((m_s1 - mean1) ** 2) / (2 * variance1))
        Left1 = y_left

        y_right = (1 / (SD1 * math.sqrt(2 * math.pi))) * math.e ** - (((mps1 - mean1) ** 2) / (2 * variance1))
        Right1 = y_right

    # plt.axis([mean1 - (1.5 * SD1), mean1 + (1.5 * SD1), min(y_list1), max(y_list1)])
    apex1 = max(y_list1)
    plt.plot(x_list1, y_list1, '-b')
    plt.plot([mean1, mean1], [0, apex1], '-c')
    plt.plot([mean1 - SD1, mean1 - SD1], [0, Left1], '-c')
    plt.plot([mean1 + SD1, mean1 + SD1], [0, Right1], '-c')


    # COMPUTE FOR FILE 2
    for i in range(100):
        x = i * delta_x2 + x_start2

        y = (1 / (SD2 * math.sqrt(2 * math.pi))) * math.e ** - (((x - mean2) ** 2) / (2 * variance2))
        y_list2.append(y)
        x_list2.append(x)

        y_left = (1 / (SD2 * math.sqrt(2 * math.pi))) * math.e ** - (((m_s2 - mean2) ** 2) / (2 * variance2))
        Left2 = y_left

        y_right = (1 / (SD2 * math.sqrt(2 * math.pi))) * math.e ** - (((mps2 - mean2) ** 2) / (2 * variance2))
        Right2 = y_right

    apex2 = max(y_list2)
    plt.plot(x_list2, y_list2, '-k')
    plt.plot([mean2, mean2], [0, apex2], '-r')
    plt.plot([mean2 - SD2, mean2 - SD2], [0, Left2], '-r')
    plt.plot([mean2 + SD2, mean2 + SD2], [0, Right2], '-r')

    plt.legend(['Great Expectations', 'Scarlet Letter'], loc = 'upper right')
    plt.show()


def main(filename1, filename2):

    list_sentence_paragraph1, list_word_paragraph1, list_word_sentence1, list_comma_sentence1 = open_file(filename1)
    list_sentence_paragraph2, list_word_paragraph2, list_word_sentence2, list_comma_sentence2 = open_file(filename2)

    # list1, list2, mean1, mean2, SD1, SD2, variance1, variance2

    mean1, SD1, variance1 = calculate_M_SD(filename1, list_word_paragraph1)
    mean2, SD2, variance2 = calculate_M_SD(filename2, list_word_paragraph2)


    graph_gaussian(list_comma_sentence1, list_comma_sentence2, mean1, mean2, SD1, SD2, variance1, variance2)




main('Jacob Kahn - Great_Expectations.txt', 'Jacob Kahn - Scarlet_Letter.txt')