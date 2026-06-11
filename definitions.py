from dagster import Definitions, load_assets_from_dbt_project
from dagster_dbt import DbtCliResource
from pathlib import Path

# Caminho para o projeto dbt
DBT_PROJECT_DIR = Path(__file__).joinpath("..", "dbt_northwind").resolve()

dbt_resource = DbtCliResource(project_dir=os.fspath(DBT_PROJECT_DIR))

# Carrega os modelos dbt como ativos do Dagster
dbt_assets = load_assets_from_dbt_project(DBT_PROJECT_DIR)

defs = Definitions(
    assets=[dbt_assets],
    resources={
        "dbt": dbt_resource,
    },
)
