

def insert_competitions(supabase, base):
    for comp in base:
        comp_data = {
            "id" : comp['id'],
            "name" : comp['name'],
            "code" : comp['code'],
            "area_name" : comp['area']['code']
        }

        existing = supabase.table('competitions').select("id").eq('id',comp_data['id']).execute()
        if len(existing.data) == 0:
            supabase.table('competitions').insert(comp_data).execute()
            print("Competição incluida com sucesso")
        else:
            print(f'Competição {comp_data["name"]} já existe no banco')