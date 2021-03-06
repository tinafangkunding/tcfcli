import os
import yaml
from tcfcli.common.user_exceptions import ContextException
from tcfcli.libs.utils.yaml_parser import yaml_parse


class Template(object):

    @staticmethod
    def get_template_data(template_file):
        if not os.path.exists(template_file):
            return {}

        with open(template_file, 'r') as f:
            try:
                return yaml_parse(f.read())
            except (ValueError, yaml.YAMLError) as ex:
                raise ContextException("Parse template failed: {}".format(str(ex)))