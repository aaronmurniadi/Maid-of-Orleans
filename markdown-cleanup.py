import re

def replace(filePath, text, subs, flags=0):
    with open(file_path, "r+") as file:
        file_contents = file.read()
        text_pattern = re.compile(re.escape(text), flags)
        file_contents = text_pattern.sub(subs, file_contents)
        file.seek(0)
        file.truncate()
        file.write(file_contents)

file_path="pg37106.txt"

#calling the replace method
replace(file_path, ' "', ' “')

replace(file_path, '" ', '” ')

replace(file_path, '\n"', '\n“')
replace(file_path, "\n'", "\n‘")

replace(file_path, '"\n', '”\n')

replace(file_path, '!"', '!”')

replace(file_path, '?"', '?”')

replace(file_path, '."', '.”')

replace(file_path, '".', '”.')

replace(file_path, '":', '”:')

replace(file_path, '";', '”;')

replace(file_path, '")', '”)')
replace(file_path, '("', '(“')

replace(file_path, '"]', '”]')
replace(file_path, '["', '[“')

replace(file_path, '--', '---')

replace(file_path, '"---', '”---')
replace(file_path, '---"', '---“')

replace(file_path, "n't ", "n’t ")
replace(file_path, "n't\n", "n’t\n")
replace(file_path, "n't", "n’t")

replace(file_path, "'s ", "’s ")
replace(file_path, "'s\n", "’s\n")
replace(file_path, "'s", "’s")

replace(file_path, "'s ", "’s ")
replace(file_path, "'s\n", "’s\n")

replace(file_path, "I'm ", "I’m ")
replace(file_path, "I'm\n", "I’m\n")

replace(file_path, "I'll ", "I’ll ")
replace(file_path, "I'll\n", "I’ll\n")

replace(file_path, "'d ", "’d ")
replace(file_path, "'d\n", "’d\n")

replace(file_path, "'ll ", "’ll ")
replace(file_path, "'ll\n", "’ll\n")

replace(file_path, " '", " ‘")
replace(file_path, "' ", "’ ")
replace(file_path, "'\n", "’\n")

replace(file_path, "'”", "’”")
replace(file_path, "“'", "“‘")
replace(file_path, "“‘'", "“‘‘")

replace(file_path, "'?", "’?")

replace(file_path, "I've", "I’ve")
replace(file_path, "'ve ", "’ve ")

replace(file_path, " & ", " \& ")

