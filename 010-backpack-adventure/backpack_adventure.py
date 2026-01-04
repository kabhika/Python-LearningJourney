# Backpack Adventure - Learning List Operations
# Date: December 2024

print("=" * 50)
print("BACKPACK ADVENTURE - A List Operations Story")
print("=" * 50)
print()

# Start with empty backpack (empty list)
backpack = []
print("0. Starting a journey with an Empty Backpack")
print("Backpack:", backpack)
print("-" * 50)

# 1. Pickup Starter Kit items - using append()
print("1. Picking up starter kit (Armour, Shield, Sword, Potion)")
backpack.append('Armour')
backpack.append('Shield')
backpack.append('Sword')
backpack.append('Potion')
print("Backpack:", backpack)
print("-" * 50)

# 2. Loot a treasure chest - using extend()
print("2. Looting a treasure chest!")
chest = ['Map', 'Potion', 'Compass', 'Potion']
backpack.extend(chest)
print("Backpack:", backpack)
print("-" * 50)

# 3. Visit to a merchant - using remove() and index()
print("3. Visiting merchant")
print("   Selling Shield and upgrading Sword to Great Magic Sword")
backpack.remove('Shield')
sword_index = backpack.index('Sword')
backpack[sword_index] = 'Great Magic Sword'
print("Backpack:", backpack)

# Count items
total_count = len(backpack)
unique_count = len(set(backpack))
print(f"   Total items: {total_count}")
print(f"   Unique items: {unique_count}")
print("-" * 50)

# 4. Items stolen by a thief - using pop()
print("4. A thief stole 2 items!")
stolen_item_1 = backpack.pop(2)
stolen_item_2 = backpack.pop()
print(f"   Stolen: {stolen_item_1}, {stolen_item_2}")
print("Backpack:", backpack)
print("-" * 50)

# 5. Found a hidden stash - using insert() and append()
print("5. Found a hidden stash behind a rock!")
ring = 'Ring of Invisibility'
gold_pouch = ['Gold Coins', 'Gold Bracelet', 'Gold Necklace']
backpack.insert(2, ring)
backpack.append(gold_pouch)
print("Backpack:", backpack)
print("-" * 50)

# 6. Half items teleported - using slicing
print("6. Half of the items teleported to a safe location!")
count = len(backpack)
half_count = count // 2
teleported_items = backpack[:half_count]
backpack = backpack[half_count:]
print(f"   Teleported: {teleported_items}")
print("Backpack:", backpack)
print(f"   Items remaining: {len(backpack)}")
print("-" * 50)

print()
print("=" * 50)
print("ADVENTURE COMPLETE!")
print("=" * 50)
