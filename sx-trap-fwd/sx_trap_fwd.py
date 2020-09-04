#!/usr/bin/env python
'''
This script enables forwarding of Control Plane protocols on Spectrum switches
'''

import sys

sys.path.append('/lib/python2.7/dist-packages/python_sdk_api/')
sys.path.append('/lib/python2.7/site-packages/python_sdk_api/')
sys.path.append('/usr/lib/python2.7/dist-packages/python_sdk_api/')
sys.path.append('/usr/lib/python2.7/site-packages/python_sdk_api/')
sys.path.append('/usr/local/lib/python2.7/dist-packages/python_sdk_api/')
sys.path.append('/usr/local/lib/python2.7/site-packages/python_sdk_api/')
try:
    from sx_api import *
except:
    print("Error: can't import SX SDK API Python library!")
    sys.exit(-1)

SWID = 0

rc, handle = sx_api_open(None)
assert rc == SX_STATUS_SUCCESS, "sx_api_open failed, rc: %d" % (rc)

# Create trap group
TRAP_GROUP = 1
trap_grp_attr = sx_trap_group_attributes_t()
trap_grp_attr.control_type = SX_CONTROL_TYPE_DEFAULT
trap_grp_attr.prio = 1
trap_grp_attr.truncate_mode = SX_TRUNCATE_MODE_DISABLE
trap_grp_attr.truncate_size = 0
rc = sx_api_host_ifc_trap_group_set(handle, SWID, TRAP_GROUP, trap_grp_attr)
assert rc == SX_STATUS_SUCCESS, "sx_api_host_ifc_trap_group_set failed, rc: %d" % (rc)

sx_host_ifc_trap_key_p = new_sx_host_ifc_trap_key_t_p()
sx_host_ifc_trap_key = sx_host_ifc_trap_key_t()
sx_host_ifc_trap_key.type = HOST_IFC_TRAP_KEY_TRAP_ID_E

sx_host_ifc_trap_attr_p = new_sx_host_ifc_trap_attr_t_p()
sx_host_ifc_trap_attr = sx_host_ifc_trap_attr_t()
sx_host_ifc_trap_attr.attr.trap_id_attr.trap_group = 1
sx_host_ifc_trap_attr.attr.trap_id_attr.trap_action = SX_TRAP_ACTION_IGNORE
sx_host_ifc_trap_attr_t_p_assign(sx_host_ifc_trap_attr_p, sx_host_ifc_trap_attr)

sx_host_ifc_trap_key.trap_key_attr.trap_id = SX_TRAP_ID_ETH_L2_STP
sx_host_ifc_trap_key_t_p_assign(sx_host_ifc_trap_key_p, sx_host_ifc_trap_key)
rc = sx_api_host_ifc_trap_id_ext_set(handle, SX_ACCESS_CMD_SET, sx_host_ifc_trap_key_p, sx_host_ifc_trap_attr_p)
assert rc == SX_STATUS_SUCCESS, "sx_api_host_ifc_trap_id_ext_set STP failed, rc: %d" % (rc)

sx_host_ifc_trap_key.trap_key_attr.trap_id = SX_TRAP_ID_ETH_L2_LACP
sx_host_ifc_trap_key_t_p_assign(sx_host_ifc_trap_key_p, sx_host_ifc_trap_key)
rc = sx_api_host_ifc_trap_id_ext_set(handle, SX_ACCESS_CMD_SET, sx_host_ifc_trap_key_p, sx_host_ifc_trap_attr_p)
assert rc == SX_STATUS_SUCCESS, "sx_api_host_ifc_trap_id_ext_set LACP failed, rc: %d" % (rc)

sx_host_ifc_trap_key.trap_key_attr.trap_id = SX_TRAP_ID_ETH_L2_EAPOL
sx_host_ifc_trap_key_t_p_assign(sx_host_ifc_trap_key_p, sx_host_ifc_trap_key)
rc = sx_api_host_ifc_trap_id_ext_set(handle, SX_ACCESS_CMD_SET, sx_host_ifc_trap_key_p, sx_host_ifc_trap_attr_p)
assert rc == SX_STATUS_SUCCESS, "sx_api_host_ifc_trap_id_ext_set EAPOL failed, rc: %d" % (rc)

