# BUILD FILE SYNTAX: SKYLARK 
python_binary(
  name = 'fetch_prices',
  platform = 'py3',
  main_module = 'fetch_prices',
  deps = [
    ':runescape',
  ],
)

python_library(
  name = 'runescape',
  srcs = ['fetch_prices.py'],
)
