from benny.text.style import Style
import benny.text.style

whitespace_string = " \t\n\r\v\f"
whitespace = list(whitespace_string)


if __name__ == "__main__":
    print(whitespace_string)
    print(whitespace)

    pascal = "PascalCase"
    camel = "camelCase"
    snake = "snake_case"
    screaming_snake = "SCREAMING_SNAKE_CASE"

    all_case = [pascal, camel, snake, screaming_snake]

    for case in all_case:
        print(f"\n{case}\n")
        print(f"pascal: {style.is_style()}")
        print(f"camel: {style.camel_case(case)}")
        print(f"snake: {style.snake_case(case)}")
        print(f"screaming_snake: {style.screaming_snake_case(case)}")
