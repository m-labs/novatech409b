import sys

from sipyco.test.generic_rpc import GenericRPCCase


class GenericNovatech409BTest:
    def test_parameters_readback(self):
        # write sample data and read it back
        for i in range(4):
            self.cont.set_freq(i, 1e6)
            self.cont.set_phase(i, 0.5)
            self.cont.set_gain(i, 0.25)
        result = self.cont.get_status()

        # check for expected status message; ignore all but first 23 bytes
        # compare with previous result extracted from Novatech
        for i in range(4):
            r = result[i]
            self.assertEqual(r[0:23], "00989680 2000 01F5 0000")



class TestNovatech409BSim(GenericRPCCase, GenericNovatech409BTest):
    def setUp(self):
        GenericRPCCase.setUp(self)
        command = (sys.executable.replace("\\", "\\\\")
                            + " -m  novatech409b.aqctl_novatech409b "
                            + "-p 3254 --simulation")
        self.cont = self.start_server("korad_ka3005p", command, 3254)
