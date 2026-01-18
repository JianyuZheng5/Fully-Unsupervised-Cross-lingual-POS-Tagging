# Fully Unsupervised Cross-lingual POS Tagging

Official code and dataset release of the work, Unsupervised Cross-Lingual Part-of-Speech Tagging with Monolingual Corpora Only


## Step1: Constructing pseudo-parallel sentence pairs
Use [Lample et al.'s work](https://github.com/facebookresearch/UnsupervisedMT) to train the unsupervised neural machine translation(UNMT) systems.
- **Training corpus**: Randomly select 10 million sentences from the [CC-100 corpus](https://huggingface.co/datasets/statmt/cc100).
- **Validation & test set**: Use the corpus provided in the ```CCMatrix&GNOME (3k sentences)``` folder.

After completing the training of the UNMT systems, use the corpus in the ```Europarl corpus for UNMT (100k sentences)``` folder to translate the source language sentences into target language sentences.


## Step2: Generating the training instances for the target language
Follow the steps outlined in [Eskander et al.'s work](https://github.com/rnd2110/unsupervised-cross-lingual-POS-tagging), including ```Producing the Alignments```, ```Tagging the Source```, and ```Annotation Projection``` to generate the training instances for training POS taggers in the target languages.


## Step3: Calibrating the annotation results through the multi-source projection technique
Use the ```calibrate.py``` script to calibrate the POS-tagged results of each target language's words from the four source languages.


## Step4: Training a neural POS tagger for the target language
Follow the ```Training and Testing the POS model``` step outlined in [Eskander et al.'s work](https://github.com/rnd2110/unsupervised-cross-lingual-POS-tagging) to train the POS taggers for the target languages.



