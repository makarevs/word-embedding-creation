# Creation of word embeddings using neural networks

The code in this project is used to read text and create a file with the word embeddings. I has been adopted from Medium paper with code reference, corrected to work, and equipped with the alternative (to article) description of how it wors in [doc\algo_explained.md](doc\algo_explained.md).

The corresponding Medium paper by author of original program is:

Bujokas, E. (2020, May 30). Creating Word Embeddings: Coding the Word2Vec Algorithm in Python using Deep Learning. Medium. https://towardsdatascience.com/creating-word-embeddings-coding-the-word2vec-algorithm-in-python-using-deep-learning-b337d0ba17a8


# Activating the virtual environment

For the creation of virtual environments (VE) anaconda is used. You can download anaconda via here: 
https://www.anaconda.com/distribution/

After installing anaconda into your system follow the steps bellow to work in a virtual environment.

Creation of the VE:
```
conda create python=3.7 --name embedding
```

Activating the VE:
```
conda activate embedding
```

Installing all the packages from the **requirements.txt** file to the virtual environment:
```
pip install -r requirements.txt
```
... or, alternatively, and to ensure program works, using the provided yaml config as:
```
conda env create -f embedding.yml
```

If you are using Microsoft Visual Studio code there may be some additional pop ups indiciating that some packages should be installed (linter or ikernel).
