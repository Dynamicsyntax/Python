import re
import os

with open("README.md", "r") as f:
    lines = f.readlines()

new_lines = []
last_num = 180
in_level = False
current_dir = ""
level_dirs = {
    4: "🔵 Level 4: Specialized AI & Interaction (Projects 181–350)",
    5: "🔴 Level 5: Smart Infrastructure & Fintech (Projects 351–450)",
    6: "🟣 Level 6: Expert Engines & Integration (Projects 451–530)"
}
current_level = 0
current_category = ""
categories = {
    "Specialized Quizzes & Brain Teasers": "Specialized Quizzes & Brain Teasers",
    "AI Assistants & Advisors": "AI Assistants & Advisors",
    "Computer Vision & Advanced Recognition": "Computer Vision & Advanced Recognition",
    "Smart Systems & Productivity AI": "Smart Systems & Productivity AI",
    "Smart Cities & Environmental Logic": "Smart Cities & Environmental Logic",
    "Financial Engineering & Wealth": "Financial Engineering & Wealth",
    "Productivity Mastery": "Productivity Mastery",
    "Advanced Financial & Personal Mastery": "Advanced Financial & Personal Mastery",
    "Advanced Engines & Backends (Building from Scratch)": "Advanced Engines & Backends (Building from Scratch)"
}

project_list = []

for line in lines:
    if "Level 4:" in line:
        current_level = 4
    elif "Level 5:" in line:
        current_level = 5
    elif "Level 6:" in line:
        current_level = 6

    cat_match = re.search(r'^###\s+(.*)', line)
    if cat_match:
        cat_name = cat_match.group(1).strip()
        if cat_name in categories:
            current_category = cat_name

    match = re.search(r'^\*\s+\*\*0?(\d+)\.\s+(.*?):\*\*\s+(.*)', line)
    if match and current_level >= 4:
        num = int(match.group(1))
        title = match.group(2)
        desc = match.group(3)

        while last_num + 1 < num:
            missing_num = last_num + 1
            missing_title = f"Project {missing_num}"
            missing_desc = f"Placeholder for project {missing_num}."
            new_lines.append(f"* **{missing_num}. {missing_title}:** {missing_desc}\n")

            project_list.append({
                'num': missing_num,
                'title': missing_title,
                'desc': missing_desc,
                'level': current_level,
                'category': current_category
            })
            last_num = missing_num

        project_list.append({
            'num': num,
            'title': title,
            'desc': desc,
            'level': current_level,
            'category': current_category
        })
        last_num = num
        new_lines.append(line)
    elif match and current_level < 4:
        last_num = int(match.group(1))
        new_lines.append(line)
    else:
        new_lines.append(line)

with open("README.md", "w") as f:
    f.writelines(new_lines)

# Now generate python files
for proj in project_list:
    level_dir = level_dirs[proj['level']]
    cat_dir = proj['category']
    # Sanitize title
    safe_title = proj['title'].replace('/', '-').replace(':', '')

    # Create category dir if not exists
    cat_path = os.path.join(level_dir, cat_dir)
    os.makedirs(cat_path, exist_ok=True)

    # Try to find existing file
    existing_files = os.listdir(cat_path)
    file_exists = False
    for f in existing_files:
        if f.startswith(f"{proj['num']}.") or f.startswith(f"0{proj['num']}."):
            file_exists = True
            break

    if not file_exists:
        file_path = os.path.join(cat_path, f"{proj['num']}. {safe_title}.py")
        with open(file_path, "w") as f:
            f.write(f"# {proj['num']}. {proj['title']}\n")
            f.write(f"# {proj['desc']}\n\n")
            f.write("def main():\n")
            f.write("    print('This is a placeholder for " + proj['title'].replace("'", "\\'") + "')\n\n")
            f.write("if __name__ == '__main__':\n")
            f.write("    main()\n")

print("Completed generation.")
