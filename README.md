# Rede-de-Hopfield
Projeto Prático - Rede de Hopfield para P2 de Redes Neurais

Este projeto implementa uma memória associativa utilizando uma rede de Hopfield com 45 neurônios para armazenar e recuperar padrões de imagem corrompidos durante a transmissão.

## Introdução

As redes de Hopfield são um tipo de rede neural recorrente introduzidas por John Hopfield em 1982. Elas são usadas principalmente para armazenamento associativo de padrões e para a recuperação desses padrões mesmo quando apresentados de maneira parcial ou corrompida.

### Arquitetura da Rede de Hopfield

- **Neurônios**: Cada neurônio está conectado a todos os outros neurônios, mas não há conexões de um neurônio para si mesmo (auto-conexões).
- **Estado**: Os neurônios possuem estados binários, geralmente representados como -1 e +1.
- **Peso das conexões**: A matriz de pesos `W` é  é simétrica (isto é, 𝑤𝑖𝑗=𝑤𝑗𝑖)e sem auto-conexões (wii= 0).
- **Função de ativação**: Utiliza-se uma função de ativação, como a função de sinal ou a tangente hiperbólica, para atualizar os estados dos neurônios.

### Funcionamento

1. **Aprendizagem**: Os padrões são armazenados ajustando os pesos das conexões entre os neurônios usando a regra do produto externo
2. **Recuperação**: Um padrão corrompido é dado como entrada. A rede atualiza iterativamente os estados dos neurônios até alcançar um estado estável (mínimo de energia), que idealmente corresponde ao padrão armazenado mais próximo.

### Implementação da Rede de Hopfield

Em rede_hopfield.py

### Simulação de Transmissão

A simulação foi feita para três transmissões de cada um dos quatro padrões, adicionando 20% de ruído a cada transmissão. O código em rede_hopfield.py inclui a função add_noise que corrompe cerca de 20% dos pixels, e a função plot_pattern para exibir os padrões.

### Resultados da Simulação

Cada simulação de transmissão exibe:
- **Padrão Original**: A imagem sem ruído.
-**Padrão com Ruído**: A imagem co
