#Superhero_team_dueler
Instructions!:
  Enter Team 1 name.
  Enter how many heroes you want on the team.
  Enter name(s) of the heroes.
  Enter any abilities, weapons, armors that you want each hero to have.
  Do the same steps above for Team 2.

Result:
  Winner.
  List of surviving heroes.
  Kill/Death Ratio for each team.

#PseudoCode that guided me throughout the project
Hero class

  defend method:
    use armor to defend against attack.
    runs 'block' method on each armor.
    returns sum of all blocks
    for each armor in list
      run 'block' method
    return sum of all blocks

  take_damage method:
    Subtract take_damage from self.current_health after subtracting the value
    received from calling self.defend.

  is_alive method:
    return True if hero is still alive.
    return False if hero is dead.
    if current_health is equal to 0,
      return True
    else
      return False  

  fight method:
    while both  heroes are is_alive:
      call take_damage method for both opponents
      if is_alive is false for either one:
        return the winner's  name
      if there's no abilities in either Hero:
        print Draw!

  Arena class

    create_ability method:
      Allow user to create new ability.
      Ask user for necessary info to create new ability object.
      return ability object.

    create_hero method:
      Ask for hero name.
      Ask if user wants abilities, weapons, armors for hero.
      Ask user input info for abilities, weapons, and armors.
      Call the methods for abilities, weapons, and armors.
        create_ability
        create_weapon
        create_armor
      return Hero

  Team class

    def heroes_alive:
      gives a list of heroes that are still alive .

    def attack:
      team1 fights team2 based on random choice of the heroes_alive list.
      team1 fights team2.
