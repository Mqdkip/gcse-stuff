def run_length_encode(text):

    encoded_text = []

    if len(text) == 0:
        return ""

    if len(text) == 1:
        return "1"+text


    current_letter = text[0]
    letter_count = 1
    code_text = ""

    for letter in text[1:]:
        if letter == current_letter:
            letter_count += 1

        else:
            code_text += str(letter_count) + current_letter
            current_letter = letter
            letter_count = 1

    code_text += str(letter_count) + current_letter
    return code_text



text_to_code = input("Input the text that you want to ecode using RLE: \n")
print(f"Encoded text is {run_length_encode(text_to_code)}")
