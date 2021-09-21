import os
import yaml
import jinja2

DB_FILE = 'database.yml'
FIELDS_FILE = 'fields.yml'
TEMPLATE_DIR = 'templates/'
OUTPUT_FILE = 'index.html'

BOOTSTRAP_DEFAULT = {
    'css': 'https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/css/bootstrap.min.css',
    'js': 'https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/js/bootstrap.bundle.min.js',
}

def main():
    '''Build static HTML page from YAML data and Jinja2 templates'''
    with open(FIELDS_FILE) as f:
        fields = yaml.safe_load(f)
    with open(DB_FILE) as f:
        data = yaml.safe_load(f)

    jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(TEMPLATE_DIR))
    template = jinja_env.get_template('index.html.j2')

    bootstrap = BOOTSTRAP_DEFAULT
    for component in bootstrap:
        override = os.environ.get(f'BOOTSTRAP_{component.upper()}')
        if override:
            bootstrap[component] = override

    with open(OUTPUT_FILE, 'w') as output:
        output.write(
            template.render(
                bootstrap=bootstrap,
                data=data,
                fields=fields,
            )
        )

if __name__ == '__main__':
    main()
