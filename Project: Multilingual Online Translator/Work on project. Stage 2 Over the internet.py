'''
Theory
User-Agent field in a request

When you use requests library, you can pass headers arguments to the function get(). Headers are text data you send over HTTP that might contain information about a web browser or application you use to surf the web. Your program doesn't use any web browser as we usually do, but it still has to present itself as some kind of a browser to be able to get the web pages. For this purpose, there's a 'User-Agent' field that forms a request.

headers = {'User-Agent': 'Mozilla/5.0'}
page = requests.get(url, headers=headers)
Think of it as a visit card that your program shows to the website before it can enter it. It introduces itself as a web browser to the website it's trying to get a page from; otherwise, the website might not allow the connection from something other than a browser.

Selecting text data

When you access a web page, an important question is how to get the data that you need in a readable form without HTML tags. The answer is CSS. You can access this text via CSS classes and tags. All you need is to go to the web page, open your browser’s Dev Tools, and find these elements in CSS code. You can get access to your browser’s DevTools in three different ways:

Keyboard: Ctrl + Shift + I, except

Internet Explorer and Edge: F12
macOS: ⌘ + ⌥ + I
Menu bar:

Firefox: Menu ➤ Web Developer ➤ Toggle Tools, or Tools ➤ Web Developer ➤ Toggle Tools
Chrome: More tools ➤ Developer tools
Safari: Develop ➤ Show Web Inspector. If you can't see the Develop menu, go to Safari ➤ Preferences ➤ Advanced, and check the Show Develop menu in the menu bar checkbox.
Opera: Developer ➤ Developer tools
Context menu: Press-and-hold/right-click an item on a web page (Ctrl-click on the Mac), and choose the option Inspect Element from the context menu that appears (an added bonus: this method highlights the code of the element you right-clicked.)

After you’re done with CSS, check it.

Description
At this stage, you'll be able to implement a real translator program! A great website called ReversoContext will help you to do that. ReversoContext is a multilingual translator tool that allows seeing original phrases that should be translated and their equivalents in other languages in contexts (example sentences). That's a very useful feature since the meaning of the word depends greatly on the context. Hence, when you see a context, it's easier for you to choose the right translation.

The goal of your program at this stage is to find translations and example sentences for a given word. The word can be either in French or in English, and the translation should be in the opposite language (that is, English or French, respectively).

To understand how to do this, go to ReversoContext and type any word you want to translate. After receiving the result, pay attention to the address bar of your browser. You will see the URL, for example:

https://context.reverso.net/translation/english-french/cheese

Here you see the language-translation pair «English-French», which represents the direction of translation, meaning that the translation is from English to French and not the other way around. After the last backslash, you can see the word being translated.

Your goal is to make your program act as if it visits the website for you. To make it happen, tell your program to generate the correct URL with the word you type, determine the translation direction, and send the URL to the website.

After getting to the needed page, the program should extract the required data: translations and sentences with usage examples. In the screenshot below, translations are highlighted with blue, and sentences for the target language are presented in a list in the right column.



Objectives
At this stage, your program should:

Take an input specifying the target language (en if the user wants to translate from French into English, or fr if the user wants to translate from English into French).
Take an input specifying the word that should be translated.
Output the confirmation message in the format You chose "..." as a language to translate "...".
Form a request and connect to ReversoContext.
Check the HTTP status of the response of the website to your request. If the status code is 200, you are good to proceed! If not... Try again?
Output the response of the website to your request (200) and OK message to show that the connection is successful (so, the entire line should be 200 OK).
Output the line Translations.
Output a list with translations of the given word in the target language: ['bonjour', 'salut'].
Output a list with examples of sentences featuring the given word or any of its translations: ['Well, hello, freedom fighters.', 'Et bien, bonjour combattants de la liberté.']. Both the original versions of the sentences and their translations should be printed. You don't need to filter sentences in any way: just print all the sentences that ReversoContext output for the given language pair and the given word.
Make sure you output exactly the sentences that ReversoContext shows initially on the page https://context.reverso.net/translation/{language_1}-{language_2}/{word}. Don't confound them with the sentences that the website shows when you click on the first translation equivalent. These sentences will not be accepted by tests.

Also, please, make sure your program follows the described format of the output.

Example
The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

Type "en" if you want to translate from French into English, or "fr" if you want to translate from English into French:
> fr
Type the word you want to translate:
> hello
You chose "fr" as a language to translate "hello".
200 OK
Translations
['bonjour', 'allô', 'ohé', 'coucou', 'salut', 'hello', 'bonsoir', "quelqu'un", 'bien le bonjour', 'Oh', 'Enchanté', 'saluer', 'ça', 'salue', 'Oui']
['Well, hello, freedom fighters.', 'Et bien, bonjour combattants de la liberté.', 'Goodbye England and hello the Netherlands...', "Au revoir l'Angleterre et bonjour les Pays-Bas...", 'Yes, hello. Jackson speaking.', "Oui, allô, Jackson à l'appareil.", 'Hello, hello, hello, hello.', 'Allô, allô, allô, allô.', 'And began appearing hello kitty games online.', 'Et a commencé à apparaître bonjour Kitty jeux en ligne.', 'Tell him hello... and congratulations.', 'Je lui dis bonjour et je le félicite.', 'A special hello to everyone from YouTube Bibi.', 'Un bonjour spécial à tout le monde de la chaîne de beauté YouTube de bibi.', 'Yes, hello, Mr Teodoresco.', 'Oui, bonjour, M. Teodoresco.', 'Well hello, Milan and Eve.', 'Eh bien bonjour, Milan et Eve.', 'Well hello, welcome to the Tree House pond.', "Alors bonjour, bienvenue à l'étang de la Maison de l'arbre.", 'pink hello kitty seat 2,3 - Auto Outlet', 'rose bonjour 2,3 siège de minou - Auto Outlet', 'hello world PL/SQL procedure successfully completed. SQL', 'bonjour procédure monde PL / SQL terminée avec succès. SQL', '"Maido-san" means something like "hello" in Kanazawa dialect.', 'Maido-sans veut dire quelque chose comme bonjour dans le dialecte de Kanazawa.', 'So anyway, hello and goodbye.', 'Donc voilà, bonjour et au revoir.', 'You can hardly hear him saying hello.', "On l'entend à peine dire bonjour.", "Yes, hello. I'd like to blackmail the Prime Minister.", "Oui, bonjour, j'aimerais faire chanter le premier Ministre.", 'Well, please tell her hello for us.', 'Bien, dites lui bonjour de notre part.', 'Homie, I think someone is saying hello.', "Homer, je crois qu'on te dit bonjour.", 'Well, hello, Susan and welcome.', 'Bien, bonjour Susan et bienvenue.', 'Normally, one says "hello" only once.', 'Normalement, on dit bonjour une fois.']
Here you can see the results that are almost readable, but there are a lot of quotes and commas. The next stage is all about the representation!


'''

