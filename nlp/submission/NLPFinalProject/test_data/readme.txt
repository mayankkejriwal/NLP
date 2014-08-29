This folder contains the test data used in the project. This test data was also part of the 'Wiki' corpus in the GLOW project
(Ratinov et al.; cited in the paper as well). Since the method is unsupervised, we did not take their training
data, just the test. The deprec folder should be ignored.
The gold folder contains the ground truth. Surface forms that don't have a link to wikipedia are designated
*null* in the gold standard. raw_text contains the input files to our framework. surface_links contains the
wikipedia links and out links/page for each surface mention (returned by the Stanford NER run on raw_text files)
in the raw text file, and surface_text contains the corresponding wikipedia text for those surface links.
Note that all files are numbered correspondingly. This is how we connect the dots across the various folders.