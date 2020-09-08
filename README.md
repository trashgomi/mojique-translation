# mojique-translation

This project is a fan-made English translation for MojiQue (もじクエ), the RPG by Ao Kurage (青くらげ).

## Progress

Text: 18960/18960 = 100% (Updated 05 September, 2020)

Images: 1084/1084 = 100% (Updated 18 July, 2020)

Testing: 130/130 = 100% (Updated 05 September, 2020)

The project has now reached version 1.0, meaning the game has been fully translated! Barring any bugfixes, the project is complete. Thanks to everyone who has helped out in any way.

## Get in Touch

Discord: **trashゴミ#7244**.

Email: trashgomi@protonmail.com.

## Donations

Please click the badge below to support me!

[![Donate](https://img.shields.io/badge/Donate-SubscribeStar-green)](https://www.subscribestar.com/trashgomi)

Donations are very much appreciated, and supporters will get early access to releases to my translations! Supporters can also optionally get their names added to the credits file distributed with my completed works.
Of course, the final translation will be available to all.

## Development

This section is required for anyone making any actual changes to the text in the game.

* First, download and install any tools that you think you need from the subsection below.
* Next, clone this repository into an appropriate folder on your computer.
* [Download the appropriate version of Mojique](https://aokurage.booth.pm/items/966800). This is necessary because the repo doesn't contain all of the game's files.
* Copy all of the downloaded game files into your local repository, but **don't overwrite any existing files**. The entire _mojikue ver-.--_ folder you downloaded goes inside the repo's root directory (_mojique-translation_)
* Test that the game runs.

### Tools Used

#### .ods Editor

Our translations are stored as .ods (OpenDocument Spreadsheets), with the hope that anyone can edit them whether they use software that is proprietary (such as Excel) or free as in freedom (such as [LibreOffice](https://www.libreoffice.org)).
If you are going to be writing any translations or localizations, either pick some software that can edit an .ods file, or consider Translator++ (see the below section).

#### Translator++

This project was made possible by [Translator++](https://forums.rpgmakerweb.com/index.php?threads/translator-game-translation-tool.102706/).
It is a spreadsheet-like front-end for all the dialogue in the game. Most importantly, it is required to patch the executable.

Unfortunately, the program has many problems, the most frustrating one being its tendency to fail when patching (upon which you will have to create a new patch and manually copy in all translations).
Furthermore, this program is not optimized for collaboration. It requires a bit more setup, but it does have some important advantages such as column headings and a global search feature.

Setup is as follows:

* Follow the main setup instructions to get your repository ready.
* In the program, **create a new project**. You will select the Mojikue _Game.exe_ file from the repository.
* Wait for the program to patch your executable and set up your cache. **This is what will allow you to export your translations later on.**
* Save your project. The output will be a .trans file. This file **cannot** be used by anyone else because of how it is cached on your machine - see below.

Translator++ does not let you import all columns of data from translation files, so you will be manually importing individual files of data as you need it, later on. Follow the set of instructions in the next section when you are ready to make a contribution.

## Contributors

If you are contributing in one of the ways mentioned above (or in some other capacity), please edit this file and leave your name and role here! Alternatively, ask someone else to add your name for you.

**Need your name pulled down?** [Let me know](mailto:trashgomi@protonmail.com).

* trashgomi - Project Lead, Repo Owner, Translations, Typesetting
* folley - Image Cleaning, Playtester
* WriterForce6XV - Translator++ Supplier
* AnonymousJS - Localization Consultancy, Misc.
* Kobold - Additional Translations
* 0x2F - Playtesting, Additional Scripts
* RubyRedRose - Playtesting