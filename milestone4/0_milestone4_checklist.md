# COLX 523 - Advanced Corpus Linguistics

# Milestone 4                   


## Repo and data storage
rubric={mechanics:2}

- [ ] Should NOT include the docker image in your repo, however you should include everything needed to build it. See below for instructions about docker image submission.

## Python back-end (Derek & Mia)
rubric={accuracy:4,quality:4,efficiency:2}

Derek:

- [ ] Submit code in .py format that implements functionality of your interface
- [ ] The back end script should be a python backend (FastAPI or similar) that responds http 'GET' requests from a browser
- [ ] The code must include:
    - [ ] Some kind of search functionality which will display text from the corpus based on user input
    - [ ] An option that involves accessing annotation in some way
- [ ] If the script did not follow what has been discussed in milestone 3, include a justification of the new choice
- [ ] High code quality satisfying:
    - [ ] Code is broken into functions (perhaps even different .py files)
    - [ ] Structure of the code should be crystal clear
    - [ ] Try to avoid iterating over entire corpus from scratch for each query, instead do appropriate loading/preprocessing of the corpus when the webserver loads
- [ ] May choose to use non-standard packages or even Elasticsearch

Mia:

- [ ] Document code thoroughly

## HTML/javascript front-end (Mandeep)
rubric={raw:3,reasoning:2,writing:1,viz:1}

Mandeep:

- [ ] An html document with at least one html form which users use to set up their query
    - [ ] Appropriate form elements for the query
    - [ ] Interface should look clean and clear on how to use it
- [ ] Any javascript requried carry out the communication between the html and the python back end, in a .js document
- [ ] A css document including at least one css class that is used in the output of your interface
- [ ] A separate .txt text file providing documentation of the front end
    - [ ] Discuss what the front end interface does, at a technical level

## Improved interface (Optional)
rubric={raw:2}

You can get bonus by going above and beyond the basic requirements in ways such as  

- Options for corpus exploration that incorporate advanced information retrieval techniques
- A standout visual experience involving extensive use of additional html/javascript/css elements not discussed in class. You might seek out templates for this purpose.
- An increased level of interactivity, going beyond just a single call to the backend for a single results page
- Incorporation of NLP elements, e.g. some kind of machine learning classifier trained on your annotated data


## Dockerization and peer review instructions (Lisa & Mia)
rubric={raw:3,reasoning:2,writing:1}

Up to discussion:

- [ ] Prepare the interface and corpus for distribution
- [ ] Package back end, front end code, and the corpus into a docker image
- [ ] Should be able to run the image and access the interface via a browser (using localhost)
- [ ] Test the docker image thoroughly before uploading
- [ ] Outside docker image include:
    - [ ] Include some fixed instructions in .md format for how to get things working
    - [ ] Include the docker commands to run and the url for the browser (and the port)
    - [ ] A specific list of things your peer reviewers should try with the interface when they are testing it
- [ ] Upload both the instruction and the image to the google drive below:

Username: colx523project
Password: COLX523-submission

- [ ] Include team number in the file names of instruction and image

## Prompt completion
rubric={raw:4}

You should finish everything discussed above by 11:59pm *Sunday*, Mar 21st (Note that this milestone is due Sunday rather than Saturday, though of course you're welcome to finish early!). If you were not able to complete it on time (in lieu of the typical 50% penalty) you will lose 1 points from your prompt completion score for each 12 hour period after the deadline. When you are done with a milestone (regardless of whether you are on time or late), one of your teammates MUST open an issue in your repo that says you are done. Any modification of the relevant documents in your milestone folder after you have opened this issue will likely result in losing all your prompt completion points.
