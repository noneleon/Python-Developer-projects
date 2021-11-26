'''
Description
The first step of this project is preparation for a convenient translation process. At this stage, there'll be only two available languages: English and French. The program should suggest to the user to choose the direction of the translation and the word to translate. Then, the confirmation message should be printed.

Objectives
At this stage, your program should:

Output the welcoming message: Type "en" if you want to translate from French into English, or "fr" if you want to translate from English into French:
Take an input specifying the target language.
Output the message: Type the word you want to translate:
Output the confirmation message in the format You chose "language" as a language to translate "word"., where language is either en or fr and word is the word chosen by the user.
Example
The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

Type "en" if you want to translate from French into English, or "fr" if you want to translate from English into French:
> fr
Type the word you want to translate:
> hello
You chose "fr" as the language to translate "hello" to.
We don't really need this output to appear at the end. However, aside from keeping the user informed, it does something else: it's showing us if the arguments were successfully accepted by the function. Keep it in mind while proceeding from stage to stage!

 Report a typo
'''

print('Type "en" if you want to translate from French into English, or "fr" if you want to translate from English into French:')
a = input()
print("Type the word you want to translate:")
word = input()
print(f'You chose "{a}" as the language to translate "{word}" to.')


\\

def main():
    language = input('Type "en" if you want to translate from French into English, '
                     'or "fr" if you want to translate from English into French:\n')
    word = input("Type the word you want to translate:\n")
    print(f'You chose "{language}" as a language to translate "{word}"')


if __name__ == "__main__":
    main()
\\
lang = input(
    'Type "en" if you want to translate from French into English, '
    'or "fr" if you want to translate from English into French:\n'
)
word = input("Type the word you want to translate:\n")
print(f'You chose "{lang}" as the language to translate "{word}" to.')
