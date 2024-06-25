
# TCC Particionamento de entrada

## Todo código aqui foi adquirido originalmente de: [link](https://github.com/troclaux/tcc-machine-teaching)

## Baixar o arquivo .pkl, que contém os problemas e soluções no [link](https://drive.google.com/file/d/1CFEO6PHUJf5DDRLEZen9vCJ-_X97yM_Z/view?usp=sharing)

## Extrair os problemas e soluções do arquivo .pkl

```
python3 depickle_problems.py
```

```
python3 depickle_solutions.py
```

## Depois basta testar todas as soluções que foram extraídas

- Existem 3 tipos de critérios:
	- original
	- input
	- new_input

- Abrir o arquivo runner.py e definir as variáveis "problems" e "criteria"
	- Definir o número da variável "number_processes, que determina o número de processos simultaneos.

- Executar o seguinte comando:

```
python3 runner.py
```

## Para analisar os dados
- Execute o notebook aggregate_data.ipynb
