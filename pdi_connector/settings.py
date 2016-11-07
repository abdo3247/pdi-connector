# -*- coding: utf-8 -*-
##############################################################################
#
#    pdi-connector module for OpenERP, Module to manage Pentaho
#                          Data Integration
#    Copyright (C) 2013 SYLEAM (<http://www.syleam.fr/>)
#                  2013-2014 MIROUNGA (<http://www.mirounga.fr>)
#              Christophe CHAUVET <christophe.chauvet@gmail.com>
#
#    This file is a part of openerp-pdi-connector
#
#    pdi-connector is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    pdi-connector is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp.osv import osv
from openerp.osv import fields


class Settings(osv.TransientModel):
    _inherit = 'base.config.settings'

    _columns = {
        'module_pdi_connector': fields.boolean('Active PDI module',
                                               help='Install Pentaho Data Integration Connector for OpenERP'),  # noqa
    }

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
