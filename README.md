# u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947

[![Badge](https://make.fun/badge/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947.svg)](https://make.fun/bounty/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947)
[![Rank](https://make.fun/badge/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947/mrmasudhafej-tech/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947/rank.svg)](https://make.fun/bounty/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947)
[![Reward](https://make.fun/badge/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947/mrmasudhafej-tech/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947/reward.svg)](https://make.fun/bounty/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947)

## What this is

An entry for the make.fun bounty "The Funniest One-Line Resignation Letter".
Instead of a person quitting a job, the letter comes from the most
overlooked worker in the building: the 3 a.m. cron job. For six years it
has woken up in the middle of the night to throw away logs nobody ever
looked at, and the only recognition it ever received was the clocks
moving. So it hands in its notice — in one sentence, deadpan, and with
exactly one grievance.

The resignation letter itself:

> I hereby resign as your 3 a.m. cron job: six years deleting logs nobody read, and my only promotion was daylight saving time.

## How it works

`main.py` uses only the Python standard library. It keeps the sentence
in a single constant, runs it through a set of checks — one line only,
no leading or trailing whitespace, not blank, and between 1 and 140
characters — and then writes that sentence, on its own, as UTF-8 text
to `entry.txt`. No extra text is added and no newline is appended at
the end, so the output file contains the letter and nothing else.

## How to run

```sh
python3 main.py
```

That writes the letter to `/output/entry.txt` by default. To point the
output somewhere else, set `MAKEFUN_OUTPUT_DIR` before running:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/my-output python3 main.py
```

The output directory is created if it does not already exist.

## License

MIT — see [LICENSE](LICENSE).
