from typing import Tuple

living_room_switch_id = "e70207e80c0b11ebaf5719ccebfd3949"
living_room_retro_lamp_id = 'light.living_room_retro_lamp'
living_room_corner_lamp_id = 'light.living_room_corner_lamp'
living_room_motion_sensor_id = "binary_sensor.living_room_motion"
living_room_speaker = "media_player.living_room_speaker"

bath_room_switch_id = "9b3e76b9ecc6f0da93331aae0a3b5d61"
bath_room_lamp_id = "light.bathroom_lamp"
bath_room_motion_sensor_id = "binary_sensor.bathroom_motion"
bath_room_speaker = "media_player.bathroom_speaker"
bath_room_motion_activation_boolean = "input_boolean.bath_room_motion_activation_boolean"

bed_room_switch_id = "6478c2810af711ebad38135e2ad28f01"
bed_room_head_lamp_id = "light.bedroom_head_light"
bed_room_night_switch_id = "aba7647ac6470849cea271f62559e2db"
bed_room_night_lamp_id = "light.bedroom_night_lamp"
bed_room_speaker = "media_player.bedroom_speaker"

kitchen_switch_id = "c7c68a1be32ca26a7050e4f5937ee1c9"
kitchen_lamp_id = "light.kitchen_lamp"
kitchen_motion_sensor_id = "binary_sensor.kitchen_motion"
kitchen_speaker = "media_player.kitchen_speaker"
kitchen_motion_activation_boolean = 'input_boolean.kitchen_motion_activation_boolean'


motion_sensor_deactivated_message: Tuple[str, str] = ('Motion sensor deactivated', 'en')
motion_sensor_activated_message: Tuple[str, str] = ('Motion sensor activated', 'en')