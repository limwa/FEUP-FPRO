# o Pedro Balazeiro copiou a minha solução kekw
def knapsack(budget, prices, wishlist): return max(((lambda price: (price, { k: v for k, v in comb if v > 0 }) if price <= budget else (0, {}))(sum(x[1] * prices[x[0]] for x in comb)) for comb in (comb for comb in __import__('itertools').combinations([(name, i) for name, amm in wishlist.items() for i in range(amm + 1)], len(wishlist)) if len(dict(comb)) == len(comb))), key=lambda x: x[0])[1]
