import style

pascal = "PascalCase"
camel = "camelCase"
snake = "snake_case"
screaming_snake = "SCREAMING_SNAKE_CASE"

all_case = [pascal, camel, snake, screaming_snake]

for case in all_case:
    print(f"\n{case}\n")
    print(f"pascal: {style.pascal_case(case)}")
    print(f"camel: {style.camel_case(case)}")
    print(f"snake: {style.snake_case(case)}")
    print(f"screaming_snake: {style.screaming_snake_case(case)}")
