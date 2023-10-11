menu = ["burgers", "warps", "hot dogs", "salads", "cokes", "coffees", "orange juices", "french fries", "onion rings" ]
order = []
combo = []
for i in menu:
    a = input(f"How many {i} would you like to order? ")
    for j in range(int(a)):
        order.append(i)
c = ["burgers", "warps", "hot dogs", "salads"]
abcd = ["Combo A", "Combo B", "Combo C", "Combo D"]
k = 0
for i in c:
    print(i)
    for j in range(order.count(i)):
        v = abcd[k]
        if i in order:
            if "onion rings" in order:
                if "coffees" in order:
                    order.remove(i)
                    order.remove("onion rings")
                    order.remove("coffees")
                    combo.append(v)
                elif "cokes" in order:
                    order.remove(i)
                    order.remove("onion rings")
                    order.remove("cokes")
                    combo.append(v)
                elif "orange juices" in order:
                    order.remove(i)
                    order.remove("onion rings")
                    order.remove("orange juices")
                    combo.append(v)
            elif "french fries" in order:
                if "coffees" in order:
                    order.remove(i)
                    order.remove("french fries")
                    order.remove("coffees")
                    combo.append(v)
                elif "cokes" in order:
                    order.remove(i)
                    order.remove("french fries")
                    order.remove("cokes")
                    combo.append(v)
                elif "orange juices" in order:
                    order.remove(i)
                    order.remove("french fries")
                    order.remove("orange juices")
                    combo.append(v)
    k += 1


final = []
total = 0
final.append("COMBOS")
if "Combo A" in combo:
    n = combo.count("Combo A")
    final.append(f"Combo A------------------------------------ $5.50 x {n} = ${(5.50 * n):.2f}")
    total += (5.50 * n)
if "Combo B" in combo:
    n = combo.count("Combo B")
    final.append(f"Combo B------------------------------------ $4.50 x {n} = ${(4.50 * n):.2f}")
    total += (4.50 * n)
if "Combo C" in combo:
    n = combo.count("Combo C")
    final.append(f"Combo C------------------------------------ $4.00 x {n} = ${(4.00 * n):.2f}")
    total += (4.00 * n)
if "Combo D" in combo:
    n = combo.count("Combo D")
    final.append(f"Combo D------------------------------------ $3.50 x {n} = ${(3.50 * n):.2f}")
    total += (3.50 * n)

final.append("INDIVIDUAL ITEMS")
order1 = set(order)

for i in order1:
    n = order.count(i)
    if i == "burgers":
        final.append(f"Burgers------------------------------------ $3.99 x {n} = S{(3.99 * n):.2f}")
        total += (3.99 * n)
    elif i == "warps":
        final.append(f"Wraps-------------------------------------- $3.00 x {n} = S{(3.00 * n):.2f}")
        total += (3.00 * n)
    elif i == "salads":
        final.append(f"Salads------------------------------------- $2.50 x {n} = S{(2.50 * n):.2f}")
        total += (2.50 * n)
    elif i == "hot dogs":
        final.append(f"Hotdogs------------------------------------ $2.00 x {n} = S{(2.00 * n):.2f}")
        total += (2.00 * n)
    elif i == "coffees":
        final.append(f"Coffee-------------------------------------- $1.50 x {n} = S{(1.50 * n):.2f}")
        total += (1.50 * n)
    elif i == "french fries":
        final.append(f"French Fries-------------------------------- $1.50 x {n} = S{(1.50 * n):.2f}")
        total += (1.50 * n)
    elif i == "onion rings":
        final.append(f"Onion Rings--------------------------------- $1.50 x {n} = S{(1.50 * n):.2f}")
        total += (1.50 * n)
    elif i == "cokes":
        final.append(f"Cokes--------------------------------------- $1.00 x {n} = S{(1.00 * n):.2f}")
        total += (1.00 * n)
    elif i == "orange juices":
        final.append(f"Orange Juice-------------------------------- $1.00 x {n} = S{(1.00 * n):.2f}")
        total += (1.00 * n)
final.append(f"TOTAL------------------------------------------------------------------- ${total}")

for u in final:
    print(u)

