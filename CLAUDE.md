# Home Assistant Configuration - CLAUDE.md

## Overview
This repository contains a comprehensive Home Assistant configuration for an automated smart home system. The setup manages lights, windows, heating, a Roborock S7 vacuum (with auto-emptying dock), music through Sonos speakers, and extensive convenience features with AI-powered interactions.

## Key Features
- **Advanced Presence Detection**: Room-by-room presence tracking using motion sensors with exponential backoff timers
- **Intelligent Vacuum Management**: Automated Roborock S7 cleaning with queuing system and room-specific scheduling
- **AI-Powered Interactions**: Welcome/goodbye messages with context-aware ChatGPT integration
- **Music Following**: Sonos speakers follow user presence throughout the home
- **Comprehensive Automation**: 100+ automations across lighting, heating, windows, and convenience features

## Repository Structure

### Core Configuration Files
- `ui-lovelace.yaml` - Main dashboard configuration
- `custom_*.yaml` - Custom sensors, templates, lights, media players, and input helpers
- `groups.yaml` - Device groupings
- `dashboard_layout.md` - Visual dashboard layout documentation for UI reference

### Automation Structure
```
automations/
├── presence/          # Room-based presence detection (10 rooms)
├── light/             # Automated lighting per room
├── heating/           # Climate control automations
├── speakers/          # Music following and control
├── windows/           # Window state management
├── vacuum.yaml        # Roborock S7 automation
├── welcome.yaml       # AI-powered greetings
├── go_to_bed.yaml     # Bedtime routines
└── system.yaml        # System monitoring
```

### Scripts and Helpers
```
scripts/
├── presence/          # Room presence management
├── light/             # Lighting control scripts
├── heating/           # Climate control
├── tts/               # AI text generation
├── vacuum.yaml        # Vacuum control and queuing
└── notifications.yaml # Telegram notifications
```

### Blueprints
Custom automation blueprints for:
- Advanced presence detection with exponential backoff
- Motion-based room presence
- Music following automation
- Vacuum control buttons
- Window management

## Device Inventory

### Motion Sensors
- **Aqara FP2 Motion Sensor**: Advanced presence detection in living room only
  - **Entity**: `binary_sensor.couch_motion_fp2`
  - **Features**: Precise presence detection, instant on/off response
- **Aqara PIR Motion Sensors**: Binary motion detection in other rooms
  - **Entity Pattern**: `binary_sensor.{room}_motion`
  - **Rooms Covered**: bed_room, kitchen, bath_room, office, toilet, hallway, entrance, bar, dining_room
  - **Important Caveat**: After triggering, sensors remain in "on" state for ~60 seconds before turning off
  - **Impact**: Requires timer-based presence detection to handle the 60-second delay

### Vacuum System
- **Model**: Roborock S7 with auto-emptying dock
- **Entity**: `vacuum.roborock_s7`
- **Features**: Room-specific cleaning, queuing system, auto-emptying
- **Room Mapping**: 10 rooms with segment IDs (16-25)

### Speakers
- **System**: Sonos speakers throughout the home
- **Rooms**: living_room, kitchen, bath_room, office
- **Features**: Music following, TTS announcements, zone control

### Lights
- **Coverage**: All rooms with automated control
- **Features**: Presence-based automation, scene control, brightness adjustment
- **Special**: Light bar with advanced controls
- **Bath Room**: Controlled by Shelly 1 (no color/brightness control)
- **Kitchen**: 3 IKEA lights grouped as one entity

### Climate Control
- **Rooms**: bed_room, living_room, bath_room, office
- **Features**: Presence-based heating, window-open detection, scheduled pre-heating

### Windows
- **Monitored Rooms**: bed_room, living_room, kitchen, bath_room, office
- **Features**: Open/closed detection, air freshness monitoring, heating integration

### Additional Devices
- **LG TV**: `media_player.lg_tv` with presence locking
- **Door Bell**: Entrance monitoring
- **Humidifier**: Automated control
- **Various Switches**: Room-specific switch controls

## Automation Patterns

### Presence Detection System
- **Advanced Multi-Timer System**: Uses exponential backoff for presence detection
- **PIR Sensor Challenge**: Most rooms use PIR sensors with 60-second "on" state after motion
- **Timer-Based Solution**: Presence timers compensate for PIR sensor limitations
- **Living Room Exception**: FP2 sensor provides instant, precise presence detection
- **Lock Mechanism**: Prevents false negatives (TV watching, sleeping)
- **Statistics Tracking**: Weekly presence statistics per room
- **Mutual Exclusion**: Only one room can have presence at a time

