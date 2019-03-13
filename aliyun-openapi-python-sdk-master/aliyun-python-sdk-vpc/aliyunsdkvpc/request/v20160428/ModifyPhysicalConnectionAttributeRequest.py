# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
class ModifyPhysicalConnectionAttributeRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Vpc', '2016-04-28', 'ModifyPhysicalConnectionAttribute','vpc')

	def get_RedundantPhysicalConnectionId(self):
		return self.get_query_params().get('RedundantPhysicalConnectionId')

	def set_RedundantPhysicalConnectionId(self,RedundantPhysicalConnectionId):
		self.add_query_param('RedundantPhysicalConnectionId',RedundantPhysicalConnectionId)

	def get_PeerLocation(self):
		return self.get_query_params().get('PeerLocation')

	def set_PeerLocation(self,PeerLocation):
		self.add_query_param('PeerLocation',PeerLocation)

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_PortType(self):
		return self.get_query_params().get('PortType')

	def set_PortType(self,PortType):
		self.add_query_param('PortType',PortType)

	def get_CircuitCode(self):
		return self.get_query_params().get('CircuitCode')

	def set_CircuitCode(self,CircuitCode):
		self.add_query_param('CircuitCode',CircuitCode)

	def get_bandwidth(self):
		return self.get_query_params().get('bandwidth')

	def set_bandwidth(self,bandwidth):
		self.add_query_param('bandwidth',bandwidth)

	def get_ClientToken(self):
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self,ClientToken):
		self.add_query_param('ClientToken',ClientToken)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_OwnerAccount(self):
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self,OwnerAccount):
		self.add_query_param('OwnerAccount',OwnerAccount)

	def get_Description(self):
		return self.get_query_params().get('Description')

	def set_Description(self,Description):
		self.add_query_param('Description',Description)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_LineOperator(self):
		return self.get_query_params().get('LineOperator')

	def set_LineOperator(self,LineOperator):
		self.add_query_param('LineOperator',LineOperator)

	def get_PhysicalConnectionId(self):
		return self.get_query_params().get('PhysicalConnectionId')

	def set_PhysicalConnectionId(self,PhysicalConnectionId):
		self.add_query_param('PhysicalConnectionId',PhysicalConnectionId)

	def get_Name(self):
		return self.get_query_params().get('Name')

	def set_Name(self,Name):
		self.add_query_param('Name',Name)