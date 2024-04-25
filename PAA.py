import matplotlib.pyplot as plt
import numpy as np
import random
import time
import matplotlib as mp
from matplotlib.animation import FuncAnimation
from matplotlib import animation
import matplotlib.animation as animation
tam = 1000
np.random.seed(1)

# Criação do vetor
def vetor(tam):
    vet = np.random.permutation(tam) # Gera uma sequência de números
    return vet

def CMergeSort():
    """Função que divide recursivamente o vetor de entrada em subconjuntos menores até que cada subconjunto contenha
    apenas um elemento. Quando todos os subconjuntos possuírem apenas um elemento, a função começa a juntá-los novamente
    em ordem."""
    def mergesort(vet, comeco, fim):
        if fim <= comeco: # Checa se e o fim é <= o começo. Se menor, o array é vazio se igual o array tem um elemento.
            return # Em ambos os casos o array só é retornado sem necessidade de ordenação.

        meio = comeco + ((fim - comeco + 1) // 2) - 1 # Calcula o índice do meio do vetor.
        yield from mergesort(vet, comeco, meio) # MergeSort na primeira metade do vetor.
        yield from mergesort(vet, meio + 1, fim) # MergeSort na segunda metade do vetor.
        yield from merge(vet, comeco, meio, fim) # Junta as metades ordenadas do vetor.
        yield vet # Yield o vetor ordenado.
        """Yield, diferentemente do return, retorna cada parte do processo e não só o resultado final."""

    vet = vetor(tam)

    generator = mergesort(vet, 0, tam - 1) # Fornece cada parte do processo de mergesort.

    def merge(vet, comeco, meio, fim):
        merged = [] # Lista vazia para armazenar os valores que foram unidos.
        indiceEsquerda = comeco # Índice da metade da esquerda recebendo o índice do começo.
        indiceDireita = meio + 1 # Índice da metade da direita recebendo o índice do meio + 1.

        # Enquanto ainda houver elementos nas metades esquerda e direita do vetor.
        while indiceEsquerda <= meio and indiceDireita <= fim:
            # Compara os elementos, adiciona o menor à lista, e anda um índice do lado do elemento adicionado.
            if vet[indiceEsquerda] < vet[indiceDireita]:
                merged.append(vet[indiceEsquerda])
                indiceEsquerda += 1
            else:
                merged.append(vet[indiceDireita])
                indiceDireita += 1

        while indiceEsquerda <= meio: # Adiciona, se houver, os elementos restantes da metade esquerda do vetor.
            merged.append(vet[indiceEsquerda])
            indiceEsquerda += 1

        while indiceDireita <= fim: # Adiciona, se houver, os elementos restantes da metade direita do vetor.
            merged.append(vet[indiceDireita])
            indiceDireita += 1

        # Atualiza o vetor original com os valores unidos, começando do índice comeco.
        for i, valOrdenados in enumerate(merged):
            vet[comeco + i] = valOrdenados
            # vet cada 20 elementos ordenados, gera o vetor atualizado. (Afim de acelerar a animação do gráfico).
            if i % 20 == 0:
                yield vet

    # Gerando o gráfico animado.
    fig, ax = plt.subplots(figsize = (9, 6)) # Cria uma figura e um conjunto de eixos para plotar gráficos.
    ax.set_title('Merge Sort') # Título do gráfico.
    plt.xlabel('Índice') # Nome do eixo x.
    plt.ylabel('Valor') # Nome do eixo y.

    # Cria um gráfico de barras. Posição das barras de acordo com vet
    bar_rects = ax.bar(range(len(vet)), vet, align = "edge")

    ax.set_xlim(0, tam) # Ajusta o tam do eixo x.
    ax.set_ylim(0, tam) # Ajusta o tam do eixo y.

    # Inicializa uma lista com um único elemento, 0. Variável acompanhará o número de iterações na animação.
    iteracoes = [0]

    # Certifica de que os índices do gráfico serão valores inteiros.
    ax.xaxis.set_major_locator(mp.ticker.MaxNLocator(integer = True))
    ax.yaxis.set_major_locator(mp.ticker.MaxNLocator(integer = True))

    # Tamanho do intervalo dos índices dos gráficos.
    tamanhoIntervalox = 100
    tamanhoIntervaloy = 100

    # Função que atualiza o gráfico de acordo com a animação.
    def update_fig(vet, rects, iteracoes):
        # Esse for itera sobre cada barra (rect) e o valor correspondente (val) no vetor.
        for rect, val in zip(rects, vet):
            rect.set_height(val) # Atualiza a altura da barra de acordo com seu valor.
        iteracoes[0] += 1 # Incrementa o contador de iterações.

        # Desenha os números índices do gráfico no eixo x.
        if iteracoes[0] % tamanhoIntervalox == 0:
            ax.set_xticks(range(0, len(vet) + 1, tamanhoIntervalox))
            ax.set_xticklabels(range(0, len(vet) + 1, tamanhoIntervalox))
            plt.draw()

        # Desenha os números índices do gráfico no eixo y.
        if iteracoes[0] % tamanhoIntervaloy == 0:
            ax.set_yticks(range(0, len(vet) + 1, tamanhoIntervaloy))
            ax.set_yticklabels(range(0, len(vet) + 1, tamanhoIntervaloy))
            plt.draw()

    # Cria a animação.
    anim = animation.FuncAnimation(fig, func = update_fig, fargs = (bar_rects, iteracoes), frames = generator,
                                   interval = 1, repeat = False, cache_frame_data = False)
    plt.show() # Mostra o plot.


def CHeapSort():
    """heapify ajusta a estrutura do heap, enquanto a extração do maior elemento é repetida até que todo o vetor
    seja ordenado."""
    vet = vetor(tam)
    def heapify(vet, n, i):
        maior = i  # Inicializa maior como raíz.
        esquerda = 2 * i + 1  # Calcula o índice do filho esquerdo de um nó.
        direita = 2 * i + 2  # Calcula o índice do filho direito de um nó.

        # Checa se o filho esquerdo existe e se é maior que a raíz.
        if esquerda < n and vet[i] < vet[esquerda]:
            maior = esquerda

        # Checa se o filho direito existe e se é maior que a raíz.
        if direita < n and vet[maior] < vet[direita]:
            maior = direita

        # Muda a raíz se necessário.
        if maior != i:
            vet[i], vet[maior] = vet[maior], vet[i]  # Troca
            yield vet
            # Heapify a raíz.
            yield from heapify(vet, n, maior)

    # Função principal que ordena o vetor.
    def heapSort(vet):
        n = len(vet) # n recebe o tam do vetor.

        # Construção do heap máximo.
        # Começa em n//2 já que o último pai estará lá.
        for i in range(n // 2, -1, -1):
            yield from heapify(vet, n, i)

        # Extraindo os elementos de maior valor
        for i in range(n - 1, 0, -1):
            vet[i], vet[0] = vet[0], vet[i]  # Troca
            yield vet
            if i % 999999999 == 0: # Acelera a animação
                yield vet
            yield from heapify(vet, i, 0)

    generator = heapSort(list(vet)) # Fornece cada parte do processo de heapsort.

    # Inicializa fig e ax.
    fig, ax = plt.subplots(figsize = (9, 6))
    ax.set_xlabel('Índice') # Nome do eixo x.
    ax.set_ylabel('Valor') # Nome do eixo y.
    ax.set_title('Heap Sort') # Título do gráfico.

    # Cria o plot inicial das barras.
    bars = ax.bar(np.arange(tam), vet, color = 'blue')

    # Função para animação
    def animate(frame):
        vetorOrdenado = next(generator)
        for bar, val in zip(bars, vetorOrdenado):
            bar.set_height(val) # Altura da barra
            bar.set_color('blue') # Cor da barra

    # Cerifica de que os números do gráfico serão inteiros
    ax.xaxis.set_major_locator(mp.ticker.MaxNLocator(integer = True))
    ax.yaxis.set_major_locator(mp.ticker.MaxNLocator(integer = True))

    # Cria animação
    ani = animation.FuncAnimation(fig, animate, frames = tam * 10, interval = 100,
                                  repeat = False, cache_frame_data = False)

    plt.show() # Mostra o plot


def CBinaryInsertionSort():
    def BinarySearch(vet, item, comeco, fim):
        """Verifica se o índice de início é igual ao índice de fim. Se sim, o intervalo de busca tem tam 1. Se o
        elemento no índice de início for maior que o item buscado, retorna o índice de início, indicando que o item deve
         ser inserido antes desse índice. Caso contrário, retorna o índice de início mais 1, indicando que o item deve
         ser inserido após esse índice."""
        if comeco == fim:
            return comeco if vet[comeco] > item else comeco + 1
        """Essa linha verifica se o índice de início é maior que o índice de fim. Se sim, o item não está presente no 
        vetor e deve ser inserido no índice de início."""
        if comeco > fim:
            return comeco

        meio = (comeco + fim) // 2 # Calcula o índice do elemento do meio do intervalo de busca.
        """Essas linhas verificam se o elemento no meio do intervalo é menor ou maior que o item buscado. Se for menor, 
        a busca é realizada recursivamente na metade direita do intervalo. Se for maior, a busca é realizada 
        recursivamente na metade esquerda do intervalo."""
        if vet[meio] < item:
            return BinarySearch(vet, item, meio + 1, fim)
        elif vet[meio] > item:
            return BinarySearch(vet, item, comeco, meio - 1)
        # Se o elemento no meio for igual ao item buscado, o item foi encontrado e o índice do meio é retornado.
        else:
            return meio

    def BinaryInsertionSort(vet):
        yield vet.copy()  # Yield o vetor incial (desordenado).

        """Este for itera os índices do vetor vet começando do segundo elemento até o último elemento. Pois o primeiro 
        elemento é considerado como já estando na posição correta inicialmente."""
        for i in range(1, len(vet)):
            """O valor do elemento atual (vet[i]) é armazenado na variável itemInserir. O índice j é definido para ser 
            o índice anterior ao índice atual i."""
            itemInserir = vet[i]
            j = i - 1
            # BinarySearch é chamada para encontrar o índice onde o itemInserir deve ser inserido no vetor ordenado.
            indiceInserir = BinarySearch(vet, itemInserir, 0, j)
            # Esse while é executado enquanto j é maior ou igual ao índice onde o itemInserir deve ser inserido.
            while j >= indiceInserir:
                vet[j + 1] = vet[j]
                j -= 1
            vet[j + 1] = itemInserir

            # Yield a cada 10 iteração afim de acelerar a animação
            if i % 10 == 0:
                yield vet.copy()

        yield vet.copy()  # Yield o vetor ordenado

    vet = vetor(tam)

    # Cria o generator para os frames da animação
    generator = BinaryInsertionSort(vet)

    # Inicializa fig e axis
    fig, ax = plt.subplots(figsize = (9, 6))
    ax.set_xlabel('Índice') # Nome do eixo x.
    ax.set_ylabel('Valor') # Nome do eixo y.
    ax.set_title('Binary Insertion Sort') # Título do gráfico.

    # Cria plot incial das barras
    bars = ax.bar(np.arange(tam), vet, color = 'blue')

    # Função para animação
    def animate(frame):
        vetOrdenado = next(generator)
        for bar, val in zip(bars, vetOrdenado):
            bar.set_height(val) # Altura da barra

    # Cria animação
    ani = FuncAnimation(fig, animate, frames = len(vet), interval = 1,
                        repeat = False, cache_frame_data = False)

    plt.show()


def CCombSort():
    def comb_sort(vet):
        gap = len(vet) # Determina o gap como o tam do vetor
        diminuir = 1.3 # Determina o quanto que o gap será diminuido a cada passagem
        troca = False # Inicializa troca como falso (variável de controle)

        iterations = 0 # Inicaliza iterações com 0
        max_iteracoes = len(vet) * len(vet) // 2  # Determina um número máximo de iterações

        while (gap != 1 or troca) and iterations < max_iteracoes:  # Checa o máximo de iterações
            gap = int(gap / diminuir) # Diminui o gap
            if gap < 1: # Se a divisão der um número menor que 1 o espaço é definido como 1
                gap = 1
            """i é reiniciado para 0 e troca é definido como falso. Isso prepara o estado para a próxima iteração do 
            loop, onde i será usado para percorrer os elementos do vetor e troca será usada para rastrear se houve 
            alguma troca de elementos durante a iteração anterior."""
            i = 0
            troca = False

            """Percorre o vetor enquanto ainda houver elementos disponíveis para comparação com um intervalo gap 
            entre eles."""
            while i + gap < len(vet):
                # Se verdadeiro, foi encontrado um par de elementos fora de ordem que precisam ser trocados.
                if vet[i] > vet[i + gap]:
                    trocaChave(vet, i, i + gap) # Função que faz a troca de posições dos elementos
                    troca = True # Elemento trocado logo, troca passa a ser True

                # Yield os frames a cada algumas iterações
                yield vet.copy(), i, i + gap

                if iterations % 99999 == 0:  # Yield a cada 99999 iterações
                    yield vet.copy(), i, i + gap

                i += 1
                iterations += 1


    vet = vetor(tam)

    # Função que faz a troca de posições dos elementos
    def trocaChave(vet, i, j):
        vet[i], vet[j] = vet[j], vet[i]

    # Cria generator para os frames da animação
    generator = comb_sort(vet)

    # Inicializa figure e axis
    fig, ax = plt.subplots(figsize = (9, 6))
    ax.set_xlabel('Índice') # Nome do eixo x
    ax.set_ylabel('Valor') # Nome do eixo y
    ax.set_title('Comb Sort') # Título do gráfico

    # Cria o plot inicial das barras
    bars = ax.bar(np.arange(tam), vet, color = 'blue')

    # Certifica que os números do gráfico serão inteiros
    ax.xaxis.set_major_locator(mp.ticker.MaxNLocator(integer = True))
    ax.yaxis.set_major_locator(mp.ticker.MaxNLocator(integer = True))

    # Função para animação
    def animate(frame):
        vetOrdenado, i, j = frame
        for k, (bar, val) in enumerate(zip(bars, vetOrdenado)):
            bar.set_height(val)
            if k == i or k == j:
                bar.set_color('red')  # Marca as barras que estão se movendo em vermelho
            else:
                bar.set_color('blue')  # Volta as barras para azul

    # Cria animação
    ani = FuncAnimation(fig, animate, frames = generator, interval = 1, repeat = False, cache_frame_data = False)
    plt.show() # Plota a animação


def CShellSort():
    def shell_sort(vet):
        tam = len(vet) # Tamanho incializado como o tam do vetor
        gap = tam // 2 # gap inicializado como metade do tam do vetor

        while gap > 0:
            # Percorre o vetor, comparando e trocando os elementos com um intervalo gap entre eles.
            for i in range(gap, tam):
                aux = vet[i]
                j = i
                # Se o elemento j for maior que o elemento j - gap eles trocam de lugar
                while j >= gap and vet[j - gap] > aux:
                    vet[j] = vet[j - gap]
                    j -= gap
                vet[j] = aux
                yield vet.copy(), j, j - gap
            gap //= 2 # Diminui o gap pela metade

    vet = vetor(tam)
    # Generator para os frames
    generator = shell_sort(vet)

    # Inicializa figure e axis
    fig, ax = plt.subplots(figsize = (9, 6))
    ax.set_xlabel('Índice') # Nome do eixo x
    ax.set_ylabel('Valor') # Nome do eixo y
    ax.set_title('Shell Sort') # Título do gráfico

    # Cria o plot inicial das barras
    bars = ax.bar(np.arange(tam), vet, color = 'blue')

    # Função para animação
    def animate(frame):
        vetOrdenado, i, j = next(generator)
        for k, (bar, val) in enumerate(zip(bars, vetOrdenado)):
            bar.set_height(val)
            if k == i or k == j:
                bar.set_color('red')  # Barras que estão se movendo ficarão vermelhas
            else:
                bar.set_color('blue')  # Volta as cores das outras barras para azul

    # Certifica de que os valores do gráfico serão inteiros
    ax.xaxis.set_major_locator(mp.ticker.MaxNLocator(integer = True))
    ax.yaxis.set_major_locator(mp.ticker.MaxNLocator(integer = True))

    # Cria animação
    ani = FuncAnimation(fig, animate, frames = len(vet) * len(vet),
                        interval = 1, repeat = False, cache_frame_data = False)

    plt.show()


def CBitonicSort():
    def compETroca(vet, i, j, direcao): # Função que compara e troca valores se a condição for satisfeita
        if (direcao == 1 and vet[i] > vet[j]) or (direcao == 0 and vet[i] < vet[j]):
            vet[i], vet[j] = vet[j], vet[i]

    # Função que une duas subsequências bitônicas em uma única subsequência bitônica maior.
    def bitonicMerge(vet, baixo, cont, direcao):
        if cont > 1:
            k = cont // 2
            for i in range(baixo, baixo + k):
                compETroca(vet, i, i + k, direcao)
            bitonicMerge(vet, baixo, k, direcao)
            bitonicMerge(vet, baixo + k, k, direcao)

    """Função que divide recursivamente o vetor em subsequências bitônicas, ordena essas subsequências de forma 
    crescente ou decrescente e, em seguida, une as subsequências de forma a manter o padrão bitônico."""
    def bitonicSort(vet, baixo, cont, direcao):
        if cont > 1:
            k = cont // 2
            bitonicSort(vet, baixo, k, 1)
            bitonicSort(vet, baixo + k, k, 0)
            bitonicMerge(vet, baixo, cont, direcao)

    # Vetor a ser utilizado
    t = 1024 # Somente tamanhos com raiz quadrada exata
    vet = vetor(t) # Vetor com o tamanho adequado
    n = len(vet) # n é o tamanho de vet
    up = 1 # Direção crescente (Qualquer número diferente de 1 ordena na direção decrescente)

    # Função que chama a função bitonicSort com os parâmetros apropriados
    def sort(vet, tam, up):
        bitonicSort(vet, 0, tam, up)

    # Inicializa figure e axis
    fig, ax = plt.subplots(figsize = (9, 6))
    ax.set_xlabel('Índice') # Nome do eixo x
    ax.set_ylabel('Valor') # Nome do eixo y
    ax.set_title('Bitonic Sort') # Título do gráfico

    # Cria plot incial das barras
    bars = ax.bar(np.arange(n), vet, color = 'blue')

    # Função para animação
    def animate(frame):
        if frame < n:
            sort(vet, frame + 1, up)
            for bar, val in zip(bars, vet):
                bar.set_height(val) # Altura das barras
                bar.set_color('blue') # Cor das barras
                # ax.set_title(f'Bitonic Sort')
            return bars

    # Certifica de que os números do gráfico serão inteiros
    ax.xaxis.set_major_locator(mp.ticker.MaxNLocator(integer = True))
    ax.yaxis.set_major_locator(mp.ticker.MaxNLocator(integer = True))

    # Cria animação
    ani = FuncAnimation(fig, animate, frames = n, interval = 200, repeat = False)

    plt.show() # Plota animação


def CRadixSortLDS():
    def contSortLDS(vet, exp):
        n = len(vet)
        aux = [0] * n  # Lista que armazena os elementos ordenados temporariamente
        cont = [0] * 10 # Lista com 10 elementos, todos contendo o valor 0

        """Para cada elemento, esse for calcula o índice do grupo onde o elemento deve ser colocado dividindo-o pelo 
        valor exp (um fator de escala para determinar a posição do dígito atual no número)."""
        for i in range(n):
            indice = vet[i] // exp
            cont[indice % 10] += 1

        # Calcula as posições finais dos grupos após a fase de contagem do algoritmo.
        for i in range(1, 10):
            cont[i] += cont[i - 1]

        i = n - 1
        # Redistribui os elementos ordenados de vet para o vetor aux de acordo com a contagem feita anteriormente.
        while i >= 0:
            indice = vet[i] // exp
            aux[cont[indice % 10] - 1] = vet[i]
            cont[indice % 10] -= 1
            i -= 1

        """Para cada elemento de aux, o valor é copiado de volta para vet. Durante cada iteração, o estado atual de vet 
        é retornado através de yield, juntamente com o índice atual i."""
        for i in range(n):
            vet[i] = aux[i]
            yield vet.copy(), i

    def RadixSortLDS(vet):
        max_num = max(vet)
        exp = 1
        while max_num // exp > 0:
            yield from contSortLDS(vet, exp)
            exp *= 10

    vet = vetor(tam)

    generator = RadixSortLDS(vet)

    fig, ax = plt.subplots(figsize = (9, 6))
    ax.set_xlabel('Índice')
    ax.set_ylabel('Valor')
    ax.set_title('Radix Sort (LSD)')

    bars = ax.bar(np.arange(tam), vet, color = 'blue')

    def animate(frame):
        vetOrdenado, i = frame
        for k, (bar, val) in enumerate(zip(bars, vetOrdenado)):
            bar.set_height(val)
            if k == i:
                bar.set_color('red')  # Marca de vermelho as barras que estão se movendo
            else:
                bar.set_color('blue')  # Volta com as cores das barras para azul

    # Certfica de que os números do gráfico serão inteiros
    ax.xaxis.set_major_locator(mp.ticker.MaxNLocator(integer = True))
    ax.yaxis.set_major_locator(mp.ticker.MaxNLocator(integer = True))

    ani = FuncAnimation(fig, animate, frames = generator, interval = 1, repeat = False, cache_frame_data = False)

    plt.show()


def CRadixSortMDS():
    # Radix Sort MDS
    def contSortMDS(vet, exp):
        n = len(vet)
        aux = [0] * n # Lista que armazena os elementos ordenados temporariamente
        cont = [0] * 10 # Lista com 10 números 0

        # Procedimento semelhante ao Radix Sort LDS só que pegando o primeiro algarismo do número
        for i in range(n):
            indice = (vet[i] // exp) % 10
            cont[indice] += 1

        for i in range(1, 10):
            cont[i] += cont[i - 1]

        i = n - 1
        while i >= 0:
            indice = (vet[i] // exp) % 10
            aux[cont[indice] - 1] = vet[i]
            cont[indice] -= 1
            i -= 1

        for i in range(n):
            vet[i] = aux[i]
            yield vet.copy(), i

    def RadixSortMDS(vet):
        max_num = max(vet)
        exp = 1
        while max_num // exp > 0:
            yield from contSortMDS(vet, exp)
            exp *= 10

    vet = vetor(tam)
    generator = RadixSortMDS(vet)

    fig, ax = plt.subplots(figsize = (9, 6))
    ax.set_xlabel('Índice')
    ax.set_ylabel('Valor')
    ax.set_title('Radix Sort (MDS)')

    bars = ax.bar(np.arange(tam), vet, color = 'blue')

    def animate(frame):
        vetOrdenado, i = frame
        for k, (bar, val) in enumerate(zip(bars, vetOrdenado)):
            bar.set_height(val)
            if k == i:
                bar.set_color('red')
            else:
                bar.set_color('blue')

    # Certifica que os números do gráfico serão inteiros
    ax.xaxis.set_major_locator(mp.ticker.MaxNLocator(integer = True))
    ax.yaxis.set_major_locator(mp.ticker.MaxNLocator(integer = True))

    ani = FuncAnimation(fig, animate, frames = generator, interval = 1,
                        repeat = False, cache_frame_data = False)

    plt.show()


def CInsertionSort():
    def insertionsort(vet):
        for j in range(1, len(vet)):
            chave = vet[j] # Armazena o valor atual a ser inserido na posição correta
            i = j - 1  # Inicializa o índice para comparar com a chave

            """Enquanto houver elementos à esquerda da chave e forem maiores que ela, move os elementos maiores para a 
            direita para abrir espaço para a chave"""
            while (i >= 0 and vet[i] > chave):
                vet[i + 1] = vet[i]
                i -= 1 # Move para o próximo elemento à esquerda
                # Yield vet
            vet[i + 1] = chave # Insere a chave na posição correta após o loop
            if j % 2 == 0:  # Yield a cada 2 iterações (deixa o gráfico mais rápido)
                yield vet

    vet = vetor(tam)
    generator = insertionsort(vet)

    fig, ax = plt.subplots(figsize = (9, 6))

    rects = ax.bar(range(len(vet)), vet, align = "edge", color = 'blue')

    plt.title('Insertion Sort')
    ax.set_xlabel('Índice')
    ax.set_ylabel('Valor')
    ax.set_xlim(0, len(vet))
    ax.set_ylim(0, int(1.1 * len(vet)))
    iteracao = [0]

    def animate(vet, rects, iteracao):
        for rect, val in zip(rects, vet):
            rect.set_height(val)

    anim = FuncAnimation(fig, func = animate, fargs = (rects, iteracao),frames = generator,
                         interval = 1, repeat = False, cache_frame_data = False)

    plt.show()


def CSelectionSort():
    vet = vetor(tam)
    n = len(vet)
    x = np.arange(tam)

    def SelectionSort(vet):
        # Passa por todo o vetor
        for i in range(len(vet)):
            # Acha o valor mínimo no vetor desordenado
            indiceMin = i
            for j in range(i + 1, len(vet)):
                if vet[j] < vet[indiceMin]:
                    indiceMin = j

            # Troca o elemento mínimo encontrado pelo primeiro elemento
            vet[i], vet[indiceMin] = vet[indiceMin], vet[i]
            yield vet.copy()

    generator = SelectionSort(vet)

    fig, ax = plt.subplots(figsize = (9, 6))
    rects = ax.bar(range(len(vet)), vet, align = "edge", color = 'blue')

    plt.title('Selection Sort')
    ax.set_xlabel('Índice')
    ax.set_ylabel('Valor')
    ax.set_xlim(0, len(vet))
    ax.set_ylim(0, int(1.1 * len(vet)))

    def animate(frame_data):
        for rect, val in zip(rects, frame_data):
            rect.set_height(val)

    anim = FuncAnimation(fig, func = animate, frames = generator,
                         interval = 1, repeat = False, cache_frame_data = False)

    plt.show()


def CTimSort():
    valorMin = 32 # Tamanho mínimo de um run (sequência ordenada) no TimSort.
    # Calcula o tamanho mínimo do run. Um run é uma subsequência que está ordenada.
    def calcMinRun(n):
        ultimo = 0
        while n >= valorMin:
            ultimo |= n & 1
            n >>= 1
        return n + ultimo

    # Implementa o algoritmo de ordenação insertion sort em um subarray específico.
    def insertionSort(vet, esquerda, direita):
        for i in range(esquerda + 1, direita + 1):
            j = i
            while j > esquerda and vet[j] < vet[j - 1]:
                vet[j], vet[j - 1] = vet[j - 1], vet[j]
                j -= 1

    # Combina dois subarrays ordenados em um único array ordenado.
    def merge(vet, prim, meio, ultimo):
        len1, len2 = meio - prim + 1, ultimo - meio
        esquerda, direita = [], []
        for i in range(0, len1):
            esquerda.append(vet[prim + i])
        for i in range(0, len2):
            direita.append(vet[meio + 1 + i])

        i = 0
        j = 0
        k = prim

        # Combina os subarrays ordenados em um único array ordenado
        while i < len1 and j < len2:
            if esquerda[i] <= direita[j]:
                vet[k] = esquerda[i]
                i += 1
            else:
                vet[k] = direita[j]
                j += 1
            k += 1

        # Adiciona, se houver, elementos restantes do subarray esquerdo
        while i < len1:
            vet[k] = esquerda[i]
            k += 1
            i += 1

        # Adiciona, se houver, elementos restantes do subarray direito
        while j < len2:
            vet[k] = direita[j]
            k += 1
            j += 1

    # Algoritmo de ordenação Tim Sort
    def TimSort(vet):
        n = len(vet)
        minRun = calcMinRun(n)
        for comeco in range(0, n, minRun):
            fim = min(comeco + minRun - 1, n - 1)
            insertionSort(vet, comeco, fim)
        tam = minRun
        while tam < n:
            for esquerda in range(0, n, 2 * tam):
                metade = min(n - 1, esquerda + tam - 1)
                direita = min((esquerda + 2 * tam - 1), (n - 1))
                if metade < direita:
                    merge(vet, esquerda, metade, direita)
            tam = 2 * tam
        return vet

    vet = vetor(tam)

    generator = (TimSort(vet[:i]) for i in range(1, len(vet) + 1))

    fig, ax = plt.subplots(figsize = (9, 6))
    rects = ax.bar(range(len(vet)), vet, align="edge", color='blue')

    plt.title('Tim Sort')
    ax.set_xlabel('Índice')
    ax.set_ylabel('Valor')
    ax.set_xlim(0, len(vet))
    ax.set_ylim(0, int(1.1 * max(vet)))

    def animate(frame_data):
        for rect, val in zip(rects, frame_data):
            rect.set_height(val)

    anim = FuncAnimation(fig, func = animate, frames = generator,
                         interval = 1, repeat = False, cache_frame_data = False)

    plt.show()


def CBubbleSort():
    def swap(vet, i, j):
        vet[i], vet[j] = vet[j], vet[i]

    def BubbleSort(vet):
        swapped = True

        for i in range(len(vet) - 1):
            if not swapped:
                return
            swapped = False

            for j in range(len(vet) - 1 - i):
                if vet[j] > vet[j + 1]:
                    swap(vet, j, j + 1)
                    swapped = True
            if (i + 1) % 2 == 0:  # Yield a cada 2 iterações
                yield vet

    def visualize():
        vet = vetor(tam)
        generator = BubbleSort(vet)

        fig, ax = plt.subplots(figsize = (9, 6))
        plt.title('Bubble Sort')
        plt.xlabel('Índice')
        plt.ylabel('Valor')
        bar_sub = ax.bar(range(len(vet)), vet, align = "edge")

        ax.set_xlim(0, tam)
        text = ax.text(0.02, 0.95, "", transform = ax.transAxes)
        iteracao = [0]


        def update(vet, rects, iteracao):
            for rect, val in zip(rects, vet):
                rect.set_height(val)
        iteracao[0] += 1

        anim = animation.FuncAnimation(fig, func = update, fargs = (bar_sub, iteracao), frames = generator,
                                       repeat = True, blit = False, interval = 1, save_count = 90000)

        plt.show()
        plt.close()
    visualize()


def CCocktailShakerSort():
    def CocktailShakerSort(vet):
        n = len(vet)
        troca = True
        comeco = 0
        fim = n - 1

        while troca:
            troca = False

            # Move da esquerda para direita
            for i in range(comeco, fim):
                if vet[i] > vet[i + 1]:
                    vet[i], vet[i + 1] = vet[i + 1], vet[i]
                    troca = True
                if i % 50 == 0: # Afim de acelerar a animação do gráfico
                    yield vet

            if not troca:
                break

            troca = False
            fim -= 1

            # Move da direita para esquerda
            for i in range(fim - 1, comeco - 1, -1):
                if vet[i] > vet[i + 1]:
                    vet[i], vet[i + 1] = vet[i + 1], vet[i]
                    troca = True
                if i % 50 == 0: # Afim de acelerar a animação do gráfico
                    yield vet

            comeco += 1

        return vet

    vet = vetor(tam)

    fig, ax = plt.subplots(figsize = (9, 6))
    rects = ax.bar(range(len(vet)), vet, align = "edge", color = 'blue')

    plt.title('Cocktail Shaker Sort')
    ax.set_xlabel('Índice')
    ax.set_ylabel('Valor')

    ax.set_xlim(0, len(vet))
    ax.set_ylim(0, int(1.1 * max(vet)))
    iteracao = [0]

    def animate(vet, rects, iteracao):
        for rect, val in zip(rects, vet):
            rect.set_height(val)

    # Animate the sorting process
    anim = FuncAnimation(fig, func = animate, fargs = (rects, iteracao), frames = CocktailShakerSort(vet[:]),
                         interval = 1, repeat = False, cache_frame_data = False)

    plt.show()


def CGnomeSort():
    def GnomeSort(vet):
        n = len(vet)
        for indice in range(n):
            if indice == 0:
                continue
            while indice > 0 and vet[indice] < vet[indice - 1]:
                vet[indice], vet[indice - 1] = vet[indice - 1], vet[indice]
                yield vet
                indice -= 1
            if indice % 999999 == 0: # Afim de acelerar a animação do gráfico
                yield vet

    vet = vetor(tam)
    n = len(vet)

    fig, ax = plt.subplots(figsize = (9, 6))
    rects = ax.bar(range(len(vet)), vet, align = "edge", color = 'blue')

    plt.title('Gnome Sort')
    plt.xlabel('Índice')
    plt.ylabel('Valor')

    ax.set_xlim(0, len(vet))
    ax.set_ylim(0, len(vet))
    iteracao = [0]

    def animate(vet, rects, iteracao):
        for rect, val in zip(rects, vet):
            rect.set_height(val)

    anim = FuncAnimation(fig, func = animate, fargs = (rects, iteracao), frames = GnomeSort(vet.copy()),
                         interval = 1, repeat = False, cache_frame_data = False)

    plt.show()


def COddEvenSort():
    vet = vetor(tam)
    n = len(vet)
    def OddEvenSort(vet):
        ordenado = False # Variável de controle
        while not ordenado:
            ordenado = True
            for i in range(0, n - 1, 2):  # Índices pares
                if vet[i] > vet[i + 1]:
                    vet[i], vet[i + 1] = vet[i + 1], vet[i]
                    ordenado = False
                if i % 100 == 0:
                    yield vet

            for i in range(1, n - 1, 2):  # Índices ímpares
                if vet[i] > vet[i + 1]:
                    vet[i], vet[i + 1] = vet[i + 1], vet[i]
                    ordenado = False
                if i % 100 == 0:
                    yield vet
        yield vet  # Yield vetor ordenado no final

    n = len(vet)
    fig, ax = plt.subplots(figsize = (9, 6))
    rects = ax.bar(range(len(vet)), vet, align = "edge", color = 'blue')

    plt.title('Odd-Even Sort')
    plt.xlabel('Índice')
    plt.ylabel('Valor')

    ax.set_xlim(0, len(vet))
    ax.set_ylim(0, len(vet))
    iteracao = [0]

    def animate(vet, rects, iteracao):
        for rect, val in zip(rects, vet):
            rect.set_height(val)

    anim = FuncAnimation(fig, func = animate, fargs = (rects, iteracao), frames = OddEvenSort(vet.copy()),
                         interval = 1, repeat = False, cache_frame_data = False)

    plt.show()


def CQuickSort():
    vet = vetor(tam)
    def particao(vet, menor, maior):
        indicePivo = (menor + maior) // 2
        valorPivo = vet[indicePivo]

        # Troca o pivô com o último elemento
        vet[indicePivo], vet[maior] = vet[maior], vet[indicePivo]

        i = menor
        for j in range(menor, maior):
            if vet[j] < valorPivo:
                vet[i], vet[j] = vet[j], vet[i]
                i += 1

        # Place the pivot value in its sorted position
        vet[i], vet[maior] = vet[maior], vet[i]
        return i

    def medianadetres(vet, menor, maior):
        metade = (menor + maior) // 2
        if vet[menor] > vet[metade]:
            vet[menor], vet[metade] = vet[metade], vet[menor]
        if vet[metade] > vet[maior]:
            vet[metade], vet[maior] = vet[maior], vet[metade]
        if vet[menor] > vet[metade]:
            vet[menor], vet[metade] = vet[metade], vet[menor]
        return metade

    def QuickSortmed(vet, menor, maior):
        if menor < maior:
            indicePivo = medianadetres(vet, menor, maior)
            indicePivo = particao(vet, menor, maior)
            yield vet.copy(), menor, maior  # Yield intermediate state of the array and the indices of the partition
            yield from QuickSortmed(vet, menor, indicePivo - 1)
            yield from QuickSortmed(vet, indicePivo + 1, maior)

    def QuickSort(vet):
        yield from QuickSortmed(vet, 0, len(vet) - 1)

    # Generator para os frames da animação
    generator = QuickSort(vet)

    # Inicializa figure e axis
    fig, ax = plt.subplots(figsize = (9, 6))
    plt.xlabel('Índice')
    plt.ylabel('Valor')
    plt.title('Quick Sort')

    # Cria o plot incial das barras
    bars = ax.bar(np.arange(tam), vet, color = 'blue')

    # Função para animação
    def animate(frame):
        vetOrdenado, menor, maior = frame
        for k, (bar, val) in enumerate(zip(bars, vetOrdenado)):
            bar.set_height(val)
            if menor <= k <= maior:
                bar.set_color('red')  # Marca as barras que estão se movendo de vermelho
            else:
                bar.set_color('blue')  # Retorna as barras para a cor azul

    # Certifica que os números do gráfico serão inteiros
    ax.xaxis.set_major_locator(mp.ticker.MaxNLocator(integer = True))
    ax.yaxis.set_major_locator(mp.ticker.MaxNLocator(integer = True))


    ani = FuncAnimation(fig, animate, frames = generator, interval = 1, repeat = False, cache_frame_data = False)

    plt.show()


# Mapeando cada opção
opcoes = {
     1: CMergeSort,
     2: CHeapSort,
     3: CBinaryInsertionSort,
     4: CCombSort,
     5: CShellSort,
     6: CBitonicSort,
     7: CRadixSortLDS,
     8: CRadixSortMDS,
     9: CInsertionSort,
    10: CSelectionSort,
    11: CTimSort,
    12: CBubbleSort,
    13: CCocktailShakerSort,
    14: CGnomeSort,
    15: COddEvenSort,
    16: CQuickSort
}

# Main
while True:
    print(f'\nMétodos de ordenação:')
    print(f'-' * 60)
    print(f'\t1 - Merge Sort\t\t\t\t 9 - Insertion Sort\n\t2 - Heap Sort\t\t\t\t10 - Selection Sort\n\t'
          f'3 - Binary Insertion Sort\t11 - Tim Sort\n\t4 - Comb Sort\t\t\t\t12 - Bubble Sort\n\t5 - Shell Sort'
          f'\t\t\t\t13 - Cocktail Shaker Sort\n\t6 - Bitonic Sort\t\t\t14 - Gnome Sort\n\t7 - Radix Sort LDS\t\t\t'
          f'15 - Odd-Even Sort\n\t8 - Radix Sort MDS\t\t\t16 - QuickSort')
    print(f'-' * 60)

    while True:
        op = int(input(f'Informe o método de ordenação desejado: '))
        if 1 <= op <= 16:
            if op in opcoes:
                opcoes[op]()
                break

    choice = input('\nDeseja escolher outro método? (s/n): ').lower()
    if choice == 'n':
        print(f'\nPrograma finalizado.\n')
        break
    elif choice == 's':
        continue
    else:
        print(f'\nOpção inválida. Digite "s" ou "n".')
        choice = input('\nDeseja escolher outro método? (s/n): ').lower()
        if choice == 'n':
            print(f'\nPrograma finalizado.\n')
            break
        elif choice == 's':
            continue
        else:
            print(f'\nOpção inválida. Digite "s" ou "n".\n')
