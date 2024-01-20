import yaml

full_config = yaml.load(open('config.yml', 'r'), Loader=yaml.FullLoader)

api_config: dict = full_config['api']
storage_config: dict = full_config['storage']