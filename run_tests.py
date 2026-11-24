from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parent

TESTS = [
    ("p1_reverse_words.py", "p1_input.txt", "p1_expected.txt"),
    ("p2_binary_search.py", "p2_input.txt", "p2_expected.txt"),
    ("p3_digit_sum.py", "p3_input.txt", "p3_expected.txt"),
    ("p4_pair_count.py", "p4_input.txt", "p4_expected.txt"),
]


def main():
    failures = 0

    for program, input_name, expected_name in TESTS:
        input_text = (ROOT / "tests" / input_name).read_text()
        expected = (ROOT / "tests" / expected_name).read_text().strip()

        result = subprocess.run(
            [sys.executable, str(ROOT / "problems" / program)],
            input=input_text,
            text=True,
            capture_output=True,
            check=True,
        )

        actual = result.stdout.strip()
        if actual == expected:
            print(f"PASS: {program}")
        else:
            failures += 1
            print(f"FAIL: {program}")
            print(f"  Expected: {expected!r}")
            print(f"  Got:      {actual!r}")

    print(f"\n{len(TESTS) - failures}/{len(TESTS)} tests passed.")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
