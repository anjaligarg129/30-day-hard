# 30 Day Hard

A two-person 30-day challenge tracker (Sanju vs. Anj), published as a Claude artifact:
https://claude.ai/artifact/YSXjGfLGjTTAjcB6MrZtae

- `index.html`: snapshot of the published page. It reads and writes its data through the
  Claude artifact runtime (`window.claude` db capability), so it only fully works when hosted as an artifact.
- `weather/update-prompt.md`: the scheduled-task prompt that refreshes the Berkeley weather
  (`weather/now` doc in the artifact database).
- `weather/map_condition.py`: helper that maps a condition string to `clear` / `clouds` / `rain` / `fog`.
