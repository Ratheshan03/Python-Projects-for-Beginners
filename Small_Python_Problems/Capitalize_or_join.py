def capitalize_or_join_words(sentence):
    """
    If the given sentence starts with *, capitalizes the first and last letters of each word in the sentence,
    and returns the sentence without *.
    Else, joins all the words in the given sentence, separating them with a comma, and returns the result.

    For example:
    - If we call capitalize_or_join_words("*i love python"), we'll get "I LovE PythoN" in return.
    - If we call capitalize_or_join_words("i love python"), we'll get "i,love,python" in return.
    - If we call capitalize_or_join_words("i love    python  "), we'll get "i,love,python" in return.

    Hint(s):
    - The startswith() function checks whether a string starts with a particualr character
    - The capitalize() function capitalizes the first letter of a string
    - The upper() function converts all lowercase characters in a string to uppercase
    - The join() function creates a single string from a list of multiple strings
    """
    # your code here
  
    if sentence.startswith('*'):
        words = sentence.replace('*', '').split()
        return ' '.join(capitalize_word(word) for word in words)

    words = sentence.split()
    return ','.join(words)
            
def capitalize_word(word):
    if not word:
        return ''
    if len(word) < 3:
        return word.upper()
    return word[0].capitalize() + word[1:-1] + word[-1].capitalize()


