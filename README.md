### # Academia-capgemini

- Esse é um desafio proposto pela empresa Capgemini com o objetivo de selecionar novos talentos.
    - O desafio foi dividido em duas etapas:
        - 1 Parte -> Uma calculadora de alcance de anúncio online:
        > Foi definido os seguintes critérios fictícios para desenvolver a calculadora de alcance de anúncio:
Baseados em dados de análise de anúncios anteriores, a agência tem os seguintes dados:
        > - 30 pessoas visualizam o anúncio original (não compartilhado) a cada R$ 1,00 investido.
        > - A cada 100 pessoas que visualizam o anúncio 12 clicam nele.
        > - A cada 20 pessoas que clicam no anúncio 3 compartilham nas redes sociais. 
        > - o mesmo anúncio é compartilhado no máximo 4 vezes em sequência
        > (1ª pessoa -> compartilha -> 2ª pessoa -> compartilha - > 3ª pessoa -> compartilha -> 4ª pessoa)
        > - Cada compartilhamento nas redes sociais gera 40 novas visualizações.

        > - O objetivo é entregar um script em qualquer linguagem que receba o valor investido em reais e retorne uma projeção aproximada da quantidade máxima de pessoas que visualizaram o anúncio ( considerando o anúncio original + os compartilhamentos )
        - 2 Parte -> Um sistema de cadastro de anúncios.
        > - Criar um sistema que permita o cadastro de anúncios. contendo os seguintes dados:
        >   -    `Nome do anúncio`
        >   -    `Cliente`
        >   -    `Data de início`
        >   -    `Data de término`
        >   -    `Investimento por dia`
        > - O sistema fornecerá os relatórios de cada anúncio contendo:
        >   -    `Valor total investido`
        >   -    `Quantidade máxima de visualizações`
        >   -    `quantidade máxima de cliques`
        >   -    `quantidade máxima de compartilhamentos`


### # Solucão

- Os scripts foram feitos em python porque foi a linguagem mais fácil que achei para resolver esse desafio. Para a solução destes utilizei o curso [Python para zumbis](https://www.youtube.com/watch?v=YO58tXerKDc&list=PLUukMN0DTKCtbzhbYe2jdF4cr8MOWClXc) por ser gratis e utilizei pesquisas no site [Stackoverflow](https://stackoverflow.com/).

### Primeira Parte
- Foi feito um script simples estrutural com o nome de `calculadora.py`. Usei o seguinte raciocínio para resolver o problema:
    - Multipliquei o valor investido por 30 para obter a quantidade de visualização inicial.
    - Calculei a porcentagem de pessoas que visualizavam o anúncio e clicavam, dessa forma eu consegui ter um valor aproximado de cliques para uma quantidade menor de visualização.
    - Calculei a porcentagem de compartilhamentos por cliques vezes 4 para obter a quantidade de compartilhamentos.
    - Multipliquei a quantidade de compartilhamentos do resultado acima por 40 para obter a quantidade de novas visualizações.
    - Somei a quantidade de visualizações do anúncio original com as novas visualizações para obter a quantidade total de visualização.

- Executando o script.
```
$ python3 calculadora.py
```
#### Observação :
-   Para informar o valor investido utilize o caracter '.' para valores fracionados.

### Segunda Parte
- Nesse script apanhei um pouco para fazer, e com pesquisas identifiquei que a forma mais "fácil" de se fazer era construindo a lógica de forma modular usando funções. Criei pequenas funções para os calculos de: 
> - Calculo de data : `calcData( )`
> - Calculo do valor investido : `calcValorInvestido( )`
> - Calculo de vizualização original : `calcVisualizacaoOriginal( )`
> - Calculo de cliques : `calcCliques( )`
> - Calculo de compartilhamento : `calcCompartilhamento( )`
> - Calculo de novas visualizações : `calcNovasVisualizacoes( )`
> - Calculo de Total de visualizações : `calcVisualizacaoTotal( )`
> - Função de cadastro : `funcaoCasdastro( )`
> - Função de relatório : `funcaoRelatorio( )`
> - Função de menu : `menu( )`

- O raciocínio para esse problema é o mesmo da Primeira parte, a única coisa de diferente foi a separação por função e modulos novos para casdastro e relatório.
- Para cadastro e relatório utilizei a escrita em um arquivo no formato json `data.json`. Nesse arquivo é armazenado os cadastros de clientes. Optei por arquivo.json porque tive dificuldade para resolver com vetor.
- No relatório a busca esta sendo feito somente pelo nome do cliente porque não consegui filtrar pela data.

- Executando o script
```
$ python3 sistemaDeCadastro.py
```
#### Observação :
- O preenchimento da data deve seguir o formato `YYYY-MM-DD`
- O cadastro e o relatório precisa do arquivo.json com a estrutura definida. Nesse arquivo que esta no repositório já tem o arquivo com a estrutura pronta. Ele precisa estar na mesma pasta que o script de execução.