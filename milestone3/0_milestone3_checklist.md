# COLX 523 - Advanced Corpus Linguistics

# Milestone 3                   

## Repo and data storage
rubric={mechanics:2}
                                                                                 
- [ ] Store annotations together with the main corpus in a sensible way, and make sure to document the relationship between the two.

## Annotation + explanation + code
rubric={raw:3,accuracy:2,quality:1,reasoning:2, writing:1}

- [ ] Finish an annotation of roughly the size promised in the previous milestone (or larger), including:
    - [ ] Link to any intermediary files produced during the annotation process (e.g. csvs downloaded from mechanical turk, excel documents for individual annotators, etc.)
    - [ ] Document what the intermediary files are
    - [ ] Link to the final version of the annotation. DO NOT include information from multiple annotators, but a single 'best' annotation
    - [ ] If there is an easy mapping from a "document" in the corpus to a single annotation, the annotation can be stored separately from the original corpus, but otherwise it should be integrated with the text of the corpus by using one of the formats we have seen in the class. (one-token-per-line csv or XML tags).
    - [ ] Briefly explain the format
    - [ ] Code used to prepare the data for annotation
    - [ ] Code used to convert the raw annotation into the final annotation
    - [ ] A brief discussion of how the annotation process went. 
        - [ ] Any challenges during the process that affected the quantity or quality of the annotation (not mentioned in the interannotator agreement)
- [ ] Make the above into a list of steps (from raw corpus to the final annotation), with links to relevant code and files

## Interannotator agreement study
rubric={accuracy:2,reasoning:3,writing:1}

- [ ] Identify an appropriate interannotator agreement measure based on the nature of your annotation, and justify the choice
- [ ] Calculate interannotator agreement
- [ ] Discuss whether you think your annotation is reliable or not
    - [ ] If the score is low, discuss why it is low, and what you might do to improve it
- [ ] Include a link to any code you used to calculate this interannotator agreement


## Experimenting with annotation options (Optional)
rubric={raw:2}

- [ ] Showing that you have tested options with the goal of improving annotation quality or annotation efficiency
- [ ] Things to try:
    - [ ] (for MTurk) different amounts of renumeration
    - [ ] (for MTurk) different numbers of annotators
    - [ ] (for MTurk) different levels of qualifications
    - [ ] Non-crowdsourced human annotation
- [ ] Compare different approaches in terms of time and quality (quality measured by interannotator agreement)


## Plan for the interface
rubric={reasoning:3,writing:2} 

- [ ] Provide 100-500 words about plans for the web interface, including justification of your choices
- [ ] Plan includes the following:
    - [ ] Have some kind of search functionality which will display text from the full corpus based on user input
    - [ ] Have an option that involves accessing annotations. This can be done in 2 ways:
        - [ ] Part of the search: When the annotation option is selected, limit the search result to only the annotated documents
        - [ ] Separated from the search: an independent sub-corpus
- [ ] Recommended: start coding the back-end part of the interface as soon as you finish planning

## Prompt completion
rubric={raw:4}

You should finish everything discussed above by 11:59pm Saturday, Mar 13th. If you were not able to complete it on time (in lieu of the typical 50% penalty) you will lose 1 points from your prompt completion score for each 12 hour period after the deadline. When you are done with a milestone (regardless of whether you are on time or late), one of your teammates MUST open an issue in your repo that says you are done. Any modification of the relevant documents in your milestone folder after you have opened this issue will likely result in losing all your prompt completion points.
