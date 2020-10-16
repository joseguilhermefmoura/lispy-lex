import re
from typing import NamedTuple, Iterable


class Token(NamedTuple):
    """
    1. Named tuples are basically easy-to-create, lightweight object types.

    2. A token is a pair consisting of a token name and an optional attribute value.

    3. The token name is an abstract symbol representing a kind of lexical unit, e.g., a particular keyword, or sequence of input characters denoting an identifier.
    """
    kind: str
    value: str


def lex(code: str) -> Iterable[Token]:
    """
    1. This function returns a object sequence of type Token, corresponding to the lexical analise of the code string given.

    2. Regular expressions (regex) are used as notation to represent lexeme patterns for a token. They are used to represent the language for lexical analyzer. They assist in finding the type of token that accounts for a particular lexeme.

    3. So, we need to specify all the possible tokens by associating each of them to a unique regex.
    """

    possibles_tokens = [
        ("NUMBER",              r"(\+|\-|)?\d+(\.\d*)?"),    # REGEX TRANSLATION: A number may start or not with '+' and '-' characters, then have digits, and may have or not a '.' character followed by another digits.
        ("STRING",              r"\".*\""),                  # REGEX TRANSLATION: A string must start with ' " ' (double quotation) character and also ends with it.
        ("CHAR",                r"#\\[a-zA-Z]*"),            # REGEX TRANSLATION: A char must start with '#' character and be followed by a '\' character and letters'
        ("SINGLEQUOTE",         r"\'"),                      # REGEX TRANSLATION: A single quote character, ' ' '.     
        ("LPAR",                r"\("),                      # REGEX TRANSLATION: A left  parenthesis character, '('.
        ("RPAR",                r"\)"),                      # REGEX TRANSLATION: A right parenthesis character, ')'.
        ("BOOL",                r"#[t|f]"),                  # REGEX TRANSLATION: A boolean must start with '#' character and be followed by 't' OR 'f' character.
        ("NAME",                r"([a-zA-Z_%\+\-]|\.\.\.)[a-zA-Z_0-9\-\>\?\!]*"), # REGEX TRANSLATION: First, it matches any letter character, '_', '%', '+' and '-'; and "...". Then, match a single character composed by letters, numbers, '_' '>', '?' and '!' - multiple times. So, basically: it matches variables or function names. 
    ]

    # Also, it is needed to remove all the code commentary.
    code = re.sub(r";;.*", "", code)

    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in possibles_tokens)

    for mo in re.finditer(tok_regex, code):
        kind = mo.lastgroup
        value = mo.group()
        yield Token(kind, value)

    # The structure above was inspired by: https://docs.python.org/3/library/re.html#writing-a-tokenizer

    return [Token('INVALIDA', 'valor inválido')]