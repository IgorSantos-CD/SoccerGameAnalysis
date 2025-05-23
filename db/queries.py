
def select_supabase(supabase, nome_tabela, colunas="*", condicao=None):
    """
    Função para selecionar dados do Supabase com condição opcional.

    Parâmetros:
    - supabase: cliente Supabase
    - nome_tabela: nome da tabela
    - colunas: colunas a serem selecionadas (padrão "*")
    - condicao: dicionário {"coluna": "valor"} para aplicar filtro (opcional)
    """
    query = supabase.table(nome_tabela).select(colunas)
    
    if condicao:
        for coluna, valor in condicao.items():
            query = query.eq(coluna, valor)
    
    result = query.execute()
    return result.data
