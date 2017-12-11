# -*- coding: utf-8 -*-
"""
Fingerprint implementation for android
======================================

Usage::

    from fingerprint import Fingerprint

    def on_authentication_succeeded(result):
        print("It worked ?", result)

    fp = Fingerprint(on_authentication_succeeded=on_authentication_succeeded)
    fp.authenticate()

"""

from jnius import autoclass, cast, PythonJavaClass, java_method
from kivy.event import EventDispatcher


FingerprintManager = autoclass("android.hardware.fingerprint.FingerprintManager")
FingerprintCallback = autoclass("org.fingerprint.FingerprintCallback")
activity = autoclass("org.kivy.android.PythonActivity").mActivity


class PyFingerprintCallback(PythonJavaClass):
    __javainterfaces__ = ["org/fingerprint/FingerprintCallbackInterface"]
    __javacontext__ = "app"

    def __init__(self, dispatcher):
        self.dispatcher = dispatcher
        super(PyFingerprintCallback, self).__init__()

    @java_method("(ILjava/lang/CharSequence;)V")
    def onAuthenticationError(self, errorCode, errString):
        self.dispatcher.dispatch(
            "on_authentication_error", errorCode, errString)

    @java_method("()V")
    def onAuthenticationFailed(self):
        self.dispatcher.dispatch("on_authentication_failed")

    @java_method("(ILjava/lang/CharSequence;)V")
    def onAuthenticationHelp(self, helpCode, helpString):
        self.dispatcher.dispatch(
            "on_authentication_help", helpCode, helpString)

    @java_method("(Landroid.hardware.fingerprint."
                 "FingerprintManager$AuthenticationResult;)V")
    def onAuthenticationSucceeded(self, result):
        self.dispatcher.dispatch(
            "on_authentication_succeeded", result)


class Fingerprint(EventDispatcher):

    _manager = None
    _py_callback = None
    _callback = None
    __events__ = (
        "on_authentication_error",
        "on_authentication_failed",
        "on_authentication_help",
        "on_authentication_succeeded"
    )

    @property
    def manager(self):
        if self._manager is None:
            self._manager = cast(
                FingerprintManager,
                activity.getSystemService(FingerprintManager))
            self._py_callback = PyFingerprintCallback(self)
            self._callback = FingerprintCallback()
            self._callback.setDispatcher(self._py_callback)
        return self._manager

    def authenticate(self):
        self._authenticate = self.manager.authenticate(self._callback)

    def on_authentication_error(self, error_code, error_str):
        pass

    def on_authentication_failed(self):
        pass

    def on_authentication_help(self, help_code, help_string):
        pass

    def on_authentication_succeeded(self, result):
        pass
