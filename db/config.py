from configparser import ConfigParser


def config_postgres(filename='config.ini'):

    parser = ConfigParser()
    parser.read_file(open(filename))

    sections = parser.sections()

    db = {}

    for section in sections:
        if parser.has_section(section):
            for param in parser.items(section):
                db[param[0]] = param[1]
        else:
            print(f'Config file does not have section {section}')

    return db


if __name__ == '__main__':
    print(config_postgres())
