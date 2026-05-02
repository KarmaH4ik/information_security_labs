# weather-app-cli

A small Python CLI that fetches the current weather for a city from the free
[Open-Meteo](https://open-meteo.com/) API (no key required) and saves every
lookup to a local SQLite database with the request timestamp.

## Install

```sh
pip install -r requirements.txt
```

## Usage

```sh
python weather.py San Francisco
python weather.py Reykjavik
python weather.py "New York"
```

Sample output:

```
San Francisco, United States
Now: 14.2°C (feels 13.0°C) · Partly cloudy
Humidity: 72% · Wind: 12.4 km/h
Today: H 18.4°C / L 11.1°C
```

Exit codes: `0` on success, `2` on any error (city not found, network failure,
non-200 response). Errors are written to stderr.

## Where data is stored

Every lookup is appended to `~/.weather-app-cli/weather.db`. The schema is a
single table `weather_lookups` with one row per request, including the full
JSON response in `raw_json`.

Inspect recent lookups:

```sh
sqlite3 ~/.weather-app-cli/weather.db \
  "SELECT fetched_at, city_input, temperature_c, weather_description
   FROM weather_lookups ORDER BY id DESC LIMIT 10;"
```
