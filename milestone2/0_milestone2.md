# COLX 523 - Advanced Corpus Linguistics

# Milestone 2                   

## Overview

For this milestone, you should complete your corpus collection, and prepare for the annotation part of the project.

## Repo and data storage
rubric={mechanics:2}
- Make sure you follow the instructions from Milestone 1, in terms of location of your files in the repo, use of branches, etc.                                                                                       
- At the end of this milestone, you will have a corpus. If it is small enough (or made up of smaller files), you can store it in your github repo, but remember that there is a 100MB limit. If your corpus doesn't fit on your repo, store it somewhere else (like Google drive), and have a link from your repo. 

## Corpus collection code
rubric={accuracy:3, quality:3}

You should provide the code you have used to build your corpus. For most, there is the expecation that we could run this code and completely rebuild your corpus (though this might not necessarily be the case if, say, it was based on doing time-sensitive searches or streaming of twitter). Please pay attention to the following:

- It should be easy for us to run this code. If there are any input or output files, make sure we have everything we need, and is easy to edit the paths to these files. When in doubt, explain.
- For full points, your code must to have the ability to stop and restart without redoing things you've already done, and without loss of data. You have to tell us how to do this. Assume we will test it.
- As reflected in the rubric, the quality of your code is important and we will enforce high standards in this course. Please review the rubric for [quality](https://github.com/UBC-MDS/public/blob/master/rubric/rubric_quality.md) carefully. Make sure you break things into functions when appropriate, and add documentation and improve aspects of readability until you are confident that we will have no problem understanding how your code works. 
- If you have any code which filters the result of your initial collection into your final corpus, include that too, with explanation.
- Either .ipynb or .py format is fine
- You do not have to store this code in the milestone 2 folder, but there should be a link in the readme                                            

## Corpus + explanation
rubric={raw:3,reasoning:1,writing:1}

You need to have finished collection of a large corpus of text with the basic properties described in Milestone 1. You should include a corpus_readme.md file in the milestone folder which provides the following basic information

- Link to the source of the corpus and a link to location of your collected corpus (either on your repo, or externally)
- Information about the format it is stored in (incl. metadata)
- total number of documents
- total amount of text (in words, ideally, though for instance characters would be acceptable for Chinese)
- Any known problems with the corpus (e.g. duplicates, noise)


## Corpus analysis (Optional)
rubric={reasoning:2}

You can get bonus points in this milestone by doing an in-depth analysis of your corpus, using the kinds of approaches we talked about in COLX 521. Compare the statistical properties of your corpus to other corpora with interesting similarities and/or differences. If you have metadata, provide a discussion of any interesting interaction between the metadata and the corpus statistics you derive. You should do this in a separate .md file (corpus_analysis.md), and include links to any code you write to carry out this analysis.


## Annotation plan
rubric={reasoning:3,writing:2} 

Provide your detailed plan for doing the annotation, including

- The exact kind of annotation you will be doing (for details, you can refer to the annotator guidelines, but you should give a basic outline here)
- The tools you will be using to create your annotation.
- Who your annotators will be. If you are using people you know, you must have at least two so you can calculate interannotator agreement, and they should have already agreed to help, and have the appropriate language background for the task. If you are using Mechanical Turk, for this milestone you should have successfully had at least one worker complete one annotation, to prove you can get workers for your task (please mention that you've done this in the text!)
- Your rough expectation for the amount of data you will be able to have annotated before the next milestone, based on limiting factors such as the availability of your annotators and/or costs. If you are using Mechanical Turk, we will give the group $50 for annotation, and expect you to use this money carefully with between 3-5 "respondents per assignment" (workers per individual annotation). If you are using people you know, you need to have annotators that are willing to spend at least several hours doing annotations for you (for this calculation you should assume they are doing the exact same annotation, i.e. you will calculate interannotator agreement over all the texts your annotate). Propose what you think is feasible given your resources, and we will let you know if we think the amount of annotation you are doing is insufficient to satisfy the requirements of the next milestone.                                                                                   
- Any steps you have taken or intend to take to ensure the quality of your annotations, including things such as annotator training, Mechanical Turk worker restrictions, and pilot studies.
- We strongly recommend you do a pilot study for this milestone, with a small amount of the total data you expect to annotate. If you have done this, please discuss the results (did everything go smoothly?.

## Annotation materials
rubric={reasoning:2,writing:1,raw:1}

- Provide an initial draft of your annotation guidelines. This should include a basic description of the task and explain of each possible label that an annotator might choose, with examples. For Mechanical Turk, this is ideally in the form of the actual page that you will show to your annotators (you can send us a link to the task on the Mechanical Turk Worker Sandbox, or just provide a copy of the page in your repo).

- A small amount of data (at least 10 examples) that has been processed into a format appropriate for annotation (e.g. a csv for upload to Mechanical Turk). You should include a link to the code that produced it from your corpus.


## Prompt completion
rubric={raw:4}

You should finish everything discussed above by 11:59pm Saturday, Mar 6th. If you were not able to complete it on time (in lieu of the typical 50% penalty) you will lose 1 points from your prompt completion score for each 12 hour period after the deadline. When you are done with a milestone (regardless of whether you are on time or late), one of your teammates MUST open an issue in your repo that says you are done. Any modification of the relevant documents in your milestone folder after you have opened this issue will likely result in losing all your prompt completion points.
