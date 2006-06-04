# -*- coding: utf-8 -*-
# browsershots.org
# Copyright (C) 2006 Johann C. Rocholl <johann@browsershots.org>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston,
# MA 02111-1307, USA.

"""
Database interface for nonce table.
"""

__revision__ = '$Rev$'
__date__ = '$Date$'
__author__ = '$Author$'

import md5, random, time, os

def random_md5():
    """
    Make a random 128bit hexadecimal authentication token.
    """
    digest = md5.new()
    digest.update('%.50f' % random.random())
    digest.update('%.20f' % time.time())
    digest.update(os.urandom(16))
    return digest.hexdigest()

def create_factory_nonce(factory, ip):
    """
    Make a factory nonce and save it in the database.
    """
    nonce = random_md5()
    cur.execute("INSERT INTO nonce (nonce, factory, ip) VALUES (%s, %s, %s)",
                (nonce, factory, ip))
    return nonce