sx_host_ifc_trap_key.trap_key_attr.trap_id = SX_TRAP_ID_ETH_L2_LLDP
sx_host_ifc_trap_key_t_p_assign(sx_host_ifc_trap_key_p, sx_host_ifc_trap_key)
rc = sx_api_host_ifc_trap_id_ext_set(handle, SX_ACCESS_CMD_SET, sx_host_ifc_trap_key_p, sx_host_ifc_trap_attr_p)
assert rc == SX_STATUS_SUCCESS, "sx_api_host_ifc_trap_id_ext_set LLDP failed, rc: %d" % (rc)

sx_host_ifc_trap_key.trap_key_attr.trap_id = SX_TRAP_ID_ETH_L2_MMRP
sx_host_ifc_trap_key_t_p_assign(sx_host_ifc_trap_key_p, sx_host_ifc_trap_key)
rc = sx_api_host_ifc_trap_id_ext_set(handle, SX_ACCESS_CMD_SET, sx_host_ifc_trap_key_p, sx_host_ifc_trap_attr_p)
assert rc == SX_STATUS_SUCCESS, "sx_api_host_ifc_trap_id_ext_set MMRP failed, rc: %d" % (rc)

sx_host_ifc_trap_key.trap_key_attr.trap_id = SX_TRAP_ID_ETH_L2_MVRP
sx_host_ifc_trap_key_t_p_assign(sx_host_ifc_trap_key_p, sx_host_ifc_trap_key)
rc = sx_api_host_ifc_trap_id_ext_set(handle, SX_ACCESS_CMD_SET, sx_host_ifc_trap_key_p, sx_host_ifc_trap_attr_p)
assert rc == SX_STATUS_SUCCESS, "sx_api_host_ifc_trap_id_ext_set MVRP failed, rc: %d" % (rc)

sx_host_ifc_trap_key.trap_key_attr.trap_id = SX_TRAP_ID_ETH_L2_RPVST
sx_host_ifc_trap_key_t_p_assign(sx_host_ifc_trap_key_p, sx_host_ifc_trap_key)
rc = sx_api_host_ifc_trap_id_ext_set(handle, SX_ACCESS_CMD_SET, sx_host_ifc_trap_key_p, sx_host_ifc_trap_attr_p)
assert rc == SX_STATUS_SUCCESS, "sx_api_host_ifc_trap_id_ext_set RPVST failed, rc: %d" % (rc)

sx_host_ifc_trap_key.trap_key_attr.trap_id = SX_TRAP_ID_ETH_L2_IGMP_TYPE_QUERY
sx_host_ifc_trap_key_t_p_assign(sx_host_ifc_trap_key_p, sx_host_ifc_trap_key)
rc = sx_api_host_ifc_trap_id_ext_set(handle, SX_ACCESS_CMD_SET, sx_host_ifc_trap_key_p, sx_host_ifc_trap_attr_p)
assert rc == SX_STATUS_SUCCESS, "sx_api_host_ifc_trap_id_ext_set IGMP_TYPE_QUERY failed, rc: %d" % (rc)

sx_host_ifc_trap_key.trap_key_attr.trap_id = SX_TRAP_ID_ETH_L2_IGMP_TYPE_V1_REPORT
sx_host_ifc_trap_key_t_p_assign(sx_host_ifc_trap_key_p, sx_host_ifc_trap_key)
rc = sx_api_host_ifc_trap_id_ext_set(handle, SX_ACCESS_CMD_SET, sx_host_ifc_trap_key_p, sx_host_ifc_trap_attr_p)
assert rc == SX_STATUS_SUCCESS, "sx_api_host_ifc_trap_id_ext_set IGMP_TYPE_V1_REPORT failed, rc: %d" % (rc)

sx_host_ifc_trap_key.trap_key_attr.trap_id = SX_TRAP_ID_ETH_L2_IGMP_TYPE_V2_REPORT
sx_host_ifc_trap_key_t_p_assign(sx_host_ifc_trap_key_p, sx_host_ifc_trap_key)
rc = sx_api_host_ifc_trap_id_ext_set(handle, SX_ACCESS_CMD_SET, sx_host_ifc_trap_key_p, sx_host_ifc_trap_attr_p)
assert rc == SX_STATUS_SUCCESS, "sx_api_host_ifc_trap_id_ext_set IGMP_TYPE_V2_REPORT failed, rc: %d" % (rc)

