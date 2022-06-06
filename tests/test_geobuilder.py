

def test_distance_matrix(geo, origin):
    return geo.get_fastest_route(origin, time_range=["11:00am", "1:00pm"])
    