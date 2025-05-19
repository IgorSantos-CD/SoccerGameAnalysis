def insert_teams(supabase, teams):
    for team in teams:
        existing = supabase.table('teams').select("id").eq('id', team['id']).execute()
        if len(existing.data) == 0:
            supabase.table('teams').insert(team).execute()
            print("Time incluido com sucesso")
        else:
            print(f'Time {team["id"]} já existe no banco')