import random

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.gold = 0
    
    def is_alive(self):
        return self.health > 0
    
    def take_damage(self, damage):
        self.health -= damage
        print(f"💥 You took {damage} damage! Health: {self.health}")
    
    def add_item(self, item):
        self.inventory.append(item)
        print(f"📦 Added {item} to inventory!")
    
    def show_status(self):
        print(f"\n{'='*40}")
        print(f"👤 {self.name}")
        print(f"❤️ Health: {self.health}")
        print(f"💰 Gold: {self.gold}")
        print(f"📦 Inventory: {self.inventory}")
        print(f"{'='*40}\n")

class Room:
    def __init__(self, name, description, enemies=None, items=None, gold=None):
        self.name = name
        self.description = description
        self.enemies = enemies or []
        self.items = items or []
        self.gold = gold or 0
        self.explored = False

class AdventureGame:
    def __init__(self):
        self.player = None
        self.rooms = {}
        self.current_room = None
    
    def setup_game(self):
        # Create rooms
        self.rooms = {
            'entrance': Room('Entrance', 'You enter a dark cave...', 
                          items=['torch'], gold=10),
            'forest': Room('Mysterious Forest', 'Trees everywhere, birds singing...',
                          enemies=['wolf'], items=['apple'], gold=20),
            'castle': Room('Old Castle', 'A huge castle door stands before you...',
                          enemies=['dragon'], items=['sword', 'gold coin'], gold=100),
            'treasure': Room('Treasure Room', 'Gold and jewels everywhere!',
                          items=['crown', 'magic gem'], gold=500)
        }
    
    def start(self):
        print("🎮 Welcome to TEXT ADVENTURE! 🎮")
        name = input("Enter your name: ")
        self.player = Player(name)
        self.setup_game()
        self.current_room = self.rooms['entrance']
        self.play()
    
    def play(self):
        while self.player.is_alive():
            self.player.show_status()
            self.explore_room()
            
            command = input("\nWhat do you do? (explore/fight/take/go/quit): ").lower()
            
            if command == 'explore':
                self.explore_room()
            elif command == 'fight':
                self.fight_enemies()
            elif command == 'take':
                self.take_items()
            elif command == 'go':
                self.move_room()
            elif command == 'quit':
                print("👋 Thanks for playing!")
                break
        
        if not self.player.is_alive():
            print("\n💀 YOU DIED! Game Over 💀")
    
    def explore_room(self):
        if not self.current_room.explored:
            print(f"\n📍 {self.current_room.name}")
            print(self.current_room.description)
            self.current_room.explored = True
            
            if self.current_room.enemies:
                print(f"⚠️  Enemies nearby: {self.current_room.enemies}")
            if self.current_room.items:
                print(f"📦 Items available: {self.current_room.items}")
            if self.current_room.gold > 0:
                print(f"💰 Gold found: {self.current_room.gold}")
    
    def fight_enemies(self):
        if not self.current_room.enemies:
            print("😌 No enemies here!")
            return
        
        enemy = self.current_room.enemies[0]
        damage = random.randint(10, 30)
        self.player.take_damage(damage)
        
        if self.player.health > 0:
            print(f"⚔️  You defeated the {enemy}!")
            self.player.gold += len(self.current_room.enemies) * 10
            self.current_room.enemies = []
    
    def take_items(self):
        if not self.current_room.items:
            print("📭 Nothing to take here!")
            return
        
        for item in self.current_room.items:
            self.player.add_item(item)
        self.current_room.items = []
    
    def move_room(self):
        print("\nAvailable rooms: entrance, forest, castle, treasure")
        destination = input("Where to go? ").lower()
        
        if destination in self.rooms:
            self.current_room = self.rooms[destination]
        else:
            print("❌ Invalid location!")

# Run the game
game = AdventureGame()
game.start()