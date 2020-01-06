# TDD com Python

## Siga o Bode dos Testes: Usando Django, Selenium e Javascript

Implementação dos exemplos do Livro.

## Instalando o Geckodriver
Os testes rodam no firefox e utilizam o geckodriver para executar corretamente.
Baixe o geckodriver [https://github.com/mozilla/geckodriver/releases]
descompacte e mova o arquivo geckodriver para um local dentro do PATH para que seja executado corretamente.
~/.local/bin

## Comandos Uteis

Para executar todos os testes
```shell script
python manager.py test
``` 

Para executar os teste funcionais
```shell script
python manage.py test functional_tests
```

Para executar os teste de unidade
```shell script
python manage.py test lists/
```
