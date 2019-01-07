# NER-Dataset
A column oriented dataset that can be used for named-entity recognition.

# Installation

Assuming you already have `python 2.7`, `pip 9`, `java 11`,

Download [jena 3.9](https://jena.apache.org/download/index.cgi) and update classpath:

```bash
export CLASSPATH=${CLASSPATH}:YOUR-JENA-DIR-PATH/lib/*
```

Create a new virtualenv:

install Cython

```bash
python -m pip install --upgrade cython
```

Install dependencies with pip:

```bash
pip install -r requirements.txt
```

# Yago dataset

Files from YAGO needs to get some kind of preprocessed, where non-unicode characters are replaced in order for Jena to accept the data.
Put yago files in a folder. go in this directory and run:

Mac:

`sed -i '' -e 's/|/-/g' ./* && sed -i '' -e 's/\\\\/-/g' ./* && sed -i '' -e  's/–/-/g' ./*`

Windows or Linux:

`sed -i 's/|/-/g' ./* && sed -i 's/\\\\/-/g' ./* && sed -i 's/–/-/g' ./*`

# Run it !

```bash
python ner_dataset.py
```
