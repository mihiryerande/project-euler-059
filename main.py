# Problem 59:
#     XOR Decryption
#
# Description:
#     Each character on a computer is assigned a unique code
#       and the preferred standard is ASCII (American Standard Code for Information Interchange).
#     For example,
#         uppercase A  = 65,
#         asterisk (*) = 42, and
#         lowercase k  = 107.
#
#     A modern encryption method is to take a text file, convert the bytes to ASCII,
#       then XOR each byte with a given value, taken from a secret key.
#     The advantage with the XOR function is that using the same encryption key on the cipher text,
#       restores the plain text; for example,
#         65  XOR 42 = 107, then
#         107 XOR 42 = 65.
#
#     For unbreakable encryption, the key is the same length as the plain text message,
#       and the key is made up of random bytes.
#     The user would keep the encrypted message and the encryption key in different locations,
#       and without both "halves", it is impossible to decrypt the message.
#
#     Unfortunately, this method is impractical for most users,
#       so the modified method is to use a password as a key.
#     If the password is shorter than the message, which is likely,
#       the key is repeated cyclically throughout the message.
#     The balance for this method is using a sufficiently long password key for security,
#       but short enough to be memorable.
#
#     Your task has been made easy, as the encryption key consists of three lower case characters.
#     Using p059_cipher.txt (right click and 'Save Link/Target As...'), a file containing the encrypted ASCII codes,
#       and the knowledge that the plain text must contain common English words,
#       decrypt the message and find the sum of the ASCII values in the original text.

from itertools import permutations
from string import ascii_lowercase


def main(filename):
    """
    Decrypts the text given in `filename` assuming that it was XOR-encrypted
      with a key of three lowercase letters, and the text contains common English words.

    Args:
        filename (str): File name containing encrypted text

    Returns:
        (Tuple[str, str, int]):
            Tuple of
    """
    assert type(filename) == str

    # Read the bytes of the encrypted text
    with open(filename, 'r') as f:
        e_bytes = list(map(int, f.read().split(',')))
    e_text = ''.join(map(chr, e_bytes))

    # Check for these common words
    common_words = ['the', 'of', 'in']

    # Iterate through different possibilities of encryption key
    key_len = 3
    for key_chars in permutations(ascii_lowercase, key_len):
        key_str = ''.join(key_chars)
        key_bytes = list(map(ord, key_chars))

        # Decrypt using this key
        d_bytes = []
        for i, e_byte in enumerate(e_bytes):
            d_byte = e_byte ^ key_bytes[i % key_len]
            d_bytes.append(d_byte)

        # Check if it looks correct
        d_text = ''.join(map(chr, d_bytes))
        d_text_lower = d_text.lower()
        if d_text.isprintable() and all(map(lambda w: w in d_text_lower, common_words)):
            print('{} -> {}'.format(key_str, d_text))
            if input('      Looks good? (Y/N): ').lower() == 'y':
                d_sum = sum(d_bytes)
                return key_str, e_text, d_text, d_sum


if __name__ == '__main__':
    encrypted_file_name = 'p059_cipher.txt'
    encryption_key, encrypted_text, decrypted_text, ascii_sum = main(encrypted_file_name)
    print('Key used to encrypt "{}":'.format(encrypted_file_name))
    print('  {}'.format(encryption_key), end='\n\n')
    print('Encrypted text:')
    print('  {}'.format(encrypted_text), end='\n\n')
    print('Decrypted text:')
    print('  {}'.format(decrypted_text), end='\n\n')
    print('Sum of decrypted ascii values')
    print('  {}'.format(ascii_sum))