from bs4 import BeautifulSoup
import requests
import itertools

language = input('Type "en" if you want to translate from French into English, '
                 'or "fr" if you want to translate from English into French:\n')
word = input("Type the word you want to translate:\n")
print(f'You chose "{language}" as a language to translate "{word}"')
translation = "english-french" if language == "fr" else "french-english"
headers = {'User-Agent': 'Mozilla/5.0'}
page = requests.get(f'https://context.reverso.net/translation/{translation}/{word}', headers=headers)
print(f"{page.status_code} {page.reason}\nTranslations")
soup = BeautifulSoup(page.text, 'html.parser')
print(soup.find("div", id="translations-content").text.split())
src = [div.text.strip() for div in soup.findAll("div", class_="src ltr")]
trg = [div.text.strip() for div in soup.findAll("div", class_="trg ltr")]
print(list(itertools.chain(*((s, t) for s, t in zip(src, trg)))))


\\

import requests
from bs4 import BeautifulSoup as bsFour


class Translator:
    headers = {'User-Agent': 'Mozilla/5.0'}
    languages = {'en': 'english', 'fr': 'french'}

    def __init__(self):
        self.word = None
        self.language = None
        self.other = None
        self.lg = None
        self.r = None

    def select_language(self):
        print('Type "en" if you want to translate from French into English, or "fr" if \
you want to translate from English into French:')
        choice = input()
        self.lg = choice
        self.language = Translator.languages[choice]
        self.other = list(Translator.languages.values())[list(Translator.languages.values()).index(self.language) - 1]

    def select_word(self):
        print('Type the word you want to translate:')
        choice = input()
        self.word = choice
        print(f'You chose "{self.lg}" as a language to translate "{self.word}".')

    def get_answer(self):
        self.r = requests.get(f'https://context.reverso.net/translation/\
{self.other}-{self.language}/{self.word}', headers=Translator.headers)
        print(f'{self.r.status_code} OK')

    def translate(self):
        soup = bsFour(self.r.content, 'html.parser')
        words = [''.join(word.text.strip().split()) for word in soup.find(id="translations-content")]
        print('Translations')
        print([word for word in words if word])
        list_example = [str(string.text).strip() for string in soup.find_all('div', {'class': 'src ltr'})]
        print(list_example)


translator = Translator()
translator.select_language()
translator.select_word()
translator.get_answer()
translator.translate()