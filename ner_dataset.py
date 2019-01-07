import argparse
import codecs
import csv

from utils.sparql_queries import load_dataset, clean_dataset
from utils.sparql_queries import get_uri_suffix, exec_ner_query
import filepath_config as RDFfiles

CSV_DELIMITER = '|'
REPLACE_DELIMITER = ' '


def results_to_csv(results, filename):
    with codecs.open(filename, "w") as fp:
        writer = csv.writer(fp, delimiter=CSV_DELIMITER)
        header = ["entity", "entity_local_name", "label", "language", "type", "type_local_name"]
        writer.writerow(header)
        while results.hasNext():
            row = []
            try:
                next_result = results.next()
                entity = next_result.get("?entity").toString().replace(CSV_DELIMITER, REPLACE_DELIMITER)
                row.append(entity)
                row.append(get_uri_suffix(entity))
                label = next_result.get("?label")
                language = 'undefined'
                if label:
                    label = label.toString().replace(CSV_DELIMITER, REPLACE_DELIMITER)
                    label, language = split_string_lang(label)
                row.append(label)
                row.append(language)
                typ = next_result.get("?type").toString().replace(CSV_DELIMITER, REPLACE_DELIMITER)
                row.append(typ)
                row.append(get_uri_suffix(typ))
                writer.writerow(row)
            except Exception:
                continue


def split_string_lang(obj):
    splitted_obj = obj.replace('"', '').split('@')
    string = splitted_obj[0].replace('^^http://www.w3.org/2001/XMLSchema#string', '')
    language = 'undefined'
    if len(splitted_obj) > 1:
        language = splitted_obj[1]
    return string, language


def dbpedia_ner_dataset():
    dataset = load_dataset(RDFfiles.DBPEDIA_LABELS_EN)
    dataset = load_dataset(RDFfiles.DBPEDIA_TRANSITIVE_TYPES_EN)
    dataset = load_dataset(RDFfiles.DBPEDIA_LABELS_FR)
    dataset = load_dataset(RDFfiles.DBPEDIA_TRANSITIVE_TYPES_FR)
    results = exec_ner_query(dataset)
    results_to_csv(results, "ner_dbpedia.csv")


def main():
    argparse.ArgumentParser(prog='ner-dataset', description='Transform rdf dataset into a dataset for NER')
    clean_dataset()
    dbpedia_ner_dataset()
    clean_dataset()


if __name__ == "__main__":
    main()
