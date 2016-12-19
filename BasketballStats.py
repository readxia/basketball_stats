from Player import Player

player=Player("Read")
player.shoot(3, True)
player.shoot(2, False)
player.shoot(2, False)
player.shoot(2, True)
player.rebound(False, 2)
player.rebound(True, 1)
player.print_stats()
