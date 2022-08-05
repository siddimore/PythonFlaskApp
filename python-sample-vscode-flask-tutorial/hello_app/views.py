from datetime import datetime
from flask import Flask, render_template
from .table_accessor import create_table_client, get_single_entity_by_partition_key
from .keyvault_accessor import get_secret

from . import app

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/contact/")
def contact():
    return render_template("contact.html")

@app.route("/hello/")
@app.route("/hello/<name>")
def hello_there(name = None):
    # Get ConnectionString from KeyVault
    table_connection_string = get_secret(
        "pav2-connection-str",
        "https://accl-staging-billing-kv.vault.azure.net/")

    print(table_connection_string)

    result=get_single_entity_by_partition_key(table_connection_string, "UsageReporting", "000d9670-5f70-4aa2-93aa-b9109c93defe")
    print(result)
    retrieved_result=result['PartitionKey'] + result['RowKey'] + result['ResourceUri']

    return render_template(
        "hello_there.html",
        name=retrieved_result,
        date=datetime.now()
    )

@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")
