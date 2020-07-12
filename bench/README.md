# Benchmarks

Benchmarking is done using the `./bench-all-5.sh` script.
Time displayed are the best time of 3 after ignoring the first 2 outputs.

## IWSLT EN-ZH (EN)

- Dataset: IWSLT EN-ZH (EN)
- Number of lines: 100000
- CPU: Intel i7-9750H (MacBook Pro 16 2020)
- OS: `Macos-10.15`
- Compiler: `clang++==11.0.3`

| Name                | Time taken (seconds) | Sentences / second | Speedup |
| ------------------- | -------------------- | ------------------ | ------- |
| `fast-tokenizer`    | 0.85                 | 127758             | 6.5     |
| `fast-tokenizer-py` | 0.89                 | 121665             | 6.2     |
| `tokenizer.perl`    | 5.13                 | 19760              | 1.0     |
| `sacremoses`        | 12.63                | 7961               | 0.4     |

## IWSLT EN-ZH (ZH)

- Dataset: IWSLT EN-ZH (ZH)
- Number of lines: 100000
- CPU: Intel i7-9750H (MacBook Pro 16 2020)
- OS: `Macos-10.15`
- Compiler: `clang++==11.0.3`

| Name                | Time taken (seconds) | Sentences / second | Speedup |
| ------------------- | -------------------- | ------------------ | ------- |
| `fast-tokenizer-py` | 0.72                 | 154447             | 3.6     |
| `fast-tokenizer`    | 0.73                 | 153884             | 3.6     |
| `tokenizer.perl`    | 2.37                 | 43300              | 1.0     |
| `sacremoses`        | >15 (timeout)        | 582                | 0.01    |

> Random note: It isn't fair to compare sacremoses (ZH) since it is
> using backtracking to match a large quantity of CJK characters.
