alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().

def caesar(shift_direction, input_text, shift_amount):
    output_text = ""
    if shift_direction == "decode":
        shift_amount *= -1
    for char in input_text:
        position = alphabet.index(char)
        new_char = alphabet[position + shift_amount]
        output_text += new_char
    print(f"Your {shift_direction}d text is {output_text}")


# TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.

caesar(direction, text, shift)
