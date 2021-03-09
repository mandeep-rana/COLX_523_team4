# COLX 523 - Advanced Corpus Linguistics

# Milestone 3                   

## Repo and data storage
rubric={mechanics:2}
                                                                                 
[ ] Store annotations together with the main corpus in a sensible way, and make sure to document the relationship between the two.

## Annotation + explanation + code
rubric={raw:3,accuracy:2,quality:1,reasoning:2, writing:1}

[ ] Finish an annotation of roughly the size promised in the previous milestone (or larger), including:
    [ ] Link to any intermediary files produced during the annotation process (e.g. csvs downloaded from mechanical turk, excel documents for individual annotators, etc.)
    [ ] Document what the intermediary files are
    [ ] Link to the final version of the annotation. DO NOT include information from multiple annotators, but a single 'best' annotation
    [ ] If there is an easy mapping from a "document" in the corpus to a single annotation, the annotation can be stored separately from the original corpus, but otherwise it should be integrated with the text of the corpus by using one of the formats we have seen in the class. (one-token-per-line csv or XML tags).
    [ ] Briefly explain the format
    [ ] Code used to prepare the data for annotation
    [ ] Code used to convert the raw annotation into the final annotation
    [ ] A brief discussion of how the annotation process went. 
        [ ] Any challenges during the process that affected the quantity or quality of the annotation (not mentioned in the interannotator agreement)


Make sure it is easy for us to identify exactly the steps that you took to get from your raw corpus to your final annotation (a list of steps, with links to relevant code and files, would be ideal).

## Interannotator agreement study
rubric={accuracy:2,reasoning:3,writing:1}

Identify an appropriate interannotator agreement measure based on the nature of your annotation (justify your choice!), calculate interannotator agreement, and discuss whether you think your annotation is reliable or not. If your annotator agreement is low, please talk about why it is low, and what you might do to improve it. Include a link to any code you used to calculate interannotator agreement. Note if your agreement is low and it appears that it is low because you didn't take steps to ensure quality, you will lose points here even if the results of the study are accurate. 

## Experimenting with annotation options (Optional)
rubric={raw:2}

You can get bonus points in this milestone by showing that you have tested options with the goal of improving annotation quality or annotation efficiency. For example, if you used Mechanical Turk, you could try different amounts of renumeration, different numbers of annotators, different levels of qualitifications, or even try an non-crowdsourced human annotation and see how things compare in terms of time it takes to complete the annotation or the quality of the annotation (as measured by interannotator agreement).


## Plan for the interface
rubric={reasoning:3,writing:2} 

You will be building an web interface for your corpus, with the goal of allowing others to learn about your corpus and your annotation in an interactive way. This will involve your user filling out a small HTML form (including button(s) and/or text box(es)) in a browser and then having this information be passed to a back-end Python script which accesses the corpus and/or annotation and prepares information in the form of text strings and/or numbers (you could also potentially generate images such as graphs but this is definitely optional!) to be passed back to the web browser for display to the user.

We have the following two expectations:

- you should have some kind of search functionality which will display text from your full corpus based on user input
- you should have an option that involves accessing your annotation in some way. Since your annotation won't cover your whole corpus, it is okay if this is somewhat separate from your main search functionality or (if it is part of the search) that accessing your annotations limits your search to those documents you have annotated. 

Otherwise, you are free to do what you like. Remember that your fellow students will be playing around with your interface and giving your a peer review score. Provide between 100 and 500 words about your plans for your interface, including a bit of justification of your choices. You will not be stricly held to this plan, but you'll need to explain deviations from it in the next milestone.

Though there are no code requirements for this part of this milestone, we recommend you start coding the back-end part of this as soon as you finish your plan.

## Prompt completion
rubric={raw:4}

You should finish everything discussed above by 11:59pm Saturday, Mar 13th. If you were not able to complete it on time (in lieu of the typical 50% penalty) you will lose 1 points from your prompt completion score for each 12 hour period after the deadline. When you are done with a milestone (regardless of whether you are on time or late), one of your teammates MUST open an issue in your repo that says you are done. Any modification of the relevant documents in your milestone folder after you have opened this issue will likely result in losing all your prompt completion points.
