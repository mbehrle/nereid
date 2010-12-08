# -*- coding: UTF-8 -*-
'''
    nereid.signals

    Flask/Blicker based signalling

    :copyright: (c) 2010 by Sharoon Thomas.
    :license: BSD, see LICENSE for more details
'''
# pylint: disable-msg=W0611
from flask.signals import template_rendered, request_started, \
        request_finished, got_request_exception
