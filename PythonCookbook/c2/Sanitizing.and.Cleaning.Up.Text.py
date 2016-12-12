#!/etc/bin/env python
# -*- coding: utf-8 -*-
#
# Useful normalize web page with special charaters

import unicodedata
import sys

# A dict mapping every Unicode combining charater to None is created
cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode)
			 if unicodedata.combining(unichr(c)))
			 
# A translation table that maps all Unicode decimal digit charaters to their equivalent in ASCII
digimap = {c: ord('0')+unicodedata.digit(unichr(c))
		for c in range(sys.maxunicode))
		if unicodedata.category(unichr(c)) == 'Nd' }