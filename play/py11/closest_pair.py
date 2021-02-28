def closest_pair(points, math=__import__('math'), itertools=__import__('itertools')): return round(min(math.dist(*x) for x in itertools.combinations(points, 2)))
