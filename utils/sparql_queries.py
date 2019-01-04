from jnius import autoclass
import shutil

STORE_PATH = 'rdf_store/tdb_dataset'

NER_QUERY = """SELECT ?entity ?label ?type
WHERE
{
      VALUES ?label_props { <http://www.w3.org/2000/01/rdf-schema#label> <http://www.w3.org/2004/02/skos/core#prefLabel> }
      OPTIONAL { ?entity ?label_props ?label } .
      ?entity <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> ?type
}
"""


def get_uri_suffix(typ):
    if '#' in typ:
        return typ.rsplit('#', 1)[-1]
    else:
        return typ.rsplit('/', 1)[-1]


def get_uri_prefix(typ):
    if '#' in typ:
        return '{}#'.format(typ.rsplit('#', 1)[0])
    else:
        return '{}/'.format(typ.rsplit('/', 1)[0])


def _exec_query(query, dataset):
    qexec = autoclass('org.apache.jena.query.QueryExecutionFactory').create(query, dataset)
    results = qexec.execSelect()
    return results


def exec_ner_query(dataset):
    results = _exec_query(NER_QUERY, dataset)
    return results
    formatter = autoclass('org.apache.jena.query.ResultSetFormatter')
    return formatter.toList(results).listIterator()


def load_dataset(filepath):
    dataset = autoclass('org.apache.jena.tdb.TDBFactory').createDataset(STORE_PATH)
    model = dataset.getDefaultModel()
    autoclass('org.apache.jena.tdb.TDBLoader').loadModel(model, filepath)
    return dataset


def clean_dataset():
    try:
        shutil.rmtree(STORE_PATH)
    except OSError as e:
        print ("Info: %s - %s." % (e.filename, "Already cleaned"))
