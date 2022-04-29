from google.cloud import bigquery



def load_to_bigquery(df, dataset_id, table_id):
    '''Load a Pandas `DataFrame` to a Google `BigQuery table`

    ## Parameters
    - df: a local DataFrame
    - dataset_id: ID of a Google BigQuery dataset
    - table_id: ID of a Google BigQuery table
    '''
    client = bigquery.Client()

    dataset = client.dataset(dataset_id)
    
    job_config = bigquery.LoadJobConfig(
        autodetect=True,
        write_disposition='WRITE_APPEND',
        source_format=bigquery.SourceFormat.CSV
    )

    load_job = client.load_table_from_dataframe(df, 
        dataset.table(table_id), 
        job_config=job_config, 
        location='eu'
    )  # BigQueryAPI request    

    return load_job
