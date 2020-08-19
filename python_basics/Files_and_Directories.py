from pathlib import Path

path = Path()
print(path.exists())
for file in (path.glob('*')):
    print(file)


