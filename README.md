# POC Great Expectations

# Motivação e Justificativa

Como os produtos de dados dependem da ingestão de dados para treinar modelos e fazer previsões, é fundamental ter um processo estruturado para validar a qualidade dos dados que estão sendo ingeridos. A ausência desse processo leva à má reputação dos produtos, uma vez que os próprios modelos são a primeira fonte de suspeita em um novo produto de dados. Como várias iniciativas dentro da empresa não estão validando os dados, a equipe de Engenharia de Dados (DE) e a equipe de Ciência de Dados (DS) foram solicitadas a verificar pipelines e modelos antes que a equipe de negócios avalie se a origem dos problemas está nos dados por conta própria.

Com uma alternativa de tornar essa validação automática e bem estruturada, já que conterá guias e definições fornecidas pela equipe de negócios, estamos testando uma biblioteca python chamada Great Expectations que pode resolver esses problemas de forma simples (do ponto de vista da codificação).

Vale ressaltar que esta biblioteca está sendo avaliada pela perspectiva de Engenharia de Dados, mas também pode se beneficiar ou ser útil para o lado da Modelagem de Dados. Portanto, os casos de uso abordados aqui são direcionados para DS, mas o material pode ser estendido para cobrir diferentes aspectos do DE, se necessário.

## Cenários & Ferramentas/Métodos

O teste do Great Expectations tem como objetivo validar os dados de um arquivo (fonte usada) antes do processo de ingestão. E para que esse cenário ocorra alguns pontos foram considerados:

    - Facíl implmentação  
    - Reaproveitamento de código
    - Legibilidade (código)
    - Manuteção descomplicada

O cenário utilizado foi baseado em uma validação onde alguns campos do arquivo deverá passar elas expectativas listadas abaixo:

* expect_table_columns_to_match_ordered_list: 
  Esperado que as colunas correspondam exatamente a uma lista especificada

* expect_column_values_to_not_be_null: 
  Esperado que os valores da coluna não sejam nulos. Para serem contados como uma exceção, os valores devem ser explicitamente nulos ou ausentes, como NULL no PostgreSQL ou np.NaN no pandas. Strings vazias não contam como nulas, a menos que tenham sido convertidas para um tipo nulo.

* expect_column_values_to_be_between 
  Esperado que as entradas da coluna estejam entre um valor mínimo e um valor máximo.

* expect_column_values_to_match_strftime_format
  Esperado que as entradas da coluna sejam strings representando uma data ou hora com um determinado formato.

* expect_column_values_to_be_in_type_list
  Espere que uma coluna contenha valores de uma lista de tipos especificados.      expect_column_values_to_be_in_type_list é uma expectativa de mapa de coluna para back-ends de coluna digitada e para PandasDataset, onde a coluna dtype fornece restrições inequívocas (qualquer dtype, exceto 'object'). Para colunas PandasDataset com dtype de 'object' expect_column_values_to_be_in_type_list verificará independentemente o tipo de cada linha.

### 📦 Execução (VSCODE)
```
1. Criar venv com comandeo python -m venv venv
2. Após clonar o projeto ativar venv *.\venv\Scripts\Activate.ps1*
3. selecione venv como seu interpretador python <(ctrl + shift + p e digite *Python: Select Interpreter*)>
4. Instalar as bibliotecas com o comando pip install -r requirements.txt
```
## 1.0 
Caso não esteja disponível o arquivo "ultimas-4-semanas-gasolina-etanol.csv" baixar no link informado *(Dados para teste Etanol Hidratado + Gasolina C das quatro últimas semanas)*

## ⚙️ 1.1
Executar arquivo src\data_validation.py para executar as seguintes validações:

  * - expect_table_columns_to_match_ordered_list
  * - expect_column_values_to_not_be_null
  * - expect_column_values_to_be_between
  * - expect_column_values_to_match_strftime_format
  * - expect_column_values_to_be_in_type_list

# 1.2
No final da execução dois arquivos seram gerados:
 *data\gx_cheackpoint_output\gx_full_log.json*
 *data\gx_cheackpoint_output\gx_resume_log.csv*

## Conclusão
```
Great Expectations possui uma barreira quase nula de utilização e implementação. Com o básico da linguagem python você consegue validar seus dados de forma rápida e eficaz sem que seja preciso escrever várias linhas de código para um um ou mais arquivos. Por ser uma biblioteca open source a comunidade está sempre atualizando os conteúdos e criando novas "expectativas" que podem ser utilizadas em diversos cenários.
```
### 📄 Mais informações ###

## Lista de expectations para consumir
*https://greatexpectations.io/expectations*

## Fontes usadas
*https://qxf2.com/blog/data-validation-great-expectations-real-example/*
*https://docs.greatexpectations.io/docs/tutorials/quickstart/*

## Dados para teste Etanol Hidratado + Gasolina C das quatro últimas semanas & Metadados
*https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/shpc/qus/ultimas-4-semanas-gasolina-etanol.csv*
*Arquivo de metadados localizado na pasta data/metadados-precos-combustiveis.pdf*

## Estudo de comparações entre Great Expectations X Pandera
*https://endjin.com/blog/2023/03/a-look-into-pandera-and-great-expectations-for-data-validation*

## Vizualizando a strutura do JSON gerado
*https://jsonviewer.stack.hu/*# Data-quality-Great-Expectations