### Vacuum Management
- **Intelligent Scheduling**: Starts when nobody is home (10-minute delay)
- **Room Prioritization**: Cleans "dirty" rooms first based on last cleaned time
- **Queuing System**: Manages multiple cleaning requests
- **Auto-Emptying**: Integrated with dock's auto-empty feature
- **Maintenance Alerts**: Water refill and dustbin empty notifications

### AI Integration
- **Welcome Messages**: Context-aware greetings with vacuum status, time-of-day
- **Goodbye Messages**: Weather-based reminders, window alerts, trash reminders
- **Conversation ID**: `01HZN5A3AE56FDKRNQ0CPJPXYW` for consistent AI context
- **Agent ID**: `f5473f5d0996f8f420405ee483c0302c`

### Music Following
- **Automatic Speaker Selection**: Music follows user presence
- **Zone Management**: Seamless transitions between rooms
- **Volume Control**: Context-aware volume adjustment

## Deployment Workflow

### Sync Scripts
The `config/` directory contains deployment scripts:
- `sync_to_host.cmd` - Deploy configuration to Home Assistant host (192.168.178.26)
- `_sync_from_host.cmd` - Pull configuration from host
- `sync/` directory - Individual component sync scripts

### Host Configuration
- **Target Host**: 192.168.178.26
- **User**: lorenzo
- **Path**: /root/config/
- **Security**: Uses specific MAC algorithms for SCP transfers

## Important Entity Patterns

### Presence Entities
- `binary_sensor.{room}_presence` - Room presence state
- `input_boolean.{room}_presence_lock` - Presence lock mechanism
- `timer.{room}_presence` - Presence timeout timer
- `counter.{room}_presence_trigger` - Trigger counting for exponential backoff

### Vacuum Entities
- `vacuum.roborock_s7` - Main vacuum entity
- `todo.vacuum_queue` - Cleaning queue management
- `todo.last_vacuumed_rooms` - Recently cleaned rooms
- `input_datetime.{room}_last_vacuumed` - Last cleaned timestamps

### Helper Entities
- `input_boolean.automate_*` - Feature toggle switches
- `input_boolean.night_mode` - Night mode state
- `input_boolean.guest_mode` - Guest mode state
- `binary_sensor.home_presence` - Overall home presence

## Special Features

### Night Mode
- Disables certain automations during night hours
- Adjusts lighting and sound levels
- Prevents vacuum operation

### Guest Mode
- Modifies automation behavior for guests
- Adjusts privacy settings
- Maintains comfort while reducing intrusive automations

### Work Mode
- Optimizes environment for work
- Manages office heating and lighting
- Reduces distractions

### Statistics and Monitoring
- Weekly presence statistics for all rooms
- Air freshness monitoring
- Battery level tracking for sensors
- Vacuum performance metrics

## Development Notes

### Blueprint System
- Custom blueprints for repeatable automation patterns
- Parameterized room-specific configurations
- Modular approach to automation development

### Template System
- Extensive use of Jinja2 templates
- Dynamic entity generation
- Context-aware automation logic

### Variable Management
- Todo lists for dynamic data storage
- State persistence across restarts
- Queue management for complex operations

### API Testing and Development
- **REST API Access**: Home Assistant REST API available for testing automations
- **Configuration File**: `ha_secrets.json` contains API credentials (gitignored for security)
- **Base URL**: http://192.168.178.26:8123
- **Authentication**: Long-lived access token stored securely
- **Common API Patterns**:
  - Turn off lights: `POST /api/services/light/turn_off` with `{"entity_id": "light.entity_name"}`
  - Turn on lights: `POST /api/services/light/turn_on` with `{"entity_id": "light.entity_name"}`
  - Call services: `POST /api/services/{domain}/{service}` with entity parameters
- **Usage**: Useful for testing automation logic, debugging entity states, and rapid prototyping

## Troubleshooting

### Common Issues
1. **Vacuum Unavailable**: Auto-reload configuration after 10 minutes
2. **Presence Detection**: Check motion sensor batteries and positioning
3. **Sync Issues**: Verify network connectivity and SSH access to host

### Maintenance Tasks
- Monitor vacuum water level and dustbin status
- Check motion sensor batteries
- Verify Sonos speaker connectivity
- Review automation performance in statistics dashboard

## Deployment Helpers
- You can apply changes to automations, scripts, scenes, etc by calling the copy_*.sh scripts