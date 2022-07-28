############
Contributing
############

What/How to contribute?
=======================
You can contribute to almost anything in the repository, from a typo in
READMEs to fixing any error/bug in code or introducing new features.
Just remember to follow a general flow of contributing to projects, which
could be found on internet.

While working in community projects, it is a good thing to ask other
contributors or any other people in community before working on any part of the
project like working on new features, bugs, issues, etc, which helps to know
if someone is already working on it or not.

Pull requests
=============
1. Check with ``PEP 8`` coding style guidelines.
2. Put appropriate summary in commit regarding what's changed/fixed, with
   more details in description.
3. Combine multiple commits into single then create new pull request.
4. You're done!

Module structure
================
Do use the structure given below to push / update files.

All paths listed below (in this section only) are to be taken from
``src/XHelp/`` only.

*  ``core/`` - Contains binding code / files.
*  ``gui/`` - Contains all gui related files (``.ui`` and ``.py`` both).
*  ``bot/`` - Contains all files related to bot only.
*  ``database/`` - Contains all files related to DBMS only.
*  ``storage/`` - Contains databases and storage structures.

Code structure / style
======================
*  For ``.py`` files, name must be ``camelCased`` and begin with lower case
   letter only.
*  Each ``.py`` file must contain a ``Class`` with their names being
   ``CamelCased``, starting with upper case letter, and name not being fully
   upper cased.
*  Each function in ``.py`` file must start with a lower case letter only.

Working with GitHub
===================
Check ``docs/GitHubUsage.rst`` for how to perform various git operations.
