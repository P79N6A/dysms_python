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
class DescribeInstancesFullStatusRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ecs', '2014-05-26', 'DescribeInstancesFullStatus','ecs')

	def get_EventIds(self):
		return self.get_query_params().get('EventIds')

	def set_EventIds(self,EventIds):
		for i in range(len(EventIds)):	
			if EventIds[i] is not None:
				self.add_query_param('EventId.' + str(i + 1) , EventIds[i]);

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_PageNumber(self):
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self,PageNumber):
		self.add_query_param('PageNumber',PageNumber)

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)

	def get_EventPublishTimeEnd(self):
		return self.get_query_params().get('EventPublishTime.End')

	def set_EventPublishTimeEnd(self,EventPublishTimeEnd):
		self.add_query_param('EventPublishTime.End',EventPublishTimeEnd)

	def get_InstanceEventTypes(self):
		return self.get_query_params().get('InstanceEventTypes')

	def set_InstanceEventTypes(self,InstanceEventTypes):
		for i in range(len(InstanceEventTypes)):	
			if InstanceEventTypes[i] is not None:
				self.add_query_param('InstanceEventType.' + str(i + 1) , InstanceEventTypes[i]);

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_OwnerAccount(self):
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self,OwnerAccount):
		self.add_query_param('OwnerAccount',OwnerAccount)

	def get_NotBeforeStart(self):
		return self.get_query_params().get('NotBefore.Start')

	def set_NotBeforeStart(self,NotBeforeStart):
		self.add_query_param('NotBefore.Start',NotBeforeStart)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_EventPublishTimeStart(self):
		return self.get_query_params().get('EventPublishTime.Start')

	def set_EventPublishTimeStart(self,EventPublishTimeStart):
		self.add_query_param('EventPublishTime.Start',EventPublishTimeStart)

	def get_InstanceIds(self):
		return self.get_query_params().get('InstanceIds')

	def set_InstanceIds(self,InstanceIds):
		for i in range(len(InstanceIds)):	
			if InstanceIds[i] is not None:
				self.add_query_param('InstanceId.' + str(i + 1) , InstanceIds[i]);

	def get_NotBeforeEnd(self):
		return self.get_query_params().get('NotBefore.End')

	def set_NotBeforeEnd(self,NotBeforeEnd):
		self.add_query_param('NotBefore.End',NotBeforeEnd)

	def get_HealthStatus(self):
		return self.get_query_params().get('HealthStatus')

	def set_HealthStatus(self,HealthStatus):
		self.add_query_param('HealthStatus',HealthStatus)

	def get_EventType(self):
		return self.get_query_params().get('EventType')

	def set_EventType(self,EventType):
		self.add_query_param('EventType',EventType)

	def get_Status(self):
		return self.get_query_params().get('Status')

	def set_Status(self,Status):
		self.add_query_param('Status',Status)