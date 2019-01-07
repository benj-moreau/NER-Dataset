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

# Run it !

```bash
python ner_dataset.py
```
