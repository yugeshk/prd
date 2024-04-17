import os
import yaml
import pypandoc
from .sections import SectionBase

class PRD:
    def __init__(self, sections_folder):
        # Convert sections_folder to an absolute path
        self.sections_folder = os.path.abspath(sections_folder)
        # Set config_path relative to the current file's directory (assuming it's in prd_tools/prd)
        self.config_path = os.path.join(os.path.dirname(__file__), 'sections_config.yml')
        self.config = self.load_config()

    def load_config(self):
        with open(self.config_path, 'r') as file:
            return yaml.safe_load(file)

    def generate_section_files(self):
        if self.config is None:
            self.load_config()

        for section in self.config['sections']:
            file_name = f"{section['index']}-{section['name'].replace(' ', '_').lower()}.md"
            file_path = os.path.join(self.sections_folder, file_name)

            if os.path.exists(file_path):
                print(f'File "{file_name}" already exists. Skipping...')
                continue

            with open(file_path, 'w') as md_file:
                md_file.write(f"# {section['title']}\n\n")
                if 'comments' in section:
                    for comment in section['comments']:  #Assuming comments are a list
                        md_file.write(f"*{comment}*\n\n")

                for subsection in section.get('subsections', []):
                    md_file.write(f"## {subsection['title']}\n\n")
                    if 'comments' in subsection:
                        for comment in subsection['comments']:  # Assuming comments are a list
                            md_file.write(f"*{comment}*\n\n")

            print(f'File "{file_name}" created with section and subsections.')

    def load_sections(self):
        sections = []
        for section_info in self.config['sections']:
            # Convert section name to CamelCase and prefix with 'Section'
            class_name = 'Section' + ''.join(word.capitalize() for word in section_info['name'].split('_'))
            section_class = globals().get(class_name, SectionBase)

            # Initialize the Section/Subsection with provided information
            section = section_class(name=section_info['name'],
                                    title=section_info.get('title', ''),
                                    word_limit=section_info.get('word_limit'),
                                    subsections=section_info.get('subsections', []),
                                    file_name=f"{section_info['index']}-{section_info['name']}.md")
            sections.append(section)
        return sections

    def compile_to_pdf(self, output_file='prd_document.pdf'):
        all_content = ''
        for section in self.sections:
            # Assuming each Section class has a method to return its markdown content
            all_content += section.to_markdown() + '\n\n'

        # Convert combined markdown content to PDF
        pypandoc.convert_text(all_content, 'pdf', format='md', outputfile=output_file)
        print(f'Compiled PDF saved as {output_file}')

    def compile_to_pdf_from_folder(self, folder_name='sections', output_file='prd_document.pdf'):
        """
        Generate a PDF from markdown files in the specified folder, ordered by file name.
        """
        original_cwd = os.getcwd()  # Save the original current working directory
        os.chdir(folder_name)  # Change to the sections directory

        markdown_files = sorted(
            [f for f in os.listdir('.') if os.path.isfile(f) and f.endswith('.md')],
            key=lambda x: (int(x.split('-')[0]), x) if x.split('-')[0].isdigit() else (float('inf'), x)
        )

        all_content = ''
        for file_name in markdown_files:
            with open(file_name, 'r') as md_file:
                all_content += md_file.read() + '\n\n'

        try:
            output_file_path = os.path.join(original_cwd, output_file)
            pypandoc.convert_text(all_content, 'pdf', format='md', outputfile=os.path.join(original_cwd, output_file))
            print(f'Compiled PDF saved as {output_file_path}')
        finally:
            os.chdir(original_cwd)
