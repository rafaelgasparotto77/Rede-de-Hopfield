import numpy as np # é usado para operações matemáticas e manipulção de arrays
import matplotlib.pyplot as plt # é usado para plotar os padrões como imagens.

class HopfieldNetwork: # Classe que implementa a Rede de Hopfield
    def __init__(self, num_neurons):
        self.num_neurons = num_neurons  # Inicializa a rede com o número especificado de neurônios
        self.weights = np.zeros((num_neurons, num_neurons)) # Cria uma matriz de pesos (inicialmente zero) para armazenar os pesos sinápticos

    def train(self, patterns):
        for p in patterns:  # Treina a rede de Hopfield com os padrões fornecidos
            p = p.reshape(-1, 1) # Reshape para garantir que o padrão é uma coluna
            self.weights += np.dot(p, p.T) # Atualiza a matriz de pesos usando a regra do produto externo
        self.weights[np.diag_indices(self.num_neurons)] = 0 # Remove auto-conexões (diagonal da matriz de pesos deve ser zero)

    def run(self, pattern, steps=5):
        pattern = pattern.copy()   # Iterativamente atualiza o padrão até convergir ou atingir o número máximo de passos
        for _ in range(steps):
            for i in range(self.num_neurons):
                raw_input = np.dot(self.weights[i], pattern)  # Calcula a entrada líquida para o neurônio i
                pattern[i] = 1 if raw_input >= 0 else -1 # Atualiza o estado do neurônio i usando a função de ativação de sinal
        return pattern

def add_noise(pattern, noise_level=0.2):   # Adiciona ruído ao padrão, invertendo o valor de aproximadamente `noise_level` percent de bits
    noisy_pattern = pattern.copy()
    num_noisy_bits = int(noise_level * len(pattern))
    noise_indices = np.random.choice(len(pattern), num_noisy_bits, replace=False)
    noisy_pattern[noise_indices] *= -1
    return noisy_pattern

def plot_pattern(pattern, title=""):
    pattern = -pattern # Inverte o padrão para visualização
    plt.imshow(pattern.reshape(9, 5), cmap='gray')  # Plota o padrão fornecido como uma imagem
    plt.title(title)
    plt.show()


patterns = np.array([ # Definindo os padrões de entrada (45 bits cada) para as imagens 1, 2, 3 e 4
    # Imagem 1
    [-1, -1, 1, 1, -1,
     -1, 1, 1, 1, -1,
     -1, -1, 1, 1, -1,
     -1, -1, 1, 1, -1,
     -1, -1, 1, 1, -1,
     -1, -1, 1, 1, -1,
     -1, -1, 1, 1,-1,
     -1, -1, 1, 1, -1,
     -1, -1, 1, 1, -1],

    # Imagem 2
    [1, 1, 1, 1, 1,
     1, 1, 1, 1, 1,
     -1, -1, -1, 1, 1,
     -1, -1, -1, 1, 1,
     1, 1, 1, 1, 1,
     1, 1, -1, -1, -1,
     1, 1, -1, -1, -1,
     1, 1, 1, 1, 1,
     1, 1, 1, 1, 1],

    # Imagem 3
    [1, 1, 1, 1, 1,
     1, 1, 1, 1, 1,
     -1, -1, -1, 1, 1,
     -1, -1, -1, 1, 1,
     1, 1, 1, 1, 1,
     -1, -1, -1, 1, 1,
     -1, -1, -1, 1, 1,
     1, 1, 1, 1, 1,
     1, 1, 1, 1, 1],

    # Imagem 4
    [1, 1, -1, 1, 1,
     1, 1, -1, 1, 1,
     1, 1, -1, 1, 1,
     1, 1, 1, 1, 1,
     1, 1, 1, 1, 1,
     -1, -1, -1, 1, 1,
     -1, -1, -1, 1, 1,
     -1, -1, -1, 1, 1,
     -1, -1, -1, 1, 1]
])

hopfield_net = HopfieldNetwork(num_neurons=45) # Inicializa a rede de Hopfield com 45 neurônios

hopfield_net.train(patterns) # Treina a rede com os padrões definidos

for idx, pattern in enumerate(patterns): # Simula transmissões com ruído
    for i in range(3):
        noisy_pattern = add_noise(pattern, noise_level=0.2)  # Adiciona ruído ao padrão original
        recovered_pattern = hopfield_net.run(noisy_pattern) # Recupera o padrão usando a rede de Hopfield

        print(f"Padrão Original {idx+1} - Transmissão {i+1}") # Exibe o padrão original, o padrão com ruído e o padrão recuperado
        plot_pattern(pattern, title="Padrão Original")
        plot_pattern(noisy_pattern, title="Padrão com Ruído")
        plot_pattern(recovered_pattern, title="Padrão Recuperado")

excessive_noise_pattern = add_noise(patterns[0], noise_level=0.6) # O que acontece com ruído excessivo
excessive_recovered_pattern = hopfield_net.run(excessive_noise_pattern)

print("Padrão Original com Ruído Excessivo")
plot_pattern(patterns[0], title="Padrão Original")
plot_pattern(excessive_noise_pattern, title="Padrão com Ruído Excessivo")
plot_pattern(excessive_recovered_pattern, title="Padrão Recuperado com Ruído Excessivo")