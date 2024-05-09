import great_expectations as gx
import pandas as pd
import json

def valida_dados_gx():

    # Set up
    context = gx.get_context()

    #lista de colunas
    column_list = [
        "Regiao - Sigla",
        "Estado - Sigla",
        "Municipio",
        "Revenda",
        "CNPJ da Revenda",
        "Nome da Rua",
        "Numero Rua",
        "Complemento",
        "Bairro",
        "Cep",
        "Produto",
        "Data da Coleta",
        "Valor de Venda",
        "Valor de Compra",
        "Unidade de Medida",
        "Bandeira"
    ]

    type_list = [
      "INTEGER",
      "integer",
      "int",
      "int_",
      "int8",
      "int16",
      "int32",
      "int64",
      "uint8",
      "uint16",
      "uint32",
      "uint64",
      "INT",
      "TINYINT",
      "BYTEINT",
      "SMALLINT",
      "BIGINT",
      "IntegerType",
      "LongType",
      "DECIMAL",
      "FLOAT",
      "float" ]
    
    df_comb_br = pd.read_csv(r".\data\ultimas-4-semanas-gasolina-etanol.csv", sep=";")
    
    #lambda usada ara converter o valor BR ',' para USA '.'
    df_comb_br["Valor de Venda"] = df_comb_br['Valor de Venda'].apply(lambda x: float(x.replace(',','.')))

    validator = context.sources.pandas_default.read_dataframe(dataframe=df_comb_br)

    # Cria expectativas
    validator.expect_table_columns_to_match_ordered_list(column_list=column_list, result_format="COMPLETE")
    validator.expect_column_values_to_not_be_null(column="Valor de Venda", result_format="COMPLETE")
    validator.expect_column_values_to_be_between(column="Valor de Venda", min_value=1, max_value=10, result_format="COMPLETE")
    validator.expect_column_values_to_be_in_type_list(column="Valor de Venda", type_list=type_list, result_format="COMPLETE")
    validator.expect_column_values_to_match_strftime_format(column="Data da Coleta",strftime_format="%d/%m/%Y", result_format="COMPLETE")

    # Validate data
    checkpoint = gx.checkpoint.SimpleCheckpoint( 
        name="combustivel_data_checkpoint",
        data_context=context,
        validator=validator,
    )


    checkpoint_result = checkpoint.run()
    checkpoint_result_json = checkpoint_result["run_results"]

    if checkpoint_result.success == True:
        print("Dados prontos para proxima etapa")

    else:
        print("Ocorreu alguma divergencia na validação, favor consultar arquivo de log")


    str_jason = str(checkpoint_result_json)
    str_jason = str_jason.replace("'","\"")[120:-1]

    json_read = json.loads(str_jason)

    # Serializar json
    json_object = json.dumps(json_read, indent=4)
    
    # Salva log completo em JSON
    with open(".\data\gx_cheackpoint_output\gx_full_log.json", "w") as outfile:
        outfile.write(json_object)

    
    # Cria log resumido usando pandas (CSV)
    df_resulme_log = pd.DataFrame()

    json_teste = json_read['validation_result']['results']
    
    for gx_info in json_read['validation_result']['results']:

        df = pd.DataFrame()
        df['expectation'] = [str(gx_info['expectation_config']['expectation_type'])]
        df['status_expectation'] = [str(gx_info['success'])]
        df_resulme_log = pd.concat([df_resulme_log, df], ignore_index=True)

    df_resulme_log['data_run'] = json_read['validation_result']['meta']['run_id']['run_time']
    df_resulme_log['element_count'] = json_read['validation_result']['results'][4]['result']['element_count']
    
    #json_log = json.dumps(df_resulme_log, indent=4)    
    json_log = df_resulme_log.to_json(orient='index')
    print(json_log)
    # Salva arquivo CSV
    df_resulme_log.to_csv('.\data\gx_cheackpoint_output\gx_resume_log.csv',sep=';', header=True, index=False)


if __name__ == "__main__":
    valida_dados_gx()