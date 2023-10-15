# Raspagem de dados e análise do campeonato brasileiro série A e B entre os anos 2012 e 2023 
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
$ python3 -m pip install -r dev-requirements.txt
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
