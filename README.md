# mojique-translation

This project is a fan-made English translation for Mojique (もじクエ), the RPG by Ao Kurage (青くらげ). If you aren't familiar with this RPG, its creator, or a concept called "omorashi", **now is the time to close this page**.

## Progress

Text: 18960/18960 = 100% (Updated 05 September, 2020)

Images: 1084/1084 = 100% (Updated 18 July, 2020)

Testing: 116/130 = 89% (Updated 05 September, 2020)

### Communication

Discord: **trashゴミ#7244**.

Email: trashgomi@protonmail.com.

### Donations

Please click the badge below to support me while I work on this project!

[![Donate](https://img.shields.io/badge/Donate-SubscribeStar-green)](https://www.subscribestar.com/trashgomi)

Donations are very much appreciated, and supporters will get early access to releases and exclusive blogs relating to the project! Supporters can also optionally get their names added to the credits file. Of course, the final translation will be available to all.

## Setup

This section is required for any contributors making any actual changes to the text in the game.

* First, download and install any tools that you think you need from the subsection below.
* Next, clone this repository into an appropriate folder on your computer.
* [Download the appropriate version of Mojique](https://aokurage.booth.pm/items/966800). This is necessary because the repo doesn't contain all of the game's files.
* Copy all of the downloaded game files into your local repository, but **don't overwrite any existing files**. The entire _mojikue ver-.--_ folder you downloaded goes inside the repo's root directory (_mojique-translation_)
* Test that the game runs.
* You are now ready to contribute!

### Useful Tools

#### .ods Editor

Our translations are stored as .ods (OpenDocument Spreadsheets), with the hope that anyone can edit them whether they use software that is proprietary (such as Excel) or free as in freedom (such as [LibreOffice](https://www.libreoffice.org)).
If you are going to be writing any translations or localizations, either pick some software that can edit an .ods file, or consider Translator++ (see the below section).

#### Translator++

This project is made possible by [Translator++](https://forums.rpgmakerweb.com/index.php?threads/translator-game-translation-tool.102706/).
I use this tool to patch the executable, but **it is not required by other contributors**.

Unfortunately, this program is not optimized for collaboration, and so we have to work around its limitations. It requires a bit more setup, but it does have some important advantages such as column headings and a global search feature.

Setup is as follows:

* Follow the main setup instructions to get your repository ready.
* Get the correct version of the software from me.
* In the program, **create a new project**. You will select the Mojikue _Game.exe_ file from the repository.
* Wait for the program to patch your executable and set up your cache. **This is what will allow you to export your translations later on.**
* Set up your columns by renaming and adding columns as appropriate:
  * The first column after the Japanese "Original Text" column should be called **Notes**, or similar
  * The second column should be **Character**, as it refers to the character speaking the corresponding dialogue
  * The third column is the **Initial** translation
  * The fourth column is the **Checked** translation
  * There must be a fifth column to accommodate the **Localized** translation
  * Column names are only seen by you, but you **must** at least have the correct number of editable columns (5)
* Save your project. The output will be a .trans file. It is for your use only, and should not be pushed to the repository.

Unfortunately, Translator++ does not let you import all columns of data from translation files, so you will be manually importing individual files of data as you need it, later on. Follow the set of instructions in the next section when you are ready to make a contribution.

If you'd like to use this software, **please contact me via [Discord](https://discord.gg/Zs3dgsP) or [email](mailto:trashgomi@protonmail.com) to get the correct version.**

## Making Changes

Choose a GitHub issue. Make an appopriately-named branch on which you can make commits as you please.

We are using multiple stages (columns) of translation.

* Assistant translators should write their translations into the **Initial** column (column **D**). 
* Lead translators should use the column called **Checked** (column **E**), and write their version of the initial translations in that column. If the initial version is correct, the lead translator can simply copy it into their **Checked** column.
* Localizers should write their version of checked translations in the **Localized** (column **F**) column. They should be careful not to change text that sounds good already, to avoid unnecessary work for everyone. When adding these localizations into the master branch, a translator will look at each line and either allow it, reject it in favor of the checked translation, or create something in-between.

### Method 1: Directly Edit the Source Files (Simpler)

* Identify which files you will need to modify. This information should be on the relevant issue on GitHub, or else you should make a list yourself.
* Make your changes.
* Check the public repo: has anyone else made changes to any files that you have touched? If so, things get a little more complicated. You will need to merge your changes together manually. Contact that contributor and work together to do this properly.
* In Git, ensure that your only changes are to the files that you changed.
* Commit to a **new, sensibly-named branch**. Push when ready!
* Your changes will be reviewed.

### Method 2: Translator++ (More Powerful)

* Identify which files you will need to modify. This information should be on the relevant issue on GitHub, or else you should make a list yourself.
* Bring those files up to date. For each file:
  * Open the appropriate .ods file in your .ods editor, such as Excel.
  * Select columns **B to F**. These correspond to the 5 columns we made earlier. Copy to clipboard.
  * In the corresponding Translator++ file click the correct cell: the very top-left non-Japanese cell. (This should be the **Notes** column, row 1).
  * Paste from clipboard.
  * If you did everything right, this file now contains every cell of data in the correct place!
  * Be aware that this method will overwrite the entire file, destroying any data currently in there.
  * If necessary, you can select only the rows that have data in them, to avoid overwriting your data with blank lines.
* Make your changes.
* Check the public repo: has anyone else made changes to any files that you have touched? If so, things get a little more complicated. You will need to merge your changes together manually. Contact that contributor and work together to do this properly.
* With any merge conflicts solved, save your project.
* You need to export your changed files as an .ods. Annoyingly, the main export option in Translator++ will end up changing every single file in the patch_output directory, so we will use an alternative method.
* In the Translator++ file list (on the left), tick the checkboxes of all of the files, and only the files, that you modified.
* Right click on any file > With x Selected > Export into... > ODS Spreadsheets > patch_output directory.
* In Git, ensure that your only changes are to those files.
* Additionally, you can commit your saved .trans file under the _tracked_ folder in the repo, in a subfolder that you make for yourself.
* Commit to a **new, sensibly-named branch**. Push when ready!
* Your changes will be reviewed.

### The Glossary

One of the most important parts of localization is to translate terms used within the world, in a consistent and interesting way. [This online spreadsheet](https://sheet.zoho.com/sheet/published.do?rid=hbvaibb530e19e4cb4abb98d4309d30b9433c) contains a list of our most subjective terms, especially those that are specific to this game and used repeatedly. Examples include character and place names, and other fictional concepts.

Contributors should skim through each page of this glossary before making translations or localizations, and keep an eye on the file as the project goes on.
Translators should update the glossary when they encounter new terms that they think should go on the list, and propose a localization for those terms!
Localizers are welcome to regularly go and propose new localizations as well, or dispute or agree with existing proposals.

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

## Supporters

Many thanks to those who have supported me through SubscribeStar or another platform!

If you donated and want your name listed in the Supporters file distributed with the game, please [contact me](mailto:trashgomi@protonmail.com).