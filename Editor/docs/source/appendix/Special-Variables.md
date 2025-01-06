(Special-Variables)=
# Special Variables

_Last updated v0.1_

This appendix details every special game or level variable used by the **Lex Talionis** engine. Normally, game and level variables are utilized by the game designer in events, but a special set of names are reserved by the engine for specific uses.

## Format:

`command` **type** description

## Game Variables

These variables are saved for the entirety of a given game.

`_random_seed` **int** The random seed used by the engine for combat RNG and random level ups. Automatically set to a number between 0 and 1023 upon creation of a "New Game".

`_next_level_nid` **Level (str)** Internal to the engine; Do not modify yourself.

`_goto_level` **Level (str)** Set to the nid of the level you want to go to next. If not set, the engine will just move to the following level like normal. Reset upon the start of the next level. If set to `_force_quit`, game will end (and return to title screen) instead of moving to the following level.

`_go_to_overworld_nid` **Overworld (str)** Set to the nid of the overworld to go to next.

`_current_turnwheel_uses` **int** The number of uses of the turnwheel left in this level. Defaults to -1, which represents infinite uses. Automatically reset to `_max_turnwheel_uses` upon winning the a level.

`_max_turnwheel_uses` **int** The maximum number of uses of the turnwheel the player has access to. Defaults to -1, which represents infinite uses.

`_convoy` **bool** Set to True to give the player access to the convoy.

`_turnwheel` **bool** Set to True to give the player access to the turnwheel.

`_supports` **bool** Set to True to give the player access to support conversations and have characters gain support points.

`_minimap` **bool** Set to True to give the player access to the minimap. Set to False to remove player access of the minimap. Defaults to True.

`_fatigue` **int** Set to 0 to turn off fatigue. Set to 1 to have fatigue prevent unit from participating in a chapter. Set to 2 to have fatigue apply a Fatigued status when fatigue >= max fatigue and Rested when fatigue < max fatigue. Set to 3 to have the engine track fatigue but not do anything with it by default.

`_repair_shop` **bool** Set to True to give the player access to the repair shop in the prep and base menus.

`_prep_market` **bool** Set to True to give the player access to the market in the prep screen.

`_prep_music` **Music (str)** Set this music as the background music in the prep screen. You don't normally need to set this manually, since it is set by the `prep` event command.

`_base_market` **bool** Set to True to give the player access to the market in the base screen.

`_base_bg_name` **Panorama (str)** Load this panorama as the background in the base screen. You don't normally need to set this 
manually, since it is set by the `base` event command.

`_base_music` **Music (str)** Set this music as the background music in the base screen. You don't normally need to set this manually, since it is set by the `base` event command.

`_bexp_menu_music` **Music (str)** Set this music as the background music in the bonus experience menu. You don't normally need to set this manually, since it is set by the `open_bexp_menu` event command.

`_phase_music_fade_ms` **int** Number of milliseconds the phase music will take to fade in. Defaults to 400 ms.

`_last_choice` **str** Always holds the most recent choice made by the player from using the `choice` event command.

## Level Variables

These variables are cleared after winning or losing the current level

`_win_game` **bool** Set to True to force the player to win the current level. Best practice is to just call the `win_game` event command, which does the same thing.

`_lose_game` **bool** Set to True to force the player to lose the current level. Best practice is to just call the `lose_game` event command, which does the same things.

`_level_end_triggered` **bool** Internal to the engine; Do not modify yourself.

`_fog_of_war` **bool** Determines whether there is a base fog of war

`_fog_of_war_type` **int** Defaults to 0
    0 - Entire map is revealed, but enemy positions are masked (like in the GBA)
    1 - Entire map is revealed, but enemy positions are masked (like in the GBA) (yes, these are identical for past compatibility reasons)
    2 - Both map and enemy positions are masked (like in Thracia)
    3 - Both map and enemy positions are masked at the start, but the map stays revealed after exploring it

`_fog_of_war_radius` **int** The distance that player units will be able to see in the fog. Defaults to 0.

`_ai_fog_of_war_radius` **int** The distance that ai units will be able to see in the fog. If not set, defaults to `_fog_of_war_radius`

`_other_fog_of_war_radius` **int** The distance that other team units will be able to see in the fog. If not set, defaults to `_ai_fog_of_war_radius`

`_prep_pick` **bool** Set to True to enable "Pick Units" in the prep screen. You don't normally need to set this manually, since it is set by the `prep` event command.

`_prep_slots` **int** Limits the number of units that can be brought to the level. Used only when you want to limit the number of player units to a number lower than the number of Formation tiles. Defaults to None.

`_minimum_deployment` **int** Must deploy at least this many units during the Prep Screen. If you have less units that this, must deploy all units.
