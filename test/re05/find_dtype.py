def find_dtype(a_tuple, data_type):
    return tuple([data for data in a_tuple if type(data) == data_type])
