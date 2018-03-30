# Sistema de Recomendação

## Descrição do trabalho

### Programa em Python, Java ou C

- Entrada
    - Arquivo CSV: 
        
        Ratings de N usuários sobre K itens (? = 'não avaliado')
        
    - Linha de Comando:
   
        Usuário X, Item Y

        ```bash
        $ recommender ARQUIVO USUARIO ITEM
        ```

- Saída:
    - O número de itens avaliados pelo Usuário X
    - O número de usuários que avaliaram o Item Y
    - Se o Usuário X avaliou o Item Y
        
        r<sub>x,y</sub>

    - Se o Usuário X não avaliou o Item Y
        - pred(r<sub>x,y</sub>) usando abordagem baseada em usuários (Seção 2.1.1)
        - pred(r<sub>x,y</sub>) usando abordagem baseada em itens (Seção 2.2.1)

### Entrega
Devem ser entregues o código e um breve relatório
contendo os resultados das execuções com datasets
usados como casos de testes

### PRAZO: 10/04