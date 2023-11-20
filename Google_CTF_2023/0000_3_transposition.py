def decode_columnar_transposition_v3(ciphertext, key):
    # Normalize key (remove spaces and make uppercase)
    key = ''.join(key.split()).upper()

    # Create a list of tuples (char, index), sort it, then extract indices
    sorted_key_tuples = sorted([(char, index) for index, char in enumerate(key)])
    sorted_key_indices = [index for _, index in sorted_key_tuples]

    # Calculate the number of full rows and the remaining characters
    num_full_rows = len(ciphertext) // len(key)
    remaining_chars = len(ciphertext) % len(key)

    # Create a grid to hold the ciphertext
    grid = [['' for _ in range(len(key))] for _ in range(num_full_rows + (1 if remaining_chars > 0 else 0))]

    # Place the ciphertext into the grid column by column according to the key order
    index = 0
    for col in sorted_key_indices:
        for row in range(num_full_rows + (1 if col < remaining_chars else 0)):
            if index < len(ciphertext):
                grid[row][col] = ciphertext[index]
                index += 1

    # Read off the grid row-wise
    plaintext = ''.join(''.join(row) for row in grid)
    return plaintext

if __name__ == "__main__":
    
    ciphertext = '''rs␣r␣enigm␣␣aierhe␣i␣gluucsclhetersnti␣a␣rla␣t␣riayrgpetai␣diu␣Fawhiho}sipatfy␣ihr␣a␣rfa␣pes␣etohwrea␣octtonee␣eihetTpxcdeghi␣ro␣ped␣yGaledemXToneepetlhtseghectnatanst␣ripctiharaics␣foarscee␣ebrn␣te␣doemrr␣c__ltcsaicsa␣coo␣wbrn␣␣aranmeibti,haarhra,sipklti␣ci.ctst␣a␣lxtcnaenlkLeoakelXpohry␣patakrntd␣cilxsU␣inehe␣cwthers␣rpo␣narahhtr␣aienlsrtrr␣o.{rd___nXnti␣␣ornrtoyrgoors␣te.ksip␣␣crs␣␣c␣pohelhgctn␣ie␣erntatecg␣teeeAsuvesuX'''
    key = "CAESAR"
    
    # Decoding with the adjusted approach
    decoded_text_v3 = decode_columnar_transposition_v3(ciphertext, key)
    print(decoded_text_v3)


