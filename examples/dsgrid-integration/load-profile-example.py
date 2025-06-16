"""
Example: Generate Load Profile using dsgrid APIs

This example demonstrates how to generate an electricity load profile
for a specific region using the unified API platform.
"""

import requests
import json
from datetime import datetime, timedelta

# API Configuration
API_BASE_URL = "http://localhost:8000/api/v1"
API_KEY = "your-api-key-here"  # Replace with your API key

# Headers for authentication
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

def get_weather_forecast(location, days=7):
    """Fetch weather forecast for load profile generation"""
    endpoint = f"{API_BASE_URL}/dsgrid/weather/forecast"
    params = {
        "location": location,
        "days": days,
        "include": "temperature,humidity,solar_radiation"
    }
    
    response = requests.get(endpoint, headers=headers, params=params)
    response.raise_for_status()
    return response.json()

def get_building_stock(county_fips):
    """Get building characteristics for the county"""
    endpoint = f"{API_BASE_URL}/dsgrid/buildings/county/{county_fips}"
    
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    return response.json()

def generate_load_profile(county_fips, scenario_params):
    """Generate electricity load profile for a county"""
    endpoint = f"{API_BASE_URL}/dsgrid/load-profile/generate"
    
    # Prepare request payload
    payload = {
        "county_fips": county_fips,
        "start_date": scenario_params["start_date"],
        "end_date": scenario_params["end_date"],
        "scenario": {
            "name": scenario_params["name"],
            "ev_adoption_rate": scenario_params.get("ev_adoption_rate", 0.15),
            "solar_penetration": scenario_params.get("solar_penetration", 0.20),
            "energy_efficiency": scenario_params.get("energy_efficiency", 1.0),
            "demand_response_participation": scenario_params.get("dr_participation", 0.1)
        },
        "output_format": "hourly",
        "include_components": True
    }
    
    response = requests.post(endpoint, headers=headers, json=payload)
    response.raise_for_status()
    return response.json()

def validate_load_profile(profile_id):
    """Validate the generated load profile"""
    endpoint = f"{API_BASE_URL}/dsgrid/validate"
    
    payload = {
        "profile_id": profile_id,
        "validation_checks": [
            "statistical_bounds",
            "peak_timing",
            "seasonal_patterns",
            "anomaly_detection"
        ]
    }
    
    response = requests.post(endpoint, headers=headers, json=payload)
    response.raise_for_status()
    return response.json()

def main():
    """Main execution flow"""
    # Example: Generate load profile for Boulder County, Colorado
    county_fips = "08013"
    location = {"lat": 40.0150, "lon": -105.2705}
    
    print("🌤️  Fetching weather forecast...")
    weather = get_weather_forecast(location)
    print(f"   - Got {len(weather['forecast'])} days of weather data")
    
    print("\n🏢 Getting building stock data...")
    buildings = get_building_stock(county_fips)
    print(f"   - Residential buildings: {buildings['residential']['count']:,}")
    print(f"   - Commercial buildings: {buildings['commercial']['count']:,}")
    
    print("\n⚡ Generating load profile...")
    scenario_params = {
        "name": "High EV Adoption Scenario",
        "start_date": datetime.now().isoformat(),
        "end_date": (datetime.now() + timedelta(days=7)).isoformat(),
        "ev_adoption_rate": 0.30,  # 30% EV adoption
        "solar_penetration": 0.25,  # 25% solar
        "energy_efficiency": 0.9,   # 10% efficiency improvement
        "dr_participation": 0.15    # 15% demand response
    }
    
    profile = generate_load_profile(county_fips, scenario_params)
    profile_id = profile['profile_id']
    print(f"   - Generated profile ID: {profile_id}")
    print(f"   - Peak load: {profile['summary']['peak_load_mw']:.2f} MW")
    print(f"   - Total energy: {profile['summary']['total_energy_mwh']:.2f} MWh")
    
    print("\n✅ Validating load profile...")
    validation = validate_load_profile(profile_id)
    print(f"   - Validation status: {validation['status']}")
    print(f"   - Confidence score: {validation['confidence_score']:.2%}")
    
    # Display hourly load for first day
    print("\n📊 Hourly Load Profile (First 24 hours):")
    print("Hour | Load (MW)")
    print("-" * 20)
    for i, hour_data in enumerate(profile['hourly_data'][:24]):
        print(f"{i:4d} | {hour_data['load_mw']:8.2f}")
    
    # Export results
    print("\n💾 Exporting results...")
    with open(f"load_profile_{profile_id}.json", "w") as f:
        json.dump(profile, f, indent=2)
    print(f"   - Saved to load_profile_{profile_id}.json")

if __name__ == "__main__":
    main()