import pandas as pd

df = pd.read_csv("../nato_phonetic_alphabet.csv")

new_dict = {n.letter:n.code for (index, n) in df.iterrows()}

not_error = True

nato_list = []
while not_error:
    try:
        user_word = input(f"Enter a word: ").upper()
        nato_list = [new_dict[nato] for nato in user_word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
    else:
        print(nato_list)
        not_error = False
    finally:
        if len(nato_list) == 0:
            try:
                raise Exception('Invalid input')
            except Exception as gen_err_msg:
                print(gen_err_msg)
                not_error = True



