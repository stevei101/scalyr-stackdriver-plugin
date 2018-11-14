import random

from scalyr_agent import ScalyrMonitor

class RandomCoinMonitor(ScalyrMonitor):
    def _initialize(self):
        self.__counter = 0
        # Read two optional config fields.  You may also create a required
        # configuration  field by supplying the argument
        # ‘require_field=True’.  Then, if the user does not supply the
        # field in the monitor’s configuration, an exception will be raised.
        self.__gauss_mean = self._config.get('gauss_mean',
                                             default=0.5,
                                             convert_to=float,
                                             min_value=0,
                                             max_value=10)
        self.__gauss_stddev = self._config.get('gauss_stddev',
                                               default=0.25,
                                               convert_to=float,
                                               min_value=0,
                                               max_value=5)


    def gather_sample(self):
        self.__counter += 1
        self._logger.emit_value('uniform', random.random(),
                                extra_fields={'count': self.__counter})
        self._logger.emit_value('gauss', random.gauss(self.__gauss_mean,
                                                      self.__gauss_stddev),
                                extra_fields={'count': self.__counter})