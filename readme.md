# Roll20 Audio Track Deleter

This is a Python script that deletes all audio tracks from a Roll20 account.
Why do you want to do that?. In my case, because I had uploaded too much music and it was hard to manage, or maybe because you want to migrate from the paid plan to the free plan and you can't because your audio library is just too big.

## Requirements

- Python 3
- `requests` library

## Installation

1. Clone this repository.
2. Install the required Python packages using pip:

```bash
pip install -r requirements.txt
```

## Usage
1. Replace the headers dictionary in roll20deleter.py with your own headers. You can get these headers from your browser's network inspector when you make a request to Roll20.
2. Run roll20deleter.py:

```bash
python roll20deleter.py
```

## Notes:
- This script will delete all audio tracks from your Roll20 account. Use at your own risk.
- This script will not delete audio track references from your games. You will have to do this manually. (!!)
- The api calls tends to time-out after a while. If this happens, just run the script again.

## License
MIT License

Copyright (c) 2023 Leonard Petit-Breuilh

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
