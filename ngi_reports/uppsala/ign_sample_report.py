#!/usr/bin/env python

""" Uppsala module for dealing with fields for the IGN Sample Report
"""

import os
from ngi_reports.common import ign_sample_report

class Report(ign_sample_report.CommonReport):

    # Initialise the report
    def __init__(self, config, LOG, working_dir, **kwargs):

        # Set node
        self.ngi_node = 'uppsala'

        # Initialise the parent class
        super(Report, self).__init__(config, LOG, working_dir, **kwargs)

        # Create the plots
        self.LOG.debug('Plotting graphs')
        self.make_plots()

        #### Missing Fields
        # self.info['recipient']
        # self.project['prep']
        # self.project['UPPMAXid']
        # self.samples[sid]['user_sample_id']
        # self.samples[sid]['barcode']
