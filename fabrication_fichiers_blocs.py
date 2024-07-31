import os

def create_markdown_files(summary_file):
    with open(summary_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    main_items = []
    current_main_item = None

    for line in lines:
        if line.startswith('* '):
            current_main_item = {'title': line.strip().split('[')[1].split(']')[0], 'link': line.strip().split('(')[1].split(')')[0], 'subitems': []}
            main_items.append(current_main_item)
        elif line.startswith('  * ') and current_main_item:
            print(line)
            subitem_title = line.strip().split('* ')[1]
            current_main_item['subitems'].append({'title': subitem_title, 'subsubitems': []})
        elif line.startswith('    * ') and current_main_item:
            print(line)
            subsubitem_title = line.strip().split('* ')[1].replace('(exercices/', '(../exercices/')
#            print(subsubitem_title) ; exit()
            current_main_item['subitems'][-1]['subsubitems'].append(subsubitem_title)

    for item in main_items:
        if not item['link'].startswith('blocs/'):
            continue

        filepath = item['link']
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        with open(filepath, 'w', encoding='utf-8') as file:
            title = item['title']
            bloc_name = filepath.replace('blocs/','').replace('.md','')
#title.lower().replace(' ', '_')
            file.write(f"# {title}\n\n")
            file.write(f"![](images/{bloc_name}.webp)\n\n")
            file.write(f"Le bloc de {title.lower()} se découpe en plusieurs chapitres:\n\n")
            for subitem in item['subitems']:
                file.write(f"* {subitem['title']}\n")
                for subsubitem in subitem['subsubitems']:
                    file.write(f"  * {subsubitem}\n")

# Utilisation du script
create_markdown_files('SUMMARY.md')
