

def insert_matches(supabase, matches, batch_size=200):
    # Obter todos os IDs que queremos inserir
    match_ids = [match['id'] for match in matches]

    # Buscar IDs existentes no banco (em lote)
    existing_ids = []
    for i in range(0, len(match_ids), batch_size):
        batch_ids = match_ids[i:i+batch_size]
        result = supabase.table('matches').select('id').in_('id', batch_ids).execute()
        existing_ids += [item['id'] for item in result.data]

    # Filtrar apenas os novos jogos (que não existem no banco)
    new_matches = [match for match in matches if match['id'] not in existing_ids]

    print(f"Total de jogos novos para inserir: {len(new_matches)}")

    # Inserir novos jogos em lotes
    for i in range(0, len(new_matches), batch_size):
        batch = new_matches[i:i+batch_size]
        supabase.table('matches').insert(batch).execute()
        print(f'{len(batch)} jogos inseridos com sucesso.')