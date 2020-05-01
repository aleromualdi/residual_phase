import scipy
import numpy as np
import librosa
import librosa.display


class ResidualPhase(object):
    """
    Calculate the residual phase of a wave signal.
    The residual phase is defined as the cosine of the phase function of the
    analytic signal derived from the linear prediction (LP) residual.

    """

    def __init__(self):
        self.y = None

        self.y_hat = None
        self.r = None
        self.r_a = None
        self.residual_phase = None

    @staticmethod
    def _check_y(y):
        pass

    def _calculate_lp_residual(self, order=16):
        """
        Uses librosa.core.lpc to calculate linear prediction residual from the
        linear prediction coefficients via Burg’s method.


        Parameters
        ----------
        order : int >0 (default=16), order of the linear filter

        Returns
        -------
        res : linear prediction residual

        """

        a = librosa.lpc(self.y, order=16)
        self.y_hat = scipy.signal.lfilter([0] + -1 * a[1:], [1], self.y)
        return self.y - self.y_hat

    @staticmethod
    def _calculate_analytic_signal(res):
        """
        Calculates analytical signal of the linear prediction residual r(n)
        by Hilbert transform


        Parameters
        ----------
        res : linear prediction residual

        Returns
        -------
        res_complex : complex linear prediction residual

        """

        return scipy.signal.hilbert(res)

    def get_lp(self):
        """ get linear prediction """
        if self.y_hat.any():
            return self.y_hat

    def get_residual(self):
        """ get residual """
        if self.r.any():
            return self.r

    def get_analytic_signal(self):
        """ get analytic signal """
        if self.r_a.any():
            return self.r_a

    def calculate(self, y):
        """
        Calculate residual phase.


        Parameters
        ----------
        y : numpy array or list representing wave signal signal.

        Returns
        -------

        residual_phase: numpy array, residual phase.

        """

        self._check_y(y)
        self.y = y

        self.r = self._calculate_lp_residual()
        self.r_a = self._calculate_analytic_signal(self.r)
        self.residual_phase = self.r / np.abs(self.r_a)

        return self.residual_phase
