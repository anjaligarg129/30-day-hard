# Weather updater (Claude scheduled task prompt)

Update the weather shown in the "30 Day Hard" tracker artifact at https://claude.ai/artifact/YSXjGfLGjTTAjcB6MrZtae.

1. Look up the current weather in Berkeley, California (WebSearch, then fetch a weather page such as https://www.theweathernetwork.com/en/city/us/california/berkeley/current). Get the current temperature in Fahrenheit and the current condition.
2. Map the condition to one of these codes: "clear" (sunny/clear/mostly clear), "clouds" (partly cloudy, cloudy, overcast), "rain" (rain, showers, drizzle, thunderstorms), "fog" (fog, mist, haze).
3. Load the ArtifactData tool. Read the document with action "get", collection "weather", doc_id "now", url above, and note its version.
4. Write it with action "set", collection "weather", doc_id "now", if_version set to that version, and data:
   {"temp": <number, °F>, "cond": "<code>", "label": "<short human label>", "place": "Berkeley", "updated": "<ISO 8601 UTC timestamp>"}

Do not change any other document in that artifact's database and do not publish or edit the artifact page.
