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
class SetDevicesPropertyRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Iot', '2018-01-20', 'SetDevicesProperty','iot')

	def get_IotInstanceId(self):
		return self.get_query_params().get('IotInstanceId')

	def set_IotInstanceId(self,IotInstanceId):
		self.add_query_param('IotInstanceId',IotInstanceId)

	def get_DeviceNames(self):
		return self.get_query_params().get('DeviceNames')

	def set_DeviceNames(self,DeviceNames):
		for i in range(len(DeviceNames)):	
			if DeviceNames[i] is not None:
				self.add_query_param('DeviceName.' + str(i + 1) , DeviceNames[i]);

	def get_ProductKey(self):
		return self.get_query_params().get('ProductKey')

	def set_ProductKey(self,ProductKey):
		self.add_query_param('ProductKey',ProductKey)

	def get_Items(self):
		return self.get_query_params().get('Items')

	def set_Items(self,Items):
		self.add_query_param('Items',Items)