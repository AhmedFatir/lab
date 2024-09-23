import sys
import os

def render_template(template_file):
	# Check if the template file exists
	if not os.path.exists(template_file):
		raise FileNotFoundError(f"Template file '{template_file}' does not exist.")

	# Check if the template file has the correct extension
	if not template_file.endswith('.template'):
		raise ValueError("Template file must have a .template extension.")

	# Read the template file
	with open(template_file, 'r') as f:
		template_content = f.read()

	# Import settings
	try:
		import settings
	except ImportError:
		raise ImportError("settings.py file not found.")

	# Replace patterns in the template
	for key, value in settings.__dict__.items():
		if not key.startswith('__'):
			pattern = '{' + key + '}'
			template_content = template_content.replace(pattern, str(value))

	# Write the result to the output file
	output_file = os.path.splitext(template_file)[0] + '.html'
	with open(output_file, 'w') as f:
		f.write(template_content)

	print(f"HTML file '{output_file}' has been generated.")

def template():
	if len(sys.argv) != 2:
		print("Usage: python3 render.py <template_file>")
		sys.exit(1)
	try:
		render_template(sys.argv[1])
	except Exception as e:
		print(f"Error: {str(e)}")
		return

if __name__ == '__main__':
	template()