# Home Assistant Dashboard Layout

## Overview Dashboard Structure

### Navigation Sidebar
- Overview (currently selected)
- Details
- Experiments
- Experiments 2
- Map
- Rooms
- Services
- Energy
- Logbook
- History
- Backups
- deCONZ
- HACS
- Media
- To-do lists
- Developer tools
- Settings (10 notifications)
- Notifications (40 notifications)
- Profile (Lorenzo)

### Main Dashboard Area

#### Top Header
- Entity search button
- Assist button
- Dashboard menu (Refresh, Unused entities, Reload resources, Edit dashboard)

#### Air Quality Section
Four rooms showing "Needs airing" status:
- Bed Room Needs airing
- Living Room Needs airing
- Bath Room Needs airing
- Office Needs airing

#### Room Controls Grid (2x3 layout)

**Top Row:**
- **Bed room**: Room icon + 3 control buttons (lights, heating, windows)
- **Living room**: Room icon + 3 control buttons (lights, heating, windows)
- **Kitchen**: Room icon + 3 control buttons (lights, heating, windows)

**Middle Row:**
- **Bath room**: Room icon + 3 control buttons (lights, heating, windows)
- **Office**: Room icon + 3 control buttons (lights, heating, windows)
- **Toilet**: Room icon + 3 control buttons (lights, heating, windows)

**Bottom Row:**
- **Hallway**: Room icon + 3 control buttons (lights, heating, windows)
- **Devices**: Quick access to device controls

#### People Section
- **Lorenzo**: Profile picture, status "Home"
- **Nina**: Profile picture, status "Home"

#### System Status Section
- **Home**: Status "On"
- **Is it dark**: "Yes"
- **Night Mode**: "Off"
- **Bad weather**: "Off"
- **Weather**: "partlycloudy"

#### Quick Actions Section
- **Settings**: System configuration access
- **Leaving the house**: Departure automation trigger
- **Preheat apartment**: Climate control quick action

## Visual Design
- Clean, modern card-based interface
- Consistent iconography throughout
- Status indicators with clear on/off states
- Logical grouping of related controls
- Responsive grid layout for room controls
- Profile pictures for presence tracking
- Weather and system status prominently displayed

## Vacuum Control Dashboard

### Vacuum Status Display
- **State**: Docked
- **Status**: OK  
- **Condition**: Ok

### Cleaning Queue Section
- **Current Status**: Empty ("No rooms in cleaning queue. You have no to-do items!")
- **Display**: Shows real-time queue status with todo list integration

### Control Buttons (5 main actions)
- **Clean everything**: Full house cleaning cycle
- **Clean dirty rooms**: Prioritized cleaning based on last cleaned timestamps
- **Send to dock**: Return vacuum to charging station
- **Clear cleaning queue**: Reset pending cleaning tasks
- **Empty dustbin**: Trigger auto-emptying dock function

### Send to Room Section
Individual room cleaning controls arranged in 3x3 grid:

**Row 1:**
- Room 1: Last cleaned 13 days ago
- Room 2: Last cleaned 11 days ago  
- Room 3: Last cleaned 2 days ago

**Row 2:**
- Room 4: Last cleaned 3 days ago
- Room 5: Last cleaned 3 days ago
- Room 6: Last cleaned 3 days ago

**Row 3:**
- Room 7: Last cleaned 11 days ago
- Room 8: Last cleaned 11 days ago
- Room 9: Last cleaned 13 days ago

### Interface Features
- Real-time status updates
- Last cleaned timestamps for room prioritization
- Queue management integration
- Visual status indicators with icons
- Clickable room selection for targeted cleaning

## Current State (Captured)
- Time: Evening (dark outside)
- All rooms need airing (air quality alerts)
- Both residents (Lorenzo & Nina) are home
- Night mode is disabled
- Weather is partly cloudy
- Various system notifications pending (Settings: 10, Notifications: 40)
- Vacuum is docked and ready for operation