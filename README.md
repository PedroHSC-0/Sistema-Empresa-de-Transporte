# Sistema de Empresa de Transporte de Passageiros (Python)

.Contribuintes:Pedro Francisco Sousa Silva,Pedro Henrique Silva Costa
.Orientador: Guido Pantuza 

Este é um sistema que implementamos em python para organizar uma linha de transporte de passageiros,nos dando a possibilidade de criar,alterar,remover as linhas e poder adicionar os onibus a cada linha criada,podendo tambem no final do codigo gerar um relatorio e guardar em um txt as reservas.

##  Funcionalidades
* Criação de Linhas com inserção,remoção,alteração.Cada linha contendo cidade de origem,cidade de destino ,horario de partida(hora:minuto) e valor da passagem.
* Cada linha tem onibus que partem dela ,os onibus tendo as informações da data de partida(dia/mes/ano) e os assentos com disponibilidade.

## Permissões do Sistema

* Cadastro de Linhas no Sistema.
* Consultar os horarios para determinada cidade e poder analisar os assentos disponveis e por fim poder reserva-los.
* Quando inserimos o dia(pegamos o dia de hoje com a biblioteca time) ,conferimos se o horario do onibus daquele dia ja passou ou nao.
* Possibilitamos a geração de relatorios do total de dinheiro arrecadado e com a matriz(com txt ou no terminal).
* Temos uma matriz que expoem a ocupação com porcentagem de cada linha em dias da semana.
* As reservas de lugares salvas podem ser lidas depois caso a linha que elas pertencem exista.

## Como Executar
    Para jogar, você precisa ter o Python 3 instalado em sua máquina, ai é necessario baixar os arquivos main.py,modelo.py,relatorios.py,reservas.py,linhas.py,abrir o terminal e navegar ate o diretorio do arquivo e tem que executar o script com Bash python e a sequencia de arquivos ou apenas clilcar para rodar no vs code


### Como jogar

    • Ao iniciar, o programa solicitará que você defina:
        Uma ou mais linhas no programa com cidade origem,partida,horario e valor
        Da a possibilidade remoção,inserção e alteração
        Possa ver as linhas cadastradas

  ### Funcionalidades dos Horarios com Busões:
```
        1)Consultar horarios ,passando a cidade de origem e o ID do busao
        2)Apos consulta do horario,voce é redirecionado para ver os assentos disponiveis
        3)Escolhe se faz uma reserva e quando reserva marca naquele onibus seu assento falando se é janela ou nao 
        4)Gerando por fim um bilhete com suas informações da viagem
```

### Utilidades dos Arquivos de reserva e relatorios:
```bash
         O arquivo de reserva é gerado apos passar todos os passos dos horarios do busao , guardando  no formato CIDADE,HORARIO(hh:mm),DATA(dd/mm/aaaa),ASSENTO.
        É possivel ler as reservas do relatorio e caso voce crie uma linha com os mesmos dados da salva ,essa reserva ira aparecer nos assentos do onibus.
        E no fim dos cadastros de onibus é possivel gerar o relatorio das viagens mensais ,com os valores e ocupações
```

## Bibliotecas Usadas

Utiliza as bibliotecas time com as funcoes datetime e timedelta para poder pegarmos o dia de hoje e data do agora.
Utiliza a biblioteca os para integração com outros sistemas operacionais,podendo usar clear e outras funcionalidades,
Utiliza a biblioteca platform usamos para acessar dados do windows ou do linux.

## Considerações Finais



| Ao cliclar em uma          | Resultado                                                | 
| :-------------------------:| :-------------------------------------------------------:|
|   MINA                     | Voce perde o jogo(BOOOM)                                 | 
|   CASA SEGURA              | Mostra o numero de minas existentes nas 8 casas vizinhas | 
|   CASA SEGURA(0 MINAS)     | Jogo abre automaticamente as casas ao redor              | 


## Condições de Vitória e Derrota
