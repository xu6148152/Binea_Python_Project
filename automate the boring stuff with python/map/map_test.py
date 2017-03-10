import pprint


def displayInventory(map):
    total = 0   
    for key, value in map.items():
        total += value
        print(str(value) + ", " + key)
    print(str(total))
	print('')


def addToInventory(inventory, addedItems):
    for item in addedItems:
        if item in inventory.keys():
            value = inventory.get(item)
            value += 1
            inventory[item] = value
        else:
            inventory.setdefault(item, 1)


if __name__ == '__main__':
    map = {'arrow': 12, 'gold coin': 42, 'rope': 1, 'torch': 8, 'dagger': 1}
    dragLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
    inv = {'gold coin': 42, 'rope': 1}
    addToInventory(inv, dragLoot)
    displayInventory(inv)
