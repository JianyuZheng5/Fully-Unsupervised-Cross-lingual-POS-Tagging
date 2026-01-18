# Fully Unsupervised Cross-lingual POS Tagging

Official code and dataset release of the work, Unsupervised Cross-Lingual Part-of-Speech Tagging with Monolingual Corpora Only


## Step1: Constructing pseudo-parallel sentence pairs
Use [Lample et al's work](https://github.com/facebookresearch/UnsupervisedMT) to train the unsupervised neural machine translation systems.
- for training corpus: randomly choose 10M sentences from [CC-100 corpus](https://huggingface.co/datasets/statmt/cc100);
- for validation & test set: the corpus in the folder "CCMatrix&GNOME (3k sentences )" we provide you;
