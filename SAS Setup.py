# Databricks notebook source
import saspy, os, pandas

# COMMAND ----------

config_file_data = """
SAS_config_names=['oda']
oda = {'java' : '/usr/bin/java',
'iomhost' : ['odaws01-usw2.oda.sas.com','odaws02-usw2.oda.sas.com','odaws03-usw2.oda.sas.com','odaws04-usw2.oda.sas.com'],
'iomport' : 8591,
'omruser' : 'SAS ODA USERNAME',
'omrpw' : 'SAS ODA PASSWORD',
'encoding' : 'utf-8',
'display' : 'databricks'
}
"""

# COMMAND ----------

import saspy, os
sas_config_path = saspy.__file__.replace('__init__.py', 'sascfg_personal.py')
print(sas_config_path)

# COMMAND ----------

#Write config file
with open(sas_config_path, "w") as cfile:
    cfile.write(config_file_data)

# COMMAND ----------

sas = saspy.SASsession(cfgname='oda')

# COMMAND ----------


