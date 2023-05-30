import streamlit as st
import numpy as np

st.title("Inserir Arrays Quadrados")

ordem = st.number_input("Ordem do Array", min_value = 2, value = 2, step = 1)

array = [[]for _ in range(ordem)]
termo_independente = []

st.header(f"Array de Ordem {ordem}x{ordem}")
for i in range(ordem):
    for j in range(ordem):
        passa_valores_do_array = st.number_input(f"Elemento [{i+1}, {j+1}]", value = 0.0)
        array[i].append(passa_valores_do_array)

st.header("Termos independentes")
for j in range(ordem):
    passa_termo_independente = st.number_input(f"Elemento [{j + 1}]", value = 0.0)
    termo_independente.append(passa_termo_independente)

st.write("Array Resultante:")
st.dataframe(array)

st.write("Array Termo independente:")
st.dataframe(termo_independente)

if st.button("Executar"):
    A = array
    B = termo_independente
    st.write("Atualização")
    def substituicoe_retroativas(A, B):
        n = len(A)

        x = n * [0]

        for i in range(n-1, -1, -1):
            

            S = 0
            for j in range(i+1, n):
                st.write("Método de Gauss")
                st.dataframe(A)
                st.dataframe(B) 
                S = S + A[i][j] * x[j]
            x[i] = (B[i] - S)/ A[i][i]
        
        st.write("Representação final")
        st.dataframe(A)
        st.dataframe(B)
        return x

    st.write("Atualização do array:")
    def gauss(A, B):
        n = len(A)
        for k in range(0, n-1):
            st.write("Triangularização")
            st.dataframe(A)
            st.dataframe(B)

            for i in range(k+1, n):
                m = - A [i][k]/A[k][k]

                for j in range(k+1, n):
                    A[i][j] = m * A[k][j] + A[i][j]

                B[i] = m * B[k] + B[i]
                A[i][k] = 0
                

        st.write("Triangulado")
        st.dataframe(A)
        st.dataframe(B)

        x = substituicoe_retroativas(A, B)
        return x


    j = gauss(A, B)

    st.write("Resultado:")
    st.dataframe(j)