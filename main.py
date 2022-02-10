

def open_file(file_name):
    with open(file_name) as file:
        for row in file:
            print(row)

# open_file('Jacob Kahn - Great_Expectations.txt')
# open_file('Jacob Kahn - Scarlet_Letter.txt')
