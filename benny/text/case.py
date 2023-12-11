import re


pascal_case_pattern = "^([A-Z0-9][a-z0-9]*)+"
camel_case_pattern = "^([a-z0-9]+)+([A-Z0-9][a-z0-9]*)*"
snake_case_pattern = "^([a-z0-9]+)(_[a-z0-9]+)*"
screaming_snake_case_pattern = "^([A-Z0-9]+)(_[A-Z0-9]+)*"