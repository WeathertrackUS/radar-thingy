# Minimum Viable Product (MVP) for Weather Radar Application

## Overview
The MVP for the Weather Radar Application focuses on delivering the core functionality required to provide value to users while keeping the scope manageable for the initial release.

## Goals
- Display radar data from the NWS
- Display the radar data ontop of a basemap
- Display Severe Weather Alerts

## Core Features
1. **Radar Data from NWS**
   - Fetch and display radar data from the National Weather Service (NWS).
   - Overlay the radar data on a basemap for better visualization.

2. **Severe Weather Alerts**
   - Notify users of severe weather conditions in the selected region.
   - Display alerts prominently on the radar map.

## Actionable Steps
### Backend
- Set up a basic API server (e.g., Python with Flask).
- Integrate the NWS API to fetch radar and alert data.
- Create endpoints for:
  - Fetching radar data.
  - Fetching severe weather alerts.

### Frontend
- Build a radar display using a mapping library (e.g., Leaflet.js).
- Overlay radar data from the NWS on the basemap.
- Create a simple UI with sections for:
  - Radar map.
  - Severe weather alerts.
- Use mock data initially to test the UI.

### Testing
- Write unit tests for backend endpoints.
- Test frontend components for functionality and responsiveness.

## Task Assignments
- **Coordinator (You)**:
  - Set up the backend API server using Python and Flask.
  - Integrate the NWS API to fetch radar and severe weather alert data.
  - Create backend endpoints for:
    - `/radar`: Fetch and return radar data from the NWS API.
    - `/alerts`: Fetch and return severe weather alerts from the NWS API.
  - Ensure backend endpoints are functional with mock data for testing purposes.
  - Document the backend API structure and usage for the team.

- **Team Member 1 (StarinBox)**:
  - Design and implement the radar display using a mapping library (e.g., Leaflet.js).
  - Overlay radar data fetched from the backend onto the basemap.
  - Create a user-friendly UI for displaying radar data and severe weather alerts.
  - Ensure the UI is responsive and works across different screen sizes.
  - Collaborate with the Coordinator to integrate frontend components with backend endpoints.

- **Team Member 2 (WxRome)**:
  - Research and finalize the integration process for the NWS API.
  - Write scripts to fetch radar and alert data from the NWS API and process it for backend use.
  - Assist with backend development tasks, such as testing and debugging API endpoints.
  - Write unit tests for both backend and frontend components to ensure functionality.
  - Collaborate with StarinBox to test and refine the integration of radar data into the frontend.

## Milestones
- **Week 1**: Backend setup, NWS API integration, and mock data endpoints.
- **Week 2**: Frontend prototype with radar display and basemap overlay.
- **Week 3**: End-to-end integration of backend and frontend.
- **Week 4**: Testing, bug fixes, and MVP completion.

## Notes
- Keep the scope limited to ensure timely delivery.
- Use GitHub Issues or a task management tool to track progress.

