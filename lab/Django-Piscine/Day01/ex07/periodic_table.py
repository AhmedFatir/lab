def parse_element(line):
    parts = line.split('=')
    if len(parts) != 2:
        return None

    name = parts[0].strip()
    attributes = parts[1].strip().split(',')
    element = {'name': name}
    
    for attr in attributes:
        key, value = attr.strip().split(':')
        if key == 'position':
            element['position'] = int(value)
        elif key == 'number':
            element['number'] = int(value)
        elif key == 'small':
            element['symbol'] = value.strip()
        elif key == 'molar':
            element['molar'] = float(value)
        elif key == 'electron':
            element['electron'] = value.strip()
    
    return element

def generate_css():
    return """
    <style>
        table { border-collapse: collapse; }
        td { border: 1px solid #ccc; padding: 5px; text-align: center; width: 100px; height: 100px; }
        h4 { margin: 0; }
        ul { list-style-type: none; padding: 0; margin: 0; font-size: 12px; text-align: left; }
    </style>
    """

def generate_element_html(element):
    return f"""
    <td>
        <h4>{element['name']}</h4>
        <ul>
            <li>No {element['number']}</li>
            <li>{element['symbol']}</li>
            <li>{element['molar']}</li>
            <li>{element['electron']} electron</li>
        </ul>
    </td>
    """

def generate_periodic_table_html(elements):
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Periodic Table of Elements</title>
    {generate_css()}
</head>
<body>
	<h1>Periodic Table of Elements</h1>
    <table>
    """

    max_position = max(element['position'] for element in elements)
    max_number = max(element['number'] for element in elements)

    current_row = 0
    for number in range(1, max_number + 1):
        element = next((e for e in elements if e['number'] == number), None)
        
        if element:
            if element['position'] < current_row:
                html += "</tr>"
                current_row = 0
            
            if current_row == 0:
                html += "<tr>"
            
            while current_row < element['position']:
                html += "<td></td>"
                current_row += 1
            
            html += generate_element_html(element)
            current_row += 1

    html += """
    </tr>
    </table>
</body>
</html>
    """
    return html

def periodic_table():
    with open('../dev/ex07/periodic_table.txt', 'r') as file:
        lines = file.readlines()

    elements = [parse_element(line) for line in lines if parse_element(line)]

    html = generate_periodic_table_html(elements)

    with open('periodic_table.html', 'w') as file:
        file.write(html)

if __name__ == "__main__":
    periodic_table()