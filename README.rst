######
README
######

XHelp
*****
.. Brief description of project, what it is used for.
XHelp is a help-line application built on chat theme to provide easy way to
report an incident, tailored specifically for Kavach OS.

Installing / Getting started
============================
.. Introduction of minimal setup.
   Command, followed by explanation in next paragraph or after every command.
*  To use components, just copy ``src/`` or ``clone`` this repository and get
   started.
*  For GitHub commands, check ``docs/GitHubUsage.rst``.

Running
-------
*  Set-up dev environment (`Setting up dev`_).
*  ``cd`` to ``src/``.
*  Run ``XHelp.py`` using ``$ python XHelp.py`` or equivalent command.

Developing
==========
Built with
----------
.. List of main libraries, frameworks used including versions.
*  Python 3.x.
*  PyQt5.
*  PyTorch.
*  NLTK.

Prerequisites
-------------
.. What is needed to set up dev environment.
   For instances, dependencies or tools include download links.

Setting up dev
--------------
.. Brief intro of what to do to start developing.
   Commands with explanations as well.
*  Fork this repository.
*  Install all requirements by ``pip install -r requirements.txt``.
*  For ``PyTorch`` installation, check `PyTorch.org <https://pytorch.org>`_.
*  Check ``docs/Contributing.rst`` and get started.

Working with ``.ui`` files
--------------------------
1. ``cd`` to ``builder/qrc/``.
2. Copy all required resource files to ``builder/qrc/assets/``.
3. Copy all required ``.ui`` files to ``builder/qrc/``, with
   ``assets.qrc`` as their single resource file.
4. Now you can start working with your files.

Compiling ``.qrc`` file
-----------------------
1. ``cd`` to ``builder/qrc/``.
2. Copy all required resource files to ``builder/qrc/assets/``.
3. Edit ``builder/qrc/assets.qrc`` file accordingly.
4. Run ``$ pyrcc5 assets.qrc -o assets.py``.
5. Move the generated ``assets.py`` to ``src/XHelp/gui/``.
6. You're done!


Training bot and generating ``.pth`` file
-----------------------------------------
1. ``cd`` to ``builder/pth/``.
2. Copy ``intents.json`` file to ``builder/pth/``.
3. Run ``$ python nltk_utils.py``.
4. Run ``$ python train.py``.
5. Move the generated ``data.pth`` to ``src/XHelp/bot/``.
6. Copy updated ``intents.json`` file to ``src/XHelp/bot/``.
7. You're done!

Deploying / Publishing
----------------------
.. How to build and release a new version?
   Commands and explanation.
* Releases are not set up currently (coming soon).

Versioning
==========
.. SemVer versioning info, link to other versions.
0.0 - dev.

Configuration
=============
.. Configurations a user can enter when using the project.
*  Check ``config/VIM.vimrc`` for vim editors.

Tests
=====
.. Describe and show how to run tests with examples. Also, explain them with
   reasons.
*  Does not contain tests, but will be added later.

Style guide
===========
.. Coding style and how to check it.
*  Follows ``PEP 8`` python style guide.
*  Tabs are 4 space characters, not 3.

Database
========
.. Database versions and usages with download links.
   Also include DB Schema, relations, etc.
*  SQLite3 database.

Tables
------
*  Settings - Stores user settings to database as key-value pairs.
*  Messages - Stores conversations as tuple of session-id, sender, timestamp,
   message.

Licensing
=========
.. State license and link to text version.
Check ``LICENSE``.
