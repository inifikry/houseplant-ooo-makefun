"""Houseplant Out-of-Office entry: write the auto-reply line to /output/entry.txt."""

LINE = "Out of office. I am a fern and have not been watered since March. Your email has been filed under 'photosynthesis'."

OUTPUT_PATH = "/output/entry.txt"


def write_entry():
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)


def main():
    write_entry()


if __name__ == "__main__":
    main()
