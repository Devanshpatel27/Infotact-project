# PyChronicle - Week 1

Week 1 delivers the project foundation only:

- Parse a target Python file with `ast`.
- List variable assignments and their source lines.
- Create the SQLite `execution_history` table with `timestamp`, `line_number`, `variable_name`, and `serialized_value` columns.

Run from this folder:

```powershell
py main.py
py main.py path\to\target.py
```

The default target is `sample.py`. Runtime tracing, state capture, and the terminal UI are planned for later weeks and are not started by the Week 1 command.
