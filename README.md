# O pacote ALC

O nome ALC diz respeito a Álgebra Linear Computacional. Esse pacote foi desenvolvido para a disciplina homônima no período letivo excepcional de 2020 na UFRJ.

## O que vai encontrar aqui

No diretório `alc/` encontrará toda a implementação do pacote. Nesse pacote, são implementadas todas as funcionalidades solicitadas em todas as listas (no caso da lista 1: decomposição LU, decomposição de Cholesky, método de Jacobi, método de Gauss-Seidel, eliminação de Gauss, eliminação de Gauss-Jordan, cálculo de determinante, inversas e resolução de sistemas `Ax=B` usando os métodos previamente citados). A fim de conseguir adquirir tais funcionalidades, também foram implementadas operações básicas, como adição, subtração e multiplicação de matrizes, algumas utilidades como o cálculo do traço, da transposta, de normas de ordem `p`, verificações de simetria, se é estritamente diagonal dominante e geradores de matrizes preenchidas com zeros, preenchidas com números aleatórios e matrizes identidade. Tudo foi implementado do zero e puramente em Python. Optei por implementar com comentários e nomes de variáveis em inglês para que, no final dessa disciplina, esse repositório me sirva de portfólio (para isso, irei posteriormente trocar esse README por um em inglês).

No diretório `exercise_lists/` irá encontrar um diretório para cada lista de exercícios implementada. Dentro de cada diretório de lista, encontrará o enunciado, com nome no formato `Lista de Exercícios X_20.pdf`, o relatório gerado para ela, com nome `report.pdf`, scripts individuais para cada exercício, com nome no formato `exerciseX.py` e um script `listX.py` que executará todos os exercícios da lista, conforme solicitado. Um exemplo de como executar todos os exercícios da Lista 1, por exemplo, é:

```
python3 exercise_lists/list1/list1.py
```

O script `test_array.py`, na raiz do repositório, demonstra várias funcionalidades e maneiras de interagir com esse pacote. Ele é escrito de forma a testar todas as funcionalidades providas pelo pacote.

## Como utilizar

Antes de executar scripts com o pacote, você deve instalá-lo. Para isso, siga os seguintes passos:

0. Desinstale versões anteriores desse pacote (caso existam):

```
python3 -m pip uninstall alc
```

1. (Preferível) Clone esse repositório:

```
git clone https://github.com/gabriel-milan/linear-algebra
```

1. (Não recomendado) Baixe um ZIP do repositório com [esse link](https://github.com/gabriel-milan/linear-algebra/archive/master.zip) e extraia os arquivos para o diretório desejado.

2. Acesse o diretório clonado ou extraído

3. Instale o pacote:

```
python3 -m pip install .
```

⚠ Aviso: Para cada nova versão desse pacote, o procedimento deverá ser repetido.

## O que está implementado

- [x] alc.Array: abstração para matrizes, implementa coisas como multiplicação, soma, etc. como se fossem variáveis quaisquer
- [x] alc.eye: função para gerar uma matriz identidade com tamanho desejado
- [x] alc.zeros: função para gerar uma matriz preenchida com 0s com tamanho desejado
- [x] alc.ones: função para gerar uma matriz preenchida com 1s com tamanho desejado
- [x] alc.random_array: função para gerar uma matriz preenchida com valores aleatórios com tamanho desejado
- [x] alc.det: função para calcular o determinante de uma matriz
- [x] alc.vector_norm: função para calcular a norma `p` de um vetor
- [x] alc.is_square: função para verificar se a matriz é quadrada
- [x] alc.is_diagonally_dominant: função para verificar se a matriz é estritamente diagonal dominante
- [x] alc.is_symmetric: função para verificar se a matriz é simétrica
- [x] alc.is_definite_positive: função para verificar se a matriz é positiva definida
- [x] alc.invert: função para inverter matrizes
- [x] alc.gauss_elimination: implementa o método de eliminação de Gauss
- [x] alc.gauss_jordan_elimination: implementa o método de eliminação de Gauss-Jordan
- [x] alc.lu_decomposition: implementa o método de decomposição LU
- [x] alc.cholesky_decomposition: implementa o método de decomposição de Cholesky
- [x] alc.solve: função para resolver sistemas do tipo `Ax=B` com múltiplos métodos
- [x] alc.gauss_seidel: implementa o método de Gauss-Seidel
- [x] alc.jacobi: implementa o método de Jacobi
- [x] alc.power_method: implementa o power method, ou método das potências, para calcular o maior autovalor e o autovetor associado a ele
- [x] alc.jacobi_eigen: implementa o método de jacobi para cálculo de autovalores e autovetores
- [ ] Refazer Cholesky manual da Lista 1
- [ ] Lista 2
- [ ] Lista 3
