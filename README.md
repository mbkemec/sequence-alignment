
# Sequence Alignment Algorithms

This repository contains implementations of two classic sequence alignment algorithms:

- **Needleman-Wunsch** (global alignment)
- **Smith-Waterman** (local alignment)

with support for different substitution matrices, including:

- **PAM250**
- **BLOSUM62**
- **TTM** (custom matrix)

These are widely used in bioinformatics for comparing DNA, RNA, or protein sequences.

---

## Features

- Needleman-Wunsch global alignment  
- Smith-Waterman local alignment  
- Choice of scoring matrix: PAM250, BLOSUM62, or TTM (you can also add anything you want)
- Configurable gap penalty  
- Simple command-line interface

---

## Usage

### Installation

Clone the repository:

```bash
git clone https://github.com/mbkemec/sequence-alignment.git
cd sequence-alignment```

### Running the Code

```bash
python alignment_score.py```

After this, the program will ask you to answer the following questions;

- Which alignment type will you use,
- The first and second sequences,
- Which matrix will you use,
- Finally, the gap penalty score,

then the alignment process will automatically take place and you will see the sequences and the score on the screen.


#### Example
```text
$ python3 alignment_score.py
!! For 'smith waterman' please write 'sw', for 'needleman wunsch' please write 'nw' !!
Do you want to apply 'smith_waterman' or 'needleman_wunsch': nw
Please write your first sequence: TCA
Please write your second sequence: TA
!! Matrix types: 'BLOSUM62.txt' , 'PAM250.txt' , 'TTM.txt' !!
Please select your substition matrix (with file extension): TTM.txt
Please write your 'GAP' penalty score: -2
('TCA', 'T-A', 2.0)
```

## Requirements

- Python 
- You can save and use any matrix file you want, depending on your preference.

## License

This project is licensed under MIT License
