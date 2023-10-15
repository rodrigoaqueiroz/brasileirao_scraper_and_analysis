# Raspagem de dados e análise do campeonato brasileiro série A e B entre os anos 2012 e 2023 - Data scraping and analysis of the Brazilian Serie A and B championships between 2012 and 2023.
### English version above 
---

# Sumário

- [Habilidades](#habilidades)
- [Análises](#análises)
- [Como Rodar](#como-rodar)
- [Descobertas](#descobertas)
- [Contatos](#contatos)
---

# Habilidades

- Uso do scrapy para raspagem de dados do site da CBF;
- Utilização do scrapyrt para subir para funcionar como a API
- Análise explorativa dos dados;
- Uso de modelos de ML

---

# Análises

- Gráficos e mapas da distribuição dos times por estados e regiões;
- Verificar a porcentagem de gols que o artilheiro de cada edição fez;
- Descobri o melhor e o pior vencedor de cada competição, assim como o pior e o melhor décimo sétimo (o primeiro rebaixado);
- Criação de função genérica para descobrir o melhor e o pior de cada posição dos campeonatos;
- Modelo de ML para ver se com os dados é possível responder a hipótese de que não tomar gol é mais importante do que fazer;

---

# Como Rodar

Criar e ativar o ambiente virtual

```bash
$ python3 -m venv .venv
$ source .venv/bin/activate
```

Instalar as dependências do projeto

```bash
$ python3 -m pip install -r requirements.txt
```

Na pasta do projeto, rodar o scrapyrt:

```bash
$ scrapyrt
```

O comando scrapyrt erá usado para iniciar a API responsável por fornecer os dados para a análise. Os dados da API são obtidos por meio do Scrapy, e a porta padrão é a 9080. O terminal fornecerá a URL correspondente. Se tudo correr conforme o esperado, a URL 'http://localhost:9080/crawl.json?spider_name=cbf_spider&url=https://www.cbf.com.br/futebol-brasileiro/competicoes/campeonato-brasileiro-serie-a' estará funcionando e exibirá um JSON com os dados mais recentes do Campeonato Brasileiro Série A de 2023.

Além disso, disponibilizei o arquivo 'output.json' com os dados extraídos no dia 15/10/2023. Portanto, se preferir evitar a raspagem em tempo real e realizar a análise estática, o arquivo 'output.json' pode ser usado para esse fim.

O notebook contendo a análise dos dados está localizado na raiz do projeto com o título 'Analysis.ipynb'. Há também uma versão em inglês do mesmo notebook intitulada 'Analysis-EN.ipynb'

---

# Descobertas

- Dentro do período analisado, o Flamengo foi tanto o melhor quanto o pior vencedor. O melhor no ano de 2019, com 90 pontos, em que teve 78% dos pontos conquistado. Já o pior, foi no ano seguinte, onde foi campẽao com apenas 71 pontos (62% de aproveitamento)
- O botafogo está acima da média de dos campeões. No momento está com 70% de aproveitamento, então se mantiver essa média até o final do campeonato, é muito provável que se sagre o vencedor do Brasileirão Série A de 2023
- Gabriel Barbosa foi o artilheiro em dois anos dentor do período 2012~2023, em 2018 pelo Santos e 2019 pelo Flamengo.
- Cano foi o artilheiro de série que mais fez gols e também o que teve a maior porcentagem dos gols do time. Em 2022 ele fez 27 dos 63 gols do Fluminense, uma taxa de 42.85% dos gols do time no campeonato foram marcados pelo argentino.
- O time que foi rebaixado com mais pontos da série A para B foi a Portuguesa de 2013, fez 44 pontos. Já o pior décimo sétimo foi o Cruzeiro em 2019, com apenas 36 pontos.
- Dentro dos dados estudados, não há diferença significativa na diferença de gols marcos e gols sofridos para a colocação final do time na série A. Já na série B, mostrou que os gols marcados tem um peso maior.

---

# English Version

# Data scraping and analysis of the Brazilian Serie A and B championships between 2012 and 2023.

### Skills
- Use of scrapy for data scraping from the CBF website;
- Utilization of scrapyrt to set up as an API
- Exploratory data analysis;
- Use of ML models

### Analysis
- Graphics and maps of team distribution by states and regions;
- Checking the percentage of goals scored by each edition's top scorer;
- Discovered the best and worst winner of each competition, as well as the worst and best seventeenth-placed team (the first relegated team);
- Creation of a generic function to discover the best and worst in each position in the championships;
- ML model to see if the data can answer the hypothesis that not conceding a goal is more important than scoring one;

### How to Run
Create and activate the virtual environment

```bash
$ python3 -m venv .venv
$ source .venv/bin/activate
```

Install project dependencies

```bash
$ python3 -m pip install -r requirements.txt
```

In the project folder, run scrapyrt:

```bash
$ scrapyrt
```
The scrapyrt command will be used to start the API responsible for providing the data for analysis. The API data is obtained through Scrapy, and the default port is 9080. The terminal will provide the corresponding URL. If all goes well, the URL 'http://localhost:9080/crawl.json?spider_name=cbf_spider&url=https://www.cbf.com.br/futebol-brasileiro/competicoes/campeonato-brasileiro-serie-a' will be functional and will display a JSON with the latest data from the 2023 Brazilian Serie A.

Furthermore, I have provided the 'output.json' file with the extracted data on 15/10/2023. Therefore, if you prefer to avoid real-time scraping and perform static analysis, the 'output.json' file can be used for this purpose.

The notebook containing the data analysis is located in the project root with the title 'Analysis.ipynb'. There is also an English version of the same notebook entitled 'Analysis-EN.ipynb.'

### Discoveries

Within the analyzed period, Flamengo was both the best and worst winner. The best was in 2019, with 90 points, where they achieved 78% of the points. The worst was the following year, where they won with only 71 points (62% efficiency).
Botafogo is above the average of the champions. Currently, they have a 70% efficiency, so if they maintain this average until the end of the championship, it is very likely that they will win the 2023 Brazilian Serie A.
Gabriel Barbosa was the top scorer for two years within the 2012~2023 period, in 2018 for Santos and in 2019 for Flamengo.
Cano was the top scorer in the series who scored the most goals and also had the highest percentage of the team's goals. In 2022, he scored 27 out of 63 goals for Fluminense, accounting for 42.85% of the team's goals in the championship, scored by Cano.

The team that was relegated with the most points from Serie A to B was Portuguesa in 2013, with 44 points. The worst seventeenth-placed team was Cruzeiro in 2019, with only 36 points.
Within the studied data, there is no significant difference in the difference between goals scored and goals conceded for the team's final placement in Serie A. In Serie B, it was shown that the goals scored carry more weight.

---
# Contatos

<div style="display: flex; align-items: center; justify-content: space-between;">
  <div>
    <div style="display: flex; align-items: center;">
      <img src="./src/images/linkedin-logo.png" alt="linkedin-logo" style="width:20px; padding: 5px"/> <a href='https://www.linkedin.com/in/rodrigoandradequeiroz/'> https://www.linkedin.com/in/rodrigoandradequeiroz/
      </a>
    </div>
    <br/>
    <div style="display: flex;align-items: center;">
      <img src="./src/images/github-logo.png" alt="github-logo" style="width:20px; padding: 5px"/> 
      <a href='https://github.com/rodrigoaqueiroz'>
      https://github.com/rodrigoaqueiroz
      </a>
    </div>
    <br/>
    <div style="display: flex;align-items: center;">
      <img src="./src/images/email-logo.png" alt="email-logo" style= 'width:20px; padding: 5px'/></img>
      <a href="mailto:rodrigoandradequeiroz@gmail.com">rodrigoandradequeiroz@gmail.com</a>
    </div>

---
