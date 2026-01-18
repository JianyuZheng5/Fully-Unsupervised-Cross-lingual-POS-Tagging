# Fully Unsupervised Cross-lingual POS Tagging

Official code and dataset release of the work, Unsupervised Cross-Lingual Part-of-Speech Tagging with Monolingual Corpora Only


## Step1: Constructing pseudo-parallel sentence pairs
Use [Lample et al's work](https://github.com/facebookresearch/UnsupervisedMT) to train the unsupervised neural machine translation(UNMT) systems.
- **Training corpus**: Randomly select 10 million sentences from the [CC-100 corpus](https://huggingface.co/datasets/statmt/cc100).
- **Validation & test set**: Use the corpus provided in the "CCMatrix&GNOME (3k sentences)" folder.
After fininshing the training of these UNMT systems, use the corpus in the folder "" we make up to translate the source language sentences parallel with each other to the target languages;
