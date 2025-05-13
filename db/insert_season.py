def insert_seasons(supabase, seasons):
    for season in seasons:
        existing = supabase.table('seasons').select("id").eq('id',season['id']).execute()
        if len(existing.data) == 0:
            supabase.table('seasons').insert(season).execute()
            print("Temporada incluida com sucesso")
        else:
            print(f'Temporada {season["start_date"]} já existe no banco')
