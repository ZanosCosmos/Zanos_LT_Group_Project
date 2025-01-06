from enum import Enum

class DatabaseType(Enum):
  CONSTANTS = 1
  TEAMS = 2
  STATS = 3
  EQUATIONS = 4
  MCOST = 5
  TERRAIN = 6
  MINIMAP = 7
  WEAPON_RANKS = 8
  WEAPONS = 9
  FACTIONS = 10
  ITEMS = 11
  SKILLS = 12
  TAGS = 13
  GAME_VAR_SLOTS = 14
  CLASSES = 15
  SUPPORT_CONSTANTS = 16
  SUPPORT_RANKS = 17
  AFFINITIES = 18
  UNITS = 19
  SUPPORT_PAIRS = 20
  PARTIES = 21
  AI = 22
  DIFFICULTY_MODES = 23
  OVERWORLDS = 24
  LEVELS = 25
  EVENTS = 26
  TRANSLATIONS = 27
  LORE = 28
  RAW_DATA = 29