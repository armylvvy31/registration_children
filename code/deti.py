def create_kid_record(line):
    parts = line.strip().split(';')
    if len(parts) < 10:
        return None
    



def create_kid_record(line):
    if not line.strip():
        return None
    parts = line.strip().split(';')



    ok_count = 0
    for i in range(6, 10):
        if parts[i] == "здоров":
            ok_count += 1
    kid_record = {
        'surname': parts[0],
        'name': parts[1],
        'year': int(parts[2]),
        'month': int(parts[3]),
        'day': int(parts[4]),
        'group': parts[5],
        'health_results': parts[6:10],
        'health_score': ok_count
    }
    return kid_record
