# 🧮 Cálculadora Interativa de Derivadas com Streamlit
* Acesse o site abaixo: 
* [![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://appderivada-pedroamerico.streamlit.app/)

Esse é um projeto pessoal que desenvolvi para automatizar o cálculo de derivadas usando a biblioteca **SymPy** e **Streamlit** . Esse projeto foi desenvolvido com objetivo de auxiliar estudantes de Engenharia.

##  🚀 Funcionalidades 
* Cálculo de Primeira e Segunda Derivada
* Cálculo da n-ésima derivada
* Suporte para Derivadas Explícitas e Implícitas
* Suporte para todas as letras do alfabeto latino e grego
* Simplificação de Derivadas

## 🛠️ Tecnologias
* **Python 3**
* **SymPy** - Computação Simbólica
* **Streamlit** - Interface web

## ⌨️ Como rodar?  
* Certifique-se que o Python está instalado;
* Instale a biblioteca **Sympy** e o **Streamlit** digitando no terminal: 
```bash
   pip install -r requirements.txt
   ```
* Depois, execute o aplicativo no terminal, ou acesse o site **https://appderivada-pedroamerico.streamlit.app/**
```bash
    streamlit run app.py
```
* Para Derivadas de ordem superior ou muito complexas, o cálculo pode demorar ou travar.
* Dica importante: se for usar o logaritmo natural, escreva log(...) em vez de ln(...) 
* Para o logaritmo em outras bases, use log(x, base), por exemplo: log(x, 7) 
* Além disso, caso queira usar o expoente natural (e), use, de preferência, exp(...)
* Use ** para expoentes e * para multiplicação 
* Para Seno, use sin(...) 
* Para Tangente, use tan(...)
* Para Cotangente, use cot(...) 
* Para Cossecante, use csc(...) 
* Também está disponível as funções trigonométricas hiperbólicas (sinh, cosh, ...) 