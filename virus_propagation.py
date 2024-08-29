import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Slider, Button

def calcular_entropia(probabilidades):
    probabilidades = np.array(probabilidades)
    return -np.sum(probabilidades * np.log2(probabilidades + 1e-9))

def calcular_entropia_virus(population):
    probs = [np.mean(population == state) for state in [0, 1, 2, 3]]
    return calcular_entropia(probs)

# Função para criar a animação com propagação do vírus
def run_simulation(taxa_infeccao):
    # Configurações iniciais
    grid_size = (100, 100)  # Aumentando o tamanho do grid
    population = np.zeros(grid_size[0] * grid_size[1])
    infected_indices = np.random.choice(grid_size[0] * grid_size[1], 100, replace=False)
    population[infected_indices] = 1

    # Lista para armazenar a entropia em cada iteração
    entropias = []

    # Configurar a figura para a animação, slider e botões
    fig, ax = plt.subplots()
    plt.subplots_adjust(left=0.25, bottom=0.5)  # Ajustar para espaço dos controles
    im = ax.imshow(population.reshape(grid_size), cmap='viridis', vmin=0, vmax=3)
    ax.set_title('Simulação da Propagação de Vírus', fontsize=16)
    
    # Descrição das cores na legenda
    colorbar = fig.colorbar(im, ax=ax)
    colorbar.set_ticks([0, 1, 2, 3])
    colorbar.set_ticklabels(['Suscetível', 'Infectado', 'Recuperado', 'Óbito'])

    # Adicionar sliders e botões
    ax_slider_infeccao = plt.axes([0.25, 0.35, 0.65, 0.03], facecolor='lightgoldenrodyellow')
    taxa_infeccao_slider = Slider(ax_slider_infeccao, 'Taxa de Infecção', 0, 0.1, valinit=taxa_infeccao)
    
    ax_slider_recuperacao = plt.axes([0.25, 0.25, 0.65, 0.03], facecolor='lightblue')
    taxa_recuperacao_slider = Slider(ax_slider_recuperacao, 'Taxa de Recuperação', 0, 0.5, valinit=0.2)
    
    ax_slider_fatalidade = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor='lightcoral')
    taxa_fatalidade_slider = Slider(ax_slider_fatalidade, 'Taxa de Fatalidade', 0, 0.1, valinit=0.03)

    # Botões de Play/Pause e Reset
    ax_play = plt.axes([0.25, 0.05, 0.1, 0.04])
    ax_pause = plt.axes([0.35, 0.05, 0.1, 0.04])
    ax_reset = plt.axes([0.45, 0.05, 0.1, 0.04])
    
    button_play = Button(ax_play, 'Play')
    button_pause = Button(ax_pause, 'Pause')
    button_reset = Button(ax_reset, 'Reset')
    
    # Variáveis de controle
    is_paused = False

    def update(frame):
        nonlocal population
        if not is_paused:
            # Novas infecções
            new_infections = np.random.choice(grid_size[0] * grid_size[1], int(grid_size[0] * grid_size[1] * taxa_infeccao_slider.val), replace=False)
            population[new_infections] = np.where(population[new_infections] == 0, 1, population[new_infections])
            
            # Recuperações
            infected_indices = np.where(population == 1)[0]
            recovered_indices = np.random.choice(infected_indices, int(len(infected_indices) * taxa_recuperacao_slider.val), replace=False)
            population[recovered_indices] = 2

            # Fatalidades
            fatalidade_indices = np.random.choice(infected_indices, int(len(infected_indices) * taxa_fatalidade_slider.val), replace=False)
            population[fatalidade_indices] = 3
            
            # Calcular e armazenar a entropia
            entropia = calcular_entropia_virus(population)
            entropias.append(entropia)

            # Atualizar a imagem
            im.set_data(population.reshape(grid_size))
            
        return [im]

    def play(event):
        nonlocal is_paused
        is_paused = False

    def pause(event):
        nonlocal is_paused
        is_paused = True

    def reset(event):
        nonlocal population, entropias
        population = np.zeros(grid_size[0] * grid_size[1])
        infected_indices = np.random.choice(grid_size[0] * grid_size[1], 100, replace=False)
        population[infected_indices] = 1
        entropias.clear()  # Limpar a lista de entropias ao resetar
        im.set_data(population.reshape(grid_size))
        plt.draw()

    # Associar botões às funções
    button_play.on_clicked(play)
    button_pause.on_clicked(pause)
    button_reset.on_clicked(reset)
    
    ani = animation.FuncAnimation(fig, update, frames=100, interval=100, blit=True)

    plt.show()

    # Após fechar a animação, exibir o gráfico de entropia
    plt.figure()
    plt.plot(entropias)
    plt.xlabel('Iteração')
    plt.ylabel('Entropia')
    plt.title('Entropia na Propagação de um Vírus')
    plt.show()

# Rodar a simulação com o valor inicial do slider
run_simulation(0.02)
