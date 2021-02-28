def invoice_totals(orders, minimum): return list(map(lambda x: (x[0], (lambda price: price + (10 if price < minimum else 0))(x[2] * x[3])), orders)) # "os one-liners do Miguel" :(
