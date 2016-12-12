#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib, urllib2
import json
import sys, os, warnings
# import getpass
import logging

DEBUG = True

logging.basicConfig(level=logging.DEBUG)

def curry(_curried_func, *args, **kwargs):
    def _curried(*moreargs, **morekwargs):
        return _curried_func(*(args + moreargs), **dict(kwargs, **morekwargs))
    return _curried

class RESTClient(object):
    """
    .. note:: If any boolean arguments are defined, they're
    automatically added to the GET request, which means the
    webservices API will treat them as being true. You've been warned.
    """

    # List all methods defined in the REST API
    METHODS = dict(test='glpi.test',
                   status='glpi.status',
                   listAllMethods='glpi.listAllMethods',
                   listEntities='glpi.listEntities',
                   doLogin='glpi.doLogin',
                   listKnowBaseItems='glpi.listKnowBaseItems',
                   getKnowBaseItem='glpi.getKnowBaseItem',
                   getDocument='glpi.getDocument',
                   doLogout='glpi.doLogout',
                   getMyInfo='glpi.getMyInfo',
                   listMyProfiles='glpi.listMyProfiles',
                   setMyProfile='glpi.setMyProfile',
                   listMyEntities='glpi.listMyEntities',
                   setMyEntity='glpi.setMyEntity',
                   listDropdownValues='glpi.listDropdownValues',
                   listGroups='glpi.listGroups',
                   listHelpdeskTypes='glpi.listHelpdeskTypes',
                   listHelpdeskItems='glpi.listHelpdeskItems',
                   listTickets='glpi.listTickets',
                   listUsers='glpi.listUsers',
                   listInventoryObjects='glpi.listInventoryObjects',
                   listObjects='glpi.listObjects',
                   getObject='glpi.getObject',
                   createObjects='glpi.createObjects',
                   deleteObjects='glpi.deleteObjects',
                   updateObjects='glpi.updateObjects',
                   linkObjects='glpi.linkObjects',
                   getInfocoms='glpi.getInfocoms',
                   getContracts='glpi.getContracts',
                   getComputer='glpi.getComputer',
                   getComputerInfoComs='glpi.getComputerInfoComs',
                   getComputerContracts='glpi.getComputerContracts',
                   getNetworkports='glpi.getNetworkports',
                   listComputers='glpi.listComputers',
                   getPhones='glpi.getPhones',
                   getNetworkEquipment='glpi.getNetworkEquipment',
                   getTicket='glpi.getTicket',
                   createTicket='glpi.createTicket',
                   addTicketFollowup='glpi.addTicketFollowup',
                   addTicketDocument='glpi.addTicketDocument',
                   addTicketObserver='glpi.addTicketObserver',
                   setTicketSatisfaction='glpi.setTicketSatisfaction',
                   setTicketValidation='glpi.setTicketValidation',)

    def __init__(self, host='glpi', baseurl='/glpi',):
        '''
        Initialize the RESTClient instance, adding supported glpi-methods by currying self._get_METHOD
        '''
        self.BASEURL = baseurl
        self._url = 'http://' + host + '/' + self.BASEURL + '/plugins/webservices/rest.php?'
        for method in self.METHODS.keys():
            setattr(self, 'get_%s' % (method),
                    curry(self._get_METHOD, self.METHODS.get(method)))

    def _get_METHOD(self, method, **kwargs):
        '''

        Private method that perform the call to glpi server with the glpi method
        and providing parameters as kwargs
        @param method: GLPI method to call
        @param kwargs: parameters to send to glpi test
        '''
        if not self.connected:
            self.connect(login_name='webservices', login_password='webservices')
        response = self.send_request(method, **kwargs)
        DEBUG and logging.debug(u'RESTClient::get_%s() '
                      u'response = %s'
                      % (method, response,))

        return response

    # Attributes
    _session = None
    _url = None

    @property
    def session(self):
        '''
        The session string
        '''
        return self._session

    @property
    def connected(self):
        '''
        tests in client is connected to the server
        '''
        return self.session is not None

    @property
    def url(self):
        ''' The complete url '''
        return self._url

    @staticmethod
    def _is_fault(response):
        '''
        tests if a fault has been raised by the server
        @param response: the decoded respose object
        @return: False if there is no error
        @raise Exception: if a server side error has been raised
        '''
        DEBUG and logging.debug(u'RESTClient::_is_fault() '
                     u'response = %s'
                     % (response,))

        if (isinstance(response, (dict))):
            faultCode = response.get('faultCode')
            faultString = response.get('faultString')
            if (faultCode is not None):
                raise Exception('Fault returned by GLPI service : %s : %s' % (faultCode, faultString,))
        # There is no server-side fault.
        return False

    def _build_url(self, method, params=None):
        '''
        private method to build the final url sent to the server
        @param method: the glpi method
        @param params: params to join to the request
        @return: the final url that will be sent
        '''
        _params = {"method": method, }
        if params:
            _params.update(params)
        _url = self.url + urllib.urlencode(_params)
        logging.debug(u'RESTClient::_build_url(%s, %s) '
                     u'_url = %s '
                     % (method, params, _url,))
        return _url

    def send_request(self, method, **kwargs):
        '''
        send a request to GLPI server and returns the json-decoded response

        @param method: glpi-method
        @param kwargs: extra-parameters to pass to the method
        @return: response object json-decoded
        @raise Exception: if the server raises {'faultCode', 'faultString'}
            or if something has failed.
        '''
        self.connected and logging.debug(u'RESTClient::get(%s, %s) '
                                         u'CONNECTED !'
                                         % (method, kwargs,))
        # Prepares parameters
        _params = {'method': method, }
        if kwargs:
            _params.update(kwargs)

        # Append session to parameters
        if self.session:
            _params['session'] = self.session

        url = self._build_url(method, _params)
        request = urllib2.Request(url)

        # Sends the request
        try:
            response = urllib2.urlopen(request)
            headers = response.headers
            read = response.read()
            logging.debug(u'RESTClient::send_request(%s, %s) '
                     u'response: %s /'
                     % (method, kwargs, read,))
            json_decoded = json.loads(read)
            if not RESTClient._is_fault(json_decoded):  # An exception is raised on protocol or glpi method error
                return json_decoded
        except Exception as e:
            # Exception is re-raised
            raise e

    def connect(self, login_name=None, login_password=None):
        """
        Connect to a running GLPI instance that has the webservices
        plugin enabled.

        Returns True if connection was successful.

        :type login_name: string
        :type login_password: string
        :param host: hostname of the GLPI server, has not been tested with HTTPS
        :param login_name: your GLPI username
        :param login_password: pretty obvious
        """
        self.login_name = login_name
        self.login_password = login_password

        if self.login_name != None and self.login_password != None:
            params = {'login_name':login_name,
                      'login_password': (login_password), }
            response = self.send_request("glpi.doLogin", **params)
            session_id = response.get('session')
            if session_id is not None:
                self._session = session_id
                return True
            else:
                raise Exception("Login incorrect or server down")
        else:
            logging.warning("Connected anonymously, will only be able to use non-authenticated methods")
            return self