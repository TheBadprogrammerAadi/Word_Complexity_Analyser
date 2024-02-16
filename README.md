# Word_Complexity_Analyser
This is a program that will analyse a word and give it a complexity score.


This Script is part of one of my projects I am trying to build.

For this project I needed a way to create a value to see what is a complexity of a word.But after searching the internet far and wide i found no help.
So to fix this problem i decided to make it myself.The process first involved looking into the internet finding different ways on how we analyse words
and deduce a way to create a numerical value for the complexity.

With my research I discorvered teh things i needed were :
Unique letters 
number of letters 
frequency
syllables

After this discovery I realised i would need to find the correct libraries to find out these values.Thankful with a bit of research i stumbled apon syllapy 
NLTK and the inbuilt function Len.This would be how I implemented this program.

After implenting them i decided just to times all the values i got to use a complexity score.But What i realised was that due to high frequency the complexity 
score of a word would go up.But it should be going down instead.So after many different variations I stuck with the reciprocal of the frequency times by all the 
other values.

Then I learnt pandas to implemnt this into my project.


I really enjoyed this project.
