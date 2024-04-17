class SectionBase:
    def __init__(self, name, title, word_limit, subsections, file_name):
        self.name = name
        self.title = title
        self.subsections = subsections  # This could be a list of Subsection objects or dictionaries
        self.file_name = file_name

    def to_markdown(self):
        # Generate markdown content for this section, including title and subsections
        markdown_content = f'# {self.title}\n\n'
        for subsection in self.subsections:
            markdown_content += f'## {subsection["title"]}\n\n'
        return markdown_content

class Subsection:
    def __init__(self, title, word_limit):
        self.title = title

