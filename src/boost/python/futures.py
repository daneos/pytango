################################################################################
##
## This file is part of PyTango, a python binding for Tango
##
## http://www.tango-controls.org/static/PyTango/latest/doc/html/index.html
##
## Copyright 2011 CELLS / ALBA Synchrotron, Bellaterra, Spain
##
## PyTango is free software: you can redistribute it and/or modify
## it under the terms of the GNU Lesser General Public License as published by
## the Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.
##
## PyTango is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU Lesser General Public License for more details.
##
## You should have received a copy of the GNU Lesser General Public License
## along with PyTango.  If not, see <http://www.gnu.org/licenses/>.
##
################################################################################

"""This module exposes a futures version of :class:`PyTango.DeviceProxy` and
:class:`PyTango.AttributeProxy"""

__all__ = ["DeviceProxy", "AttributeProxy"]

from functools import partial

from PyTango import GreenMode
from PyTango.device_proxy import get_device_proxy
from PyTango.attribute_proxy import get_attribute_proxy


DeviceProxy = partial(get_device_proxy, green_mode=GreenMode.Futures)
DeviceProxy.__doc__ = """
    DeviceProxy(self, dev_name, wait=True, timeout=True) -> DeviceProxy
    DeviceProxy(self, dev_name, need_check_acc, wait=True, timeout=True) -> DeviceProxy

    Creates a *futures* enabled :class:`~PyTango.DeviceProxy`.
     
    The DeviceProxy constructor internally makes some network calls which makes
    it *slow*. By using the futures *green mode* you are allowing other
    python code to be executed in a cooperative way.

    .. note::
        The timeout parameter has no relation with the tango device client side
        timeout (gettable by :meth:`~PyTango.DeviceProxy.get_timeout_millis` and 
        settable through :meth:`~PyTango.DeviceProxy.set_timeout_millis`)

    :param dev_name: the device name or alias
    :type dev_name: str
    :param need_check_acc: in first version of the function it defaults to True.
                           Determines if at creation time of DeviceProxy it 
                           should check for channel access (rarely used)
    :type need_check_acc: bool
    :param wait: whether or not to wait for result of creating a DeviceProxy.
    :type wait: bool
    :param timeout: The number of seconds to wait for the result.
                    If None, then there is no limit on the wait time.
                    Ignored when wait is False.
    :type timeout: float
    :returns:
        if wait is True:
            :class:`~PyTango.DeviceProxy`
        else:
            :class:`concurrent.futures.Future`
    :throws:
        * a *DevFailed* if wait is True and there is an error creating 
          the device.
        * a *concurrent.futures.TimeoutError* if wait is False, timeout is not
          None and the time to create the device has expired.                            

    New in PyTango 8.1.0
"""

AttributeProxy = partial(get_attribute_proxy, green_mode=GreenMode.Futures)
AttributeProxy.__doc__ = """
    AttributeProxy(self, full_attr_name, wait=True, timeout=True) -> AttributeProxy
    AttributeProxy(self, device_proxy, attr_name, wait=True, timeout=True) -> AttributeProxy

    Creates a *futures* enabled :class:`~PyTango.AttributeProxy`.
    
    The AttributeProxy constructor internally makes some network calls which
    makes it *slow*. By using the *gevent mode* you are allowing other python
    code to be executed in a cooperative way.

    :param full_attr_name: the full name of the attribute
    :type full_attr_name: str
    :param device_proxy: the :class:`~PyTango.DeviceProxy`
    :type device_proxy: DeviceProxy
    :param attr_name: attribute name for the given device proxy
    :type attr_name: str
    :param wait: whether or not to wait for result of creating an
                 AttributeProxy.
    :type wait: bool
    :param timeout: The number of seconds to wait for the result.
                    If None, then there is no limit on the wait time.
                    Ignored when wait is False.
    :type timeout: float
    :returns:
        if wait is True:
            :class:`~PyTango.AttributeProxy`
        else:
            :class:`concurrent.futures.Future`
    :throws:
        * a *DevFailed* if wait is True  and there is an error creating the
          attribute.
        * a *concurrent.futures.TimeoutError* if wait is False, timeout is not
          None and the time to create the attribute has expired.
    
    New in PyTango 8.1.0
"""

del GreenMode
del get_device_proxy
del get_attribute_proxy