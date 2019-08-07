# mojique-translation

This project is a fan-made English translation for Mojique (もじクエ), the RPG by Aoi Kurage (青くらげ). If you aren't familiar with this RPG, its creator, or a concept called "omorashi", **now is the time to close this page**.

## Progress

Lines Fully Translated: 0/19466 (Updated 07/24/2019)

I have made a small start on establishing this project, but it is currently in the process of gathering volunteers. If you'd like to see this translation get started, please spread word far and wide! Also consider joining yourself: see the section below.

## Can I Help?

There are many ways you can contribute, whether or not you can translate Japanese.

* If you have a very strong grasp of both Japanese and English, you can act as a **lead translator**. We need at least one of these! Lead translators will be in charge of organising other translators, checking translations for correctness, and deciphering the most obscure lines of Japanese dialogue.
* If you have decent knowledge of both Japanese and English, you can be an **assistant translator**. We need several of these. Assistant translators will do a lot of the heavy lifting and translate most of the text so that the lead translators can do their job.
* If you are fluent in English, you can act as a **localizer**. Localizers will ensure that every line of dialogue sounds natural and has appropriate levels of expression and stylization.
* We also need at least one **typesetter**. This is someone who knows a thing or two about image editing (e.g. Photoshop) and can add English text to images in place of Japanese text.
* Otherwise, you can be a **playtester** (as long as you have a decent grasp of English). Playtesters will check for typos, missing translations and other dialogue errors, as well as ensuring that the game works as it should.

To contribute, you should register for a GitHub account. Ideally, all translators should know how to create commits to this project - you can find out how using the [GitHub guides](https://guides.github.com/).
Localizers and playtesters can get away with simply creating [issues](https://github.com/trashgomi/mojique-translation/issues) on this project as appropriate.

### Donations

It is possible that some of our contributors may wish to receive donations - but this isn't happening yet. We would have to decide whether this is feasible; how it can be managed; and methods of transfer. It may also not be okay to do without Aoi Kurage's blessing. 

## Setup

This section is required for any contributors making any actual changes to the text in the game.

* First, download and install any required tools from the subsection below.
* Next, clone this repository into an appropriate folder on your computer.
* [Download the appropriate version of Mojique](https://aokurage.booth.pm/items/966800). This is necessary because the repo doesn't contain all of the game's files.
* Copy all of the downloaded game files into your local repository, but **don't overwrite any existing files**. The entire _mojikue ver-.--_ folder you downloaded goes inside the repo's root directory (_mojique-translation_)
* Test that the game runs.
* Run Translator++ and open the _translation.trans_ file.
* You are now ready to contribute!

### Required Tools

This project is made possible by [Translator++](https://forums.rpgmakerweb.com/index.php?threads/translator-game-translation-tool.102706/).
This tool is required for making any changes to the game. [Download here.](https://mega.nz/#F!P191mCib!f1gDY15BkUN20_61ikoAew)

## Making Changes

The best way to add new translations is to first choose a scene (i.e. one of the many maps) that hasn't been touched yet. Then you should make an appopriately-named branch and make commits to that branch as you please.

Translator++ supports multiple columns (stages) of translations.
* Assistant translators should write their translations into the **Initial** column. 
* Lead translators should use the column called **Checked**, and write their version of the initial translations in that column. If the initial version is correct, the lead translator can simply copy it into their **Checked** column.
* Localizers should write their version of checked translations in the **Localised** column. However, localizers must then get all of their localized lines checked once more by a lead translator.

When you have finished work on a branch, you should export the changes as RPGMakerTrans formatted \*.txt files to the _patch_output_ directory. Ensure that you only commit the relevant changes. Although these files aren't used in the game, this step is important because it makes it much easier for collaborators to view your changes using the Git diffs.

Branches shouldn't be merged into _master_ until they have gone through this whole process.

Following this convention, we can avoid work overlap and merge conflicts.

## Contributors

If you are contributing in one of the ways mentioned above (or in some other capacity), please edit this file and leave your name and role here! Alternatively, ask someone else to add your name for you.
**Need your name pulled down?** [Let me know](mailto:trashgomi@protonmail.com).

* trashgomi - Assistant Translator, Repo Owner
* WriterForce6XV - Localizer, Playtester, Bugfixer
* 0x2F - Playtester
* RubyRedRose - Playtester
