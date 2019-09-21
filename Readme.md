# Introduction
Find the definitions of given words and generate a txt file with **Chinese** translation, which can be loaded into Quizlet  
There are two input modes: **batch mode and live mode** (specified in instruction)

# Relating Website
youdao.com

# Requirement
Python: 3.4+  
Module: 
- requests
- lxml.tree

# Instructions
Open the program and choose a mode (1 for batch mode, 2 for live mode) 

Input the vacabulary words in either Batch mode and Live mode
## Batch mode
Input words in a txt file (./txt/input.txt), words separated by enter (\n). You need to create the file at the path before choosing the path.
## Live mode
Input words interactiviely. The program will return the Chinese and append result the result file.