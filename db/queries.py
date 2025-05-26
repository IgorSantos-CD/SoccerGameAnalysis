import pandas as pd

def select_supabase(
    supabase,
    nome_tabela,
    colunas="*",
    filtros=None,
    order_by=None,
    limit=None,
    offset=None
):
    """
    Função para selecionar dados do Supabase com filtros e parâmetros opcionais.

    Parâmetros:
    - supabase: cliente Supabase.
    - nome_tabela: nome da tabela ou VIEW.
    - colunas: lista de colunas ou "*" (padrão).
    - filtros: lista de dicionários para filtros, exemplo:
        [{"coluna": "status", "operador": "eq", "valor": "FINISHED"}]
    - order_by: coluna para ordenar (string ou lista).
    - limit: número máximo de registros.
    - offset: número de registros a pular (para paginação).

    Retorna:
    - Lista de registros (dicionários).
    """
    try:
        query = supabase.table(nome_tabela).select(colunas)
        
        # Aplicar filtros
        if filtros:
            for f in filtros:
                coluna = f.get("coluna")
                operador = f.get("operador", "eq")
                valor = f.get("valor")
                
                if operador == "eq":
                    query = query.eq(coluna, valor)
                elif operador == "gt":
                    query = query.gt(coluna, valor)
                elif operador == "lt":
                    query = query.lt(coluna, valor)
                elif operador == "gte":
                    query = query.gte(coluna, valor)
                elif operador == "lte":
                    query = query.lte(coluna, valor)
                elif operador == "like":
                    query = query.like(coluna, valor)
                elif operador == "ilike":
                    query = query.ilike(coluna, valor)
                elif operador == "neq":
                    query = query.neq(coluna, valor)
                # outros operadores podem ser adicionados conforme necessário

        # Ordenação
        if order_by:
            if isinstance(order_by, list):
                for col in order_by:
                    query = query.order(col)
            else:
                query = query.order(order_by)

        # Limite e Offset
        if limit is not None:
            query = query.limit(limit)
        if offset is not None:
            query = query.offset(offset)

        result = query.execute()
        result = pd.DataFrame(result.data)
        return result

    except Exception as e:
        print(f"Erro ao executar select: {e}")
        return []