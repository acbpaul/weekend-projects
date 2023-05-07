# -*- coding: utf-8 -*-
"""
Created on Sat May  6 16:40:52 2023

@author: adr_paul
"""

import pdfplumber
import pandas as pd
import re

def fuvest_extract_pdf_text(file_path):
    """
    Extrai o texto de um arquivo PDF, dividindo cada página em duas colunas e 
    removendo números de página no formato '<Page:nb>'.
    
    Args:
        file_path (str): Caminho para o arquivo PDF.
    
    Returns:
        text (str): Texto extraído do PDF.
    """
    text = ''
    
    with pdfplumber.open(file_path) as pdf:

        pages = len(pdf.pages)
        pages = range(len(pdf.pages[1:]))
        
        for i in pages:
            page = pdf.pages[i]

            # Obter a área de interesse da página
            page_width = page.width
            page_height = page.height
            header_height = 30  # Ajuste este valor para corresponder à altura do cabeçalho em pontos

            # Dividir a página em duas metades (esquerda e direita)
            left_half = page.crop((0, header_height, page_width / 2, page_height))
            right_half = page.crop((page_width / 2, header_height, page_width, page_height))

            # Extrair texto de ambas as metades
            left_text = left_half.extract_text()
            right_text = right_half.extract_text()

            # Combinar o texto das duas metades da página
            text += '\n' + str(page) + '\n'
            text += left_text + '\n' + right_text

            # Remover números de página no formato '<Page:xx>'
            text = re.sub(r'<Page:\d{1,2}>\n', '', text)

    return text






def fuvest_process_text(text):
    """
    Processa o texto extraído do PDF  das provas da Fuvest e converte-o 
    em um DataFrame com as seguintes colunas:
        ['Questao Nr', 'Questao', 'A', 'B', 'C', 'D', 'E'].

    Args:
        text (str): Texto extraído do PDF.

    Returns:
        df (pd.DataFrame): DataFrame contendo as questões e suas alternativas.
    """

    colunas = ['Questao Nr', 'Questao', 'A', 'B', 'C', 'D', 'E']
    df = pd.DataFrame(columns=colunas)

    for question_number in range(1, 91):
        # Construa os padrões regex para o número da questão atual e o próximo número.
        question_pattern = r'\b{:02d}\n'.format(question_number)
        next_question_pattern = r'\b{:02d}\n'.format(question_number + 1)

        # Encontre a posição inicial das questões atual e seguinte no texto.
        question_start = re.search(question_pattern, text)
        next_question_start = re.search(next_question_pattern, text)

        if question_start is not None:
            question_start_pos = question_start.end()

            # Encontre a posição final da questão atual no texto.
            question_end_pos = next_question_start.start() if next_question_start is not None else len(text)

            # Extraia o texto da questão e remova as quebras de linha.
            question_text = text[question_start_pos:question_end_pos].strip().replace('\n', ' ').replace('\r', '')

            # Encontre a posição das alternativas (A) a (E) no texto da questão.
            answer_B_pos = re.search(r'\(B\)', question_text)
            answer_C_pos = re.search(r'\(C\)', question_text)
            answer_D_pos = re.search(r'\(D\)', question_text)
            answer_E_pos = re.search(r'\(E\)', question_text)

            # Extraia as alternativas e remova as quebras de linha.
            answer_A = question_text[4:answer_B_pos.start()].strip()
            answer_B = question_text[answer_B_pos.end():answer_C_pos.start()].strip()
            answer_C = question_text[answer_C_pos.end():answer_D_pos.start()].strip()
            answer_D = question_text[answer_D_pos.end():answer_E_pos.start()].strip()
            answer_E = question_text[answer_D_pos.end():].strip()

            # Crie um dicionário com os dados da questão e adicione-o ao DataFrame.
            question_data = {'Questao Nr': [question_number], 
                             'Questao': [question_text], 
                             'A': [answer_A], 
                             'B': [answer_B], 
                             'C': [answer_C], 
                             'D': [answer_D], 
                             'E': [answer_E]}
            
            df1 = pd.DataFrame(question_data)
            df = pd.concat([df,df1], ignore_index=True)

            # Atualize o texto removendo a questão atual.
            if question_number < 90:
                text = text[next_question_start.start():]

    return df


file_path = r"C:\Users\adr_p\Desktop\Provas\Fuvest\fuvest2023_primeira_fase_prova_V.pdf"
pdf_text = fuvest_extract_pdf_text(file_path)  

df = fuvest_process_text(pdf_text)

print(df.head())

