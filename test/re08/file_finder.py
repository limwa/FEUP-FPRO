def file_finder(dirs, file_name): return f"{dirs[0]}/{file_name}" if file_name in dirs[1:] else dirs[0] + '/' + "".join([l for l in [file_finder(i, file_name) for i in dirs[1:] if isinstance(i, list)] if l is not None and len(l) > 0]) if len([l for l in [file_finder(i, file_name) for i in dirs[1:] if isinstance(i, list)] if l is not None and len(l) > 0]) > 0 else None # "os one-liners do Miguel" :(