from pathlib import Path

import dagfactory


BASE_DIR = Path('./dags')

for path in BASE_DIR.glob(r'**/*'):
    if path.name.endswith("_dag.yml"):
        dag_factory = dagfactory.DagFactory(path.absolute())
        dag_factory.clean_dags(globals())
        dag_factory.generate_dags(globals())
