import ast
from .base.base import register_check
from .base.ast import AstCheck
from .base.etree import EtreeCheck


@register_check
class DummyWriteCheck(AstCheck):
    version_to = '16.0'
    ttype = 'function'
    keywords = {
        'name': 'write',
    }
    message = 'Trululuted Write'


@register_check
class DummyCreateCheck(AstCheck):
    version_from = '14.0'
    ttype = 'function'
    keywords = {
        'name': 'create',
    }
    message = 'Trululuted Create'


@register_check
class DummyCreateDecoratorCheck(AstCheck):
    version_from = '15.0'
    ttype = 'decorator'
    keywords = {
        'name': 'create',
        'decorator': 'model_create_multi'
    }
    message = 'Create method should not be decorated with @api.model_create_multi from version 15.0+'



@register_check
class DummyViewCheck(EtreeCheck):
    ttype = 'attribute'
    keywords = {
        'attribute': 'model',
        'value': 'ir.ui.view',
    }
    message = 'Trululuted views'