sx_host_ifc_trap_key.trap_key_attr.trap_id = SX_TRAP_ID_ETH_L2_IGMP_TYPE_V2_LEAVE
sx_host_ifc_trap_key_t_p_assign(sx_host_ifc_trap_key_p, sx_host_ifc_trap_key)
rc = sx_api_host_ifc_trap_id_ext_set(handle, SX_ACCESS_CMD_SET, sx_host_ifc_trap_key_p, sx_host_ifc_trap_attr_p)
assert rc == SX_STATUS_SUCCESS, "sx_api_host_ifc_trap_id_ext_set IGMP_TYPE_V2_LEAVE failed, rc: %d" % (rc)

sx_host_ifc_trap_key.trap_key_attr.trap_id = SX_TRAP_ID_ETH_L2_IGMP_TYPE_V3_REPORT
sx_host_ifc_trap_key_t_p_assign(sx_host_ifc_trap_key_p, sx_host_ifc_trap_key)
rc = sx_api_host_ifc_trap_id_ext_set(handle, SX_ACCESS_CMD_SET, sx_host_ifc_trap_key_p, sx_host_ifc_trap_attr_p)
assert rc == SX_STATUS_SUCCESS, "sx_api_host_ifc_trap_id_ext_set IGMP_TYPE_V3_REPORT failed, rc: %d" % (rc)

sx_host_ifc_trap_key.trap_key_attr.trap_id = SX_TRAP_ID_ETH_L2_DHCP
sx_host_ifc_trap_key_t_p_assign(sx_host_ifc_trap_key_p, sx_host_ifc_trap_key)
rc = sx_api_host_ifc_trap_id_ext_set(handle, SX_ACCESS_CMD_SET, sx_host_ifc_trap_key_p, sx_host_ifc_trap_attr_p)
assert rc == SX_STATUS_SUCCESS, "sx_api_host_ifc_trap_id_ext_set DHCP failed, rc: %d" % (rc)

sx_host_ifc_trap_key.trap_key_attr.trap_id = SX_TRAP_ID_ETH_L2_UDLD
sx_host_ifc_trap_key_t_p_assign(sx_host_ifc_trap_key_p, sx_host_ifc_trap_key)
rc = sx_api_host_ifc_trap_id_ext_set(handle, SX_ACCESS_CMD_SET, sx_host_ifc_trap_key_p, sx_host_ifc_trap_attr_p)
assert rc == SX_STATUS_SUCCESS, "sx_api_host_ifc_trap_id_ext_set UDLD failed, rc: %d" % (rc)

sx_host_ifc_trap_key.trap_key_attr.trap_id = SX_TRAP_ID_ARP_REQUEST
sx_host_ifc_trap_key_t_p_assign(sx_host_ifc_trap_key_p, sx_host_ifc_trap_key)
rc = sx_api_host_ifc_trap_id_ext_set(handle, SX_ACCESS_CMD_SET, sx_host_ifc_trap_key_p, sx_host_ifc_trap_attr_p)
assert rc == SX_STATUS_SUCCESS, "sx_api_host_ifc_trap_id_ext_set ARP_REQUEST failed, rc: %d" % (rc)

sx_host_ifc_trap_key.trap_key_attr.trap_id = SX_TRAP_ID_ARP_RESPONSE
sx_host_ifc_trap_key_t_p_assign(sx_host_ifc_trap_key_p, sx_host_ifc_trap_key)
rc = sx_api_host_ifc_trap_id_ext_set(handle, SX_ACCESS_CMD_SET, sx_host_ifc_trap_key_p, sx_host_ifc_trap_attr_p)
assert rc == SX_STATUS_SUCCESS, "sx_api_host_ifc_trap_id_ext_set ARP_RESPONSE failed, rc: %d" % (rc)

rc = sx_api_close(handle)
assert rc == SX_STATUS_SUCCESS, "sx_api_close failed, rc: %d" % (rc)