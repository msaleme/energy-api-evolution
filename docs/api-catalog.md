# API Catalog

This catalog provides a comprehensive overview of all 36 APIs in the Energy API Evolution Platform, organized by project and layer.

## 📑 Table of Contents

- [dsgrid APIs](#dsgrid-apis)
  - [System APIs](#dsgrid-system-apis)
  - [Process APIs](#dsgrid-process-apis)
  - [Experience APIs](#dsgrid-experience-apis)
- [OpenEMS APIs](#openems-apis)
  - [System APIs](#openems-system-apis)
  - [Process APIs](#openems-process-apis)
  - [Experience APIs](#openems-experience-apis)
- [REopt APIs](#reopt-apis)
  - [System APIs](#reopt-system-apis)
  - [Process APIs](#reopt-process-apis)
  - [Experience APIs](#reopt-experience-apis)

---

## dsgrid APIs

### dsgrid System APIs

#### 1. Weather Data API
- **Endpoint**: `/api/v1/dsgrid/weather`
- **Purpose**: Retrieve weather data and forecasts
- **Methods**: GET, POST
- **Key Features**:
  - Historical weather data
  - 7-day forecasts
  - Real-time updates
  - Location-based queries
- **Response Time**: < 200ms

#### 2. Building Stock Database API
- **Endpoint**: `/api/v1/dsgrid/buildings`
- **Purpose**: Access building characteristics data
- **Methods**: GET
- **Key Features**:
  - ResStock residential data
  - ComStock commercial data
  - Building type filtering
  - Regional aggregation
- **Response Time**: < 300ms

#### 3. Transportation Model API
- **Endpoint**: `/api/v1/dsgrid/transport`
- **Purpose**: EV charging and transportation data
- **Methods**: GET, POST
- **Key Features**:
  - EV adoption projections
  - Charging patterns
  - Fleet electrification
  - TEMPO model integration
- **Response Time**: < 250ms

#### 4. Census Bureau API
- **Endpoint**: `/api/v1/dsgrid/census`
- **Purpose**: Demographic and economic data
- **Methods**: GET
- **Key Features**:
  - Population demographics
  - Economic indicators
  - Geographic filtering
  - Time series data
- **Response Time**: < 200ms

### dsgrid Process APIs

#### 5. Load Profile Generator API
- **Endpoint**: `/api/v1/dsgrid/load-profile`
- **Purpose**: Generate electricity load profiles
- **Methods**: POST, GET
- **Key Features**:
  - County-level resolution
  - Hourly granularity
  - Scenario modeling
  - Machine learning predictions
- **Response Time**: < 5s (complex calculations)

#### 6. Scenario Validation API
- **Endpoint**: `/api/v1/dsgrid/validate`
- **Purpose**: Validate load scenarios
- **Methods**: POST
- **Key Features**:
  - Statistical validation
  - Anomaly detection
  - Comparison with historical data
  - Confidence scoring
- **Response Time**: < 2s

### dsgrid Experience APIs

#### 7. Grid Modeling Data API
- **Endpoint**: `/api/v1/dsgrid/grid-model`
- **Purpose**: Export data for grid analysis tools
- **Methods**: GET, POST
- **Key Features**:
  - PSS/E format export
  - PowerWorld compatibility
  - Custom formatting
  - Bulk export
- **Response Time**: < 10s

#### 8. Policy Impact Analysis API
- **Endpoint**: `/api/v1/dsgrid/policy`
- **Purpose**: Analyze policy impacts on grid
- **Methods**: POST, GET
- **Key Features**:
  - Policy scenario modeling
  - Impact visualization
  - Comparative analysis
  - Report generation
- **Response Time**: < 5s

---

## OpenEMS APIs

### OpenEMS System APIs

#### 9. Device API
- **Endpoint**: `/api/v1/openems/devices`
- **Purpose**: Manage energy devices
- **Methods**: GET, POST, PUT, DELETE
- **Key Features**:
  - Multi-protocol support (Modbus, SunSpec)
  - Auto-discovery
  - Real-time telemetry
  - Control commands
- **Response Time**: < 100ms

#### 10. Utility Tariff API
- **Endpoint**: `/api/v1/openems/tariffs`
- **Purpose**: Manage utility rate structures
- **Methods**: GET, POST
- **Key Features**:
  - Time-of-use rates
  - Demand charges
  - Net metering
  - Dynamic pricing
- **Response Time**: < 150ms

#### 11. Weather Forecast API
- **Endpoint**: `/api/v1/openems/weather`
- **Purpose**: Site-specific weather for solar/load prediction
- **Methods**: GET
- **Key Features**:
  - Solar irradiance
  - Temperature forecasts
  - Cloud cover prediction
  - 48-hour forecasts
- **Response Time**: < 200ms

### OpenEMS Process APIs

#### 12. Energy Optimization API
- **Endpoint**: `/api/v1/openems/optimize`
- **Purpose**: Optimize energy flows
- **Methods**: POST
- **Key Features**:
  - Cost minimization
  - Self-consumption maximization
  - Carbon reduction
  - Multi-objective optimization
- **Response Time**: < 3s

#### 13. Device Control API
- **Endpoint**: `/api/v1/openems/control`
- **Purpose**: Execute device commands
- **Methods**: POST
- **Key Features**:
  - Secure command dispatch
  - Conflict resolution
  - Safety interlocks
  - Command queuing
- **Response Time**: < 500ms

#### 14. Anomaly Detection API
- **Endpoint**: `/api/v1/openems/anomaly`
- **Purpose**: Detect abnormal patterns
- **Methods**: POST, GET
- **Key Features**:
  - Real-time detection
  - Pattern recognition
  - Fault diagnosis
  - Alert generation
- **Response Time**: < 1s

### OpenEMS Experience APIs

#### 15. Homeowner Dashboard API
- **Endpoint**: `/api/v1/openems/dashboard`
- **Purpose**: Power homeowner interfaces
- **Methods**: GET
- **Key Features**:
  - Real-time energy flows
  - Cost tracking
  - Device status
  - Insights and recommendations
- **Response Time**: < 200ms

#### 16. Fleet Management API
- **Endpoint**: `/api/v1/openems/fleet`
- **Purpose**: Manage multiple sites
- **Methods**: GET, POST
- **Key Features**:
  - Multi-site overview
  - Bulk operations
  - Performance benchmarking
  - Virtual Power Plant (VPP) coordination
- **Response Time**: < 500ms

---

## REopt APIs

### REopt System APIs

#### 17. Energy Load API
- **Endpoint**: `/api/v1/reopt/load`
- **Purpose**: Manage site load data
- **Methods**: GET, POST
- **Key Features**:
  - 15-minute interval data
  - Annual load profiles
  - Data validation
  - Gap filling
- **Response Time**: < 300ms

#### 18. Technology Cost API
- **Endpoint**: `/api/v1/reopt/tech-costs`
- **Purpose**: Current technology costs
- **Methods**: GET
- **Key Features**:
  - Solar, wind, battery costs
  - Regional variations
  - Degradation rates
  - O&M costs
- **Response Time**: < 200ms

#### 19. Incentive Database API
- **Endpoint**: `/api/v1/reopt/incentives`
- **Purpose**: Tax credits and incentives
- **Methods**: GET
- **Key Features**:
  - Federal/state/local incentives
  - Utility rebates
  - Eligibility checking
  - DSIRE integration
- **Response Time**: < 250ms

#### 20. Renewable Resource API
- **Endpoint**: `/api/v1/reopt/resources`
- **Purpose**: Solar and wind resource data
- **Methods**: GET
- **Key Features**:
  - NSRDB solar data
  - Wind resource data
  - Typical meteorological year
  - Shading analysis
- **Response Time**: < 400ms

### REopt Process APIs

#### 21. Optimization Run API
- **Endpoint**: `/api/v1/reopt/optimize`
- **Purpose**: Run techno-economic optimization
- **Methods**: POST, GET
- **Key Features**:
  - Technology sizing
  - Economic optimization
  - Resilience constraints
  - Sensitivity analysis
- **Response Time**: < 60s

#### 22. Resilience Analysis API
- **Endpoint**: `/api/v1/reopt/resilience`
- **Purpose**: Analyze outage survival
- **Methods**: POST
- **Key Features**:
  - Outage simulation
  - Critical load coverage
  - Probability analysis
  - Economic valuation
- **Response Time**: < 30s

#### 23. Financial Proforma API
- **Endpoint**: `/api/v1/reopt/financial`
- **Purpose**: Detailed financial analysis
- **Methods**: POST, GET
- **Key Features**:
  - NPV/IRR calculation
  - Cash flow projection
  - Financing scenarios
  - Sensitivity analysis
- **Response Time**: < 5s

### REopt Experience APIs

#### 24. Web Tool Backend API
- **Endpoint**: `/api/v1/reopt/webtool`
- **Purpose**: Support public web interface
- **Methods**: GET, POST
- **Key Features**:
  - Project management
  - Guided workflows
  - Results visualization
  - Report generation
- **Response Time**: < 300ms

#### 25. Consultant Analysis API
- **Endpoint**: `/api/v1/reopt/consultant`
- **Purpose**: Advanced features for professionals
- **Methods**: GET, POST
- **Key Features**:
  - Batch processing
  - Custom constraints
  - Portfolio analysis
  - White-label reports
- **Response Time**: < 500ms

---

## Common API Features

### Authentication
All APIs support:
- OAuth 2.0
- API Keys
- JWT tokens

### Rate Limiting
- Default: 1000 requests/minute
- Premium tiers available

### Response Formats
- JSON (default)
- CSV (data export)
- XML (legacy support)

### Error Handling
Standardized error responses:
```json
{
  "error": {
    "code": "RESOURCE_NOT_FOUND",
    "message": "The requested resource was not found",
    "details": {...}
  }
}
```

### Versioning
- Current version: v1
- Version in URL path
- Backward compatibility guaranteed

### Documentation
- Interactive Swagger UI for each API
- Postman collections available
- Code examples in multiple languages

---

For detailed API documentation, authentication setup, and code examples, visit our [API Portal](https://api.energyplatform.io).