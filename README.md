# AtivosB3

## Descrição

O objetivo do sistema é auxiliar um investidor nas suas decisões de comprar/vender ativos. Para tal, ele deve registrar periodicamente a cotação atual de ativos da B3 e também avisar, via e-mail, caso haja oportunidade de negociação.

Os seguintes requisitos funcionais são necessários:

- Obter periodicamente as cotações de alguma fonte pública qualquer e armazená-las, em uma periodicidade configurável para cada túnel, para consulta posterior.
- Expor uma interface web para permitir consultar os preços armazenados, configurar os ativos a serem monitorados e parametrizar os túneis de preço de cada ativo e periodicidade da checagem de cada ativo.
- Enviar e-mail para o investidor sugerindo Compra sempre que o preço de um ativo monitorado cruzar o seu limite inferior, e sugerindo Venda sempre que o preço de um ativo monitorado cruzar o seu limite superior.

## Linha de pensamento

1. Criação de um programa em python que coletasse as cotações da B3 (desenvolvido).
2. Armazenar os dados da consulta em um banco de dados (usarei o PostgreSQL) (Em desenvolvimento)
3. Webpage para mostrar e listar às ações (Em desenvolvimento)
4. Sistema de envio de e-mails (Não desenvolvido)

## Ferramentas usadas
1. [Python 3.10](https://docs.python.org/3/)
2. [Django 4](https://docs.djangoproject.com/pt-br/4.0/)
3. [PostgreSQL](https://www.postgresql.org/)
4. [Yahooquery](https://yahooquery.dpguthrie.com/)

## Como rodar
Para testar, execute o virtualenv com às dependências do projeto. Execute o servidor django, executando na pasta `BolsaB3` o comando `python manage.py runserver`.

Acesse `http://localhost:8000/`. Ao fim, você será direcionado a página inicial.

O arquivo com o código se encontra na pasta `coletaAtivos`, o nome do arquivo é `getacoes.py`.

## Outras maneiras

### A primeira

Ao longo do desenvolvimento pensei em formas diferentes de fazer a aplicação.

A principal linha de pensamento era fazer um scraping que coletasse as cotações e armazenasse no banco de dados. No entanto, até chegar na solução do [Yahooquery](https://yahooquery.dpguthrie.com/), passei por outras ferramentas.

A primeira forma que tentei e persisti por mais tempo foi utilizar as seguintes ferramentas em cojunto:

1. [Python 3.10](https://docs.python.org/3/)
2. [Django 4](https://docs.djangoproject.com/pt-br/4.0/)
3. [PostgreSQL](https://www.postgresql.org/)
4. [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
5. [Openpyxl](https://openpyxl.readthedocs.io/en/stable/)
6. [Pandas](https://pandas.pydata.org/)

Nesta linha de pensamento desenvolvi apenas o codigo [Python](https://docs.python.org/3/), que busca os dados na pagina `https://br.tradingview.com/markets/stocks-brazil/market-movers-all-stocks/`. E salva parte dos dados em uma tabela excel.

O problema aqui inicialmente foi conseguir uma fonte segura para coletar os dados. Após isso o problema passou a ser a coleta de todos os ativos da B3. Pois para poder coletar seria necessário clicar na opção `Carregar mais` na pagina. E durante o desenvolvimento o utilizando [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) não encontrei uma forma de resolver o problema.

O arquivo com o código se encontra na pasta `coletaAtivos`, o nome do arquivo é `tests.py`.

A segunda forma que tentei foi com as seguintes ferramentas:

1. [Python 3.10](https://docs.python.org/3/)
2. [Django 4](https://docs.djangoproject.com/pt-br/4.0/)
3. [PostgreSQL](https://www.postgresql.org/)
4. [Selenium](https://www.selenium.dev/)

Nesta linha de pensamento desenvolvi apenas o codigo com [Selenium](https://www.selenium.dev/), que busca os dados na pagina `https://br.tradingview.com/chart/`. No entanto, como o prazo estava apertado, preferi deixar de lado, mas ainda assim gastei parte do meu tempo analisando a estrutura do Selenium.

O arquivo com o código se encontra na pasta `coletaAtivos`, o nome do arquivo é `teste.py`. Ao longo do código sera possivel ver varias linhas comentadas(são tentativas).

## Extra

Ao longo do desenvolvimento criei ao tentar fazer o objetivo principal um historico de dados inserindo as datas de inicio e fim no próprio arquivo. Além do código do ativo. O arquivo com o código se encontra na pasta `coletaAtivos`, o nome do arquivo é `historico.py`.
