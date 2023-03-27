from cowsay import main

from dagster import asset

from shared import shared_function

@asset
def asset1(context):
    context.log.info(shared_function())
    context.log.info(f"Cowsay version {main.__version__}")
