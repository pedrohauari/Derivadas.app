# Autor : Pedro Américo
import streamlit as st
import sympy as sp
import string

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(
    page_title="Calculadora de Engenharia - Derivadas", 
    layout="centered", 
    page_icon="⚙️"
)

def calculadora():
    # PREPARAÇÃO DOS SÍMBOLOS 
    latino = list(string.ascii_lowercase + string.ascii_uppercase)
    gregas = [
        "alpha", "beta", "gamma", "delta", "epsilon", "omega", "psi", "chi", 
        "phi", "eta", "zeta", "theta", "iota", "kappa", "lambda", "nu", 
        "mu", "omicron", "xi", "pi", "rho", "sigma", "tau", "upsilon"
    ]
    todos_simbolos = latino + gregas + [g.capitalize() for g in gregas]

    st.title("⚙️ Calculadora de Derivadas Profissional")
    st.markdown("---")

    # --- INTERFACE LATERAL ---
    st.sidebar.header("🔧 Configurações")
    
    modo = st.sidebar.radio("Modo de Cálculo:", ["Explícita", "Implícita"])
    
    # Tratamento de entrada
    entrada_raw = st.sidebar.text_area("Digite a função/equação:", "x**2 + y**2 = 25", help="Use '*' para multiplicar e '**' ou '^' para potência.")
    entrada_usuario = entrada_raw.replace('^', '**') 

    if modo == "Explícita":
        var_indep = st.sidebar.selectbox("Variável Independente (x):", todos_simbolos, index=23) # x
        var_dep = None
    else:
        var_indep = st.sidebar.selectbox("Variável Independente (x):", todos_simbolos, index=23) # x
        var_dep = st.sidebar.selectbox("Variável Dependente (y):", todos_simbolos, index=24)    # y

    n = st.sidebar.number_input("Ordem da derivada (n):", min_value=1, value=1, step=1)
    
    # Nova opção para evitar Explosao simbólica
    tipo_simplificacao = st.sidebar.selectbox(
        "Nível de Simplificação:", 
        ["Leve (Rápido)", "Médio (Cancel)", "Profundo (Lento)"],
        index=1
    )

    # --- PROCESSAMENTO ---
    try:
        # Limpeza da equação para o SymPy
        if "=" in entrada_usuario:
            lado_esquerdo, lado_direito = entrada_usuario.split("=")
            texto_para_sympy = f"({lado_esquerdo}) - ({lado_direito})"
        else:
            texto_para_sympy = entrada_usuario

        # Definição dos símbolos e da função
        f = sp.sympify(texto_para_sympy, locals={"e": sp.E})
        x_sym = sp.symbols(var_indep)

        if modo == "Implícita" and var_dep:
            y_sym = sp.symbols(var_dep)
            
            st.subheader("📝 Equação Analisada")
            st.latex(f"{sp.latex(f)} = 0")
            
            with st.spinner("Processando derivada implícita complexa..."):
                # Cálculo da derivada implícita
                resultado = sp.idiff(f, y_sym, x_sym, n)
                
                # Notação LaTeX
                notacao = rf"\frac{{d^{{{n}}}{var_dep}}}{{d{var_indep}^{{{n}}}}}" if n > 1 else rf"\frac{{d{var_dep}}}{{d{var_indep}}}"
        
        else:
            st.subheader("📝 Função Original")
            st.latex(f"f({var_indep}) = {sp.latex(f)}")
            
            with st.spinner("Calculando derivada..."):
                resultado = sp.diff(f, x_sym, n)
                notacao = rf"\frac{{d^{{{n}}}}}{{d{var_indep}^{{{n}}}}}" if n > 1 else rf"\frac{{d}}{{d{var_indep}}}"

        # --- SIMPLIFICAÇÃO INTELIGENTE COM 3 NIVEIS---
        if tipo_simplificacao == "Leve (Rápido)":
            resultado_final = resultado
        elif tipo_simplificacao == "Médio (Cancel)":
            resultado_final = sp.cancel(resultado)
        else:
            resultado_final = sp.simplify(resultado)

        # --- EXIBIÇÃO DO RESULTADO ---
        st.divider()
        st.subheader(f"🎯 Resultado da {n}ª Derivada")

        latex_resultado = sp.latex(resultado_final)

        # Proteção contra strings gigantes que travam o navegador
        if len(latex_resultado) > 1000:
            st.warning("⚠️ O resultado é muito complexo. Mostrando formato de código:")
            st.code(str(resultado_final), language="python")
        else:
            st.latex(f"{notacao} = {latex_resultado}")

    except Exception as erro:
        st.error(f"❌ Ocorreu um erro no processamento: {erro}")
        st.info("💡 Verifique se esqueceu algum sinal de '*' ou se as variáveis coincidem com as selecionadas na barra lateral.")

if __name__ == "__main__":
    calculadora()