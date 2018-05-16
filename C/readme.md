# Instruções

- Para executar o programa, após compilá-lo você deve passar os seguintes parâmetros na chamada:

 - Arquivo [string] 
	- nome do arquivo (com extensão) a ser analisado.
 - Usuário [string]
	- nome do usuário a ser verificado. 
 - Item #  [int]
	- Número da coluna referete ao item que você deseja que seja avaliado. Inicia a contagem em 1 (primeira coluna = 1). 
## Exemplo

	```bash
        $ main dataset.csv A1 5
        ```

## Observações:
Caso você chame o programa sem passar exatamente quatro parâmetros ele dá erro e informa no console.
Não é feito um tratamento nos inputs dos parâmetros, asume-se que o usuário fará uso apropriado.