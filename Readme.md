# Content
- [Content](#content)
- [Introduction](#introduction)
- [Relating Website](#relating-website)
- [Requirement](#requirement)
  - [Python: 3.*](#python-3)
  - [Module:](#module)
- [Program Instructions](#program-instructions)
  - [Batch mode](#batch-mode)
  - [Live mode](#live-mode)
- [Quizlet Import Instructions](#quizlet-import-instructions)
# Introduction
Find the definitions of given words and generate a txt file with **Chinese** translation, which can be loaded into Quizlet  
There are two input modes: **batch mode and live mode** (specified in instruction)

# Relating Website
youdao.com  

Visit youdao.com to get Chinese translations

# Requirement
## Python: 3.*  
## Module: 
- requests
- lxml.tree
- time.time
- tqdm.tqdm

# Program Instructions
1. Open the program and choose a mode (1 for batch mode, 2 for live mode) 
2. Input the vacabulary words in either Batch mode and Live mode
## Batch mode
Input words in a txt file (./txt/input.txt), words separated by enter (\n). You need to create the file at the path before choosing the mode.
## Live mode
Input words interactiviely. The program will return the Chinese and append result the result file.

# Quizlet Import Instructions
1. Click "Create" at the home page
2. Click "Import from Word, Excel, Google Docs, etc."
3. Copy and paste content in the output.txt into the frame.
4. Click "Import"
5. Follow the prompt to add languages and click "Import" again.