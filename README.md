# Simulação de Propagação de Vírus com Fatalidade

Este projeto é uma simulação de propagação de um vírus em uma população. A simulação permite ajustar taxas de infecção, recuperação e fatalidade para explorar diferentes cenários epidemiológicos.

## Estados dos Indivíduos

- **Suscetível (0)**: Indivíduos que ainda não foram infectados pelo vírus.
- **Infectado (1)**: Indivíduos que foram infectados pelo vírus e estão atualmente doentes.
- **Recuperado (2)**: Indivíduos que se recuperaram da infecção e não podem ser infectados novamente.
- **Falecido (3)**: Indivíduos que morreram devido à infecção.

## Regras de Infecção

- **Infecção**: Em cada iteração, uma certa porcentagem de indivíduos suscetíveis pode ser infectada. Essa porcentagem é controlada pelo `Slider` de **Taxa de Infecção**.

  - **Cálculo de Novas Infecções**:
    ```math
    Novas Infecções = População Total × Taxa de Infecção
    ```
    - Um número de indivíduos suscetíveis equivalente ao resultado do cálculo acima é selecionado aleatoriamente e mudado para o estado de infectado.

## Regras de Recuperação

- **Recuperação**: A cada iteração, uma porcentagem dos indivíduos infectados se recupera. Essa porcentagem é controlada pelo `Slider` de **Taxa de Recuperação**.

  - **Cálculo de Recuperações**:
    ```math
    Indivíduos Recuperados = Número de Infectados × Taxa de Recuperação
    ```
    - Um número de indivíduos infectados equivalente ao resultado do cálculo acima é selecionado aleatoriamente e mudado para o estado de recuperado.

## Regras de Fatalidade

- **Fatalidade**: A cada iteração, uma porcentagem dos indivíduos infectados morre. Essa porcentagem é controlada pelo `Slider` de **Taxa de Fatalidade**.

  - **Cálculo de Fatalidades**:
    ```math
    Indivíduos Falecidos = Número de Infectados × Taxa de Fatalidade
    ```
    - Um número de indivíduos infectados equivalente ao resultado do cálculo acima é selecionado aleatoriamente e mudado para o estado de falecido.

## Fluxo Geral do Sistema

1. **Início da Simulação**:
   - A simulação começa com uma população de 10.000 indivíduos, dos quais 100 são inicialmente infectados.

2. **Propagação da Infecção**:
   - A cada iteração, a infecção se espalha para indivíduos suscetíveis de acordo com a taxa de infecção definida.
   
3. **Recuperação e Fatalidade**:
   - Simultaneamente, uma porcentagem dos indivíduos infectados se recupera e outra porcentagem morre, de acordo com as taxas de recuperação e fatalidade definidas.

4. **Evolução do Sistema**:
   - Com o tempo, a quantidade de indivíduos suscetíveis tende a diminuir, enquanto os números de recuperados e falecidos aumentam, dependendo das taxas ajustadas.

5. **Estado Final**:
   - O sistema pode eventualmente alcançar um estado onde a maioria dos indivíduos está recuperada ou falecida, dependendo de como as taxas foram ajustadas ao longo da simulação.

## Exemplos de Cenários

- **Alta Taxa de Infecção** e **Baixa Taxa de Recuperação**:
  - A infecção se espalha rapidamente, mas poucos indivíduos se recuperam. Com uma **Alta Taxa de Fatalidade**, isso resultará em um grande número de mortes.

- **Baixa Taxa de Infecção** e **Alta Taxa de Recuperação**:
  - A infecção se espalha lentamente, e muitos indivíduos se recuperam rapidamente, resultando em poucas fatalidades.

## Resumo

Este projeto permite simular uma epidemia onde indivíduos suscetíveis podem ser infectados, e uma vez infectados, podem se recuperar ou morrer. As taxas de infecção, recuperação e fatalidade controlam a dinâmica dessa propagação, permitindo que o usuário explore diferentes cenários epidemiológicos.

---

### Como Executar

Certifique-se de ter o Python e as bibliotecas `numpy` e `matplotlib` instaladas. Execute o script em um ambiente de desenvolvimento que suporte janelas de visualização, como o Jupyter Notebook ou o VSCode.

```bash
python simulacao_virus.py
