Rota Inteligente: Otimização de Entregas com Algoritmos de IA

1. Descrição do Problema e Desafio

A empresa Sabor Express, um pequeno delivery de alimentos localizado na região central da cidade, enfrenta dificuldades para realizar entregas eficientes durante horários de pico (almoço e jantar). As rotas são definidas manualmente pelos entregadores, o que resulta em trajetos ineficientes, atrasos, aumento do consumo de combustível e insatisfação dos clientes.

O desafio consiste em desenvolver uma solução baseada em Inteligência Artificial capaz de sugerir rotas ótimas para os entregadores, considerando múltiplos pontos de entrega e restrições urbanas. A cidade será modelada como um grafo, onde os nós representam bairros ou locais de entrega e as arestas representam ruas, com pesos associados à distância ou tempo estimado.

2. Objetivos do Projeto

Minimizar o tempo e a distância total das entregas;

Reduzir custos operacionais (combustível e tempo);

Aumentar a eficiência logística da empresa;

Melhorar a satisfação dos clientes;

Demonstrar a aplicação prática de algoritmos clássicos de IA.


3. Abordagem Adotada

A solução foi dividida em duas partes principais:

1. Otimização de Rotas: utilização de algoritmos de busca em grafos para encontrar o menor caminho entre o ponto de origem (restaurante) e os pontos de entrega.


2. Agrupamento de Entregas (Clustering): aplicação de aprendizado não supervisionado para agrupar entregas próximas geograficamente, facilitando a distribuição eficiente entre entregadores.



Essa abordagem permite lidar tanto com entregas individuais quanto com cenários de alta demanda.

4. Algoritmos Utilizados

4.1 Algoritmos de Busca em Grafos

A*: utilizado para encontrar o menor caminho entre dois pontos, combinando custo real e heurística (distância estimada até o destino).

BFS (Busca em Largura): empregado para comparação, garantindo o menor número de arestas.

DFS (Busca em Profundidade): utilizado para exploração do grafo e análise estrutural.


4.2 Clustering

K-Means: utilizado para agrupar pontos de entrega próximos, criando zonas eficientes de atendimento para cada entregador.


5. Representação do Problema

A cidade foi representada como um grafo ponderado, onde:

Nós: bairros ou endereços de entrega;

Arestas: ruas conectando os pontos;

Pesos: distância ou tempo médio de deslocamento.


Para fins didáticos e acadêmicos, o grafo utilizado neste projeto é uma abstração simplificada da cidade, representada por nós identificados por letras (A, B, C, etc.). Essa modelagem permite validar, testar e comparar o funcionamento dos algoritmos de busca e otimização de forma clara e objetiva.

Um diagrama do grafo pode ser gerado via código ou representado por imagem estática presente na pasta /docs do repositório.

6. Análise dos Resultados

A aplicação do algoritmo A* demonstrou maior eficiência em comparação com BFS e DFS, reduzindo significativamente o tempo total das rotas. O uso do K-Means permitiu agrupar entregas de forma estratégica, diminuindo a distância percorrida por cada entregador.

Métricas Avaliadas

Distância total percorrida;

Tempo estimado de entrega;

Número de entregas por rota.


7. Limitações e Sugestões de Melhoria

Limitações:

Não considera tráfego em tempo real;

Pesos das arestas são estáticos;

Número fixo de clusters.


Sugestões de Melhoria:

Integração com APIs de trânsito em tempo real;

Uso de algoritmos genéticos ou aprendizado por reforço;

Ajuste dinâmico do número de clusters.


8. Estrutura do Repositório

/rota-inteligente
 ├── src/
 │   ├── graph.py
 │   ├── search_algorithms.py
 │   ├── clustering.py
 │   └── main.py
 ├── data/
 │   └── entregas.csv
 ├── docs/
 │   └── diagrama_grafo.png
 ├── README.md

9. Instruções de Execução

1. Clonar o repositório;


2. Instalar as dependências:

pip install -r requirements.txt


3. Executar o projeto:

python src/main.py



10. Referências

UPS ORION – Wired (2013);

Medium – Optimizing Logistics: Clustering and MILP;

ResearchGate – AI-Powered Route Optimization;

Kardinal.ai – Case Study Fresh Product Delivery.